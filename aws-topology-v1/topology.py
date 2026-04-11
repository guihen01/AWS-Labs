import boto3
from diagrams import Diagram, Cluster

# NETWORK
from diagrams.aws.network import (
    VPC, PublicSubnet, PrivateSubnet,
    InternetGateway, NATGateway, RouteTable,
    ELB, Endpoint, TransitGateway
)

# COMPUTE / DB / SECURITY
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS


region = "ca-central-1"

ec2 = boto3.client("ec2", region_name=region)
elbv2 = boto3.client("elbv2", region_name=region)
rds = boto3.client("rds", region_name=region)

# ======================
# DATA COLLECTION
# ======================
vpcs = ec2.describe_vpcs()["Vpcs"]
subnets = ec2.describe_subnets()["Subnets"]
igws = ec2.describe_internet_gateways()["InternetGateways"]
natgws = ec2.describe_nat_gateways()["NatGateways"]
rts = ec2.describe_route_tables()["RouteTables"]

instances = ec2.describe_instances()["Reservations"]
lbs = elbv2.describe_load_balancers()["LoadBalancers"]
target_groups = elbv2.describe_target_groups()["TargetGroups"]

dbs = rds.describe_db_instances()["DBInstances"]
endpoints = ec2.describe_vpc_endpoints()["VpcEndpoints"]

tgws = ec2.describe_transit_gateways()["TransitGateways"]
tgw_attachments = ec2.describe_transit_gateway_attachments()["TransitGatewayAttachments"]

# ======================
# DIAGRAM
# ======================
with Diagram("AWS Full Topology", show=False, direction="LR"):

    ec2_nodes = {}
    subnet_map = {}

    for vpc in vpcs:
        vpc_node = VPC(vpc["CidrBlock"])

        # IGW
        igw_node = None
        for igw in igws:
            for att in igw.get("Attachments", []):
                if att["VpcId"] == vpc["VpcId"]:
                    igw_node = InternetGateway("IGW")
                    igw_node >> vpc_node

        with Cluster(f"VPC {vpc['CidrBlock']}"):

            private_subnets = []

            # SUBNETS
            for subnet in subnets:
                if subnet["VpcId"] != vpc["VpcId"]:
                    continue

                cidr = subnet["CidrBlock"]
                is_public = False
                used_rt = None

                for rt in rts:
                    for assoc in rt.get("Associations", []):
                        if assoc.get("SubnetId") == subnet["SubnetId"]:
                            used_rt = rt

                    for route in rt.get("Routes", []):
                        if route.get("GatewayId", "").startswith("igw"):
                            is_public = True

                sn = PublicSubnet(cidr) if is_public else PrivateSubnet(cidr)
                vpc_node >> sn
                subnet_map[subnet["SubnetId"]] = sn

                if not is_public:
                    private_subnets.append((sn, used_rt))

            # NAT
            for nat in natgws:
                if nat["VpcId"] != vpc["VpcId"]:
                    continue

                nat_node = NATGateway("NAT")

                for sn, rt in private_subnets:
                    if not rt:
                        continue

                    for route in rt.get("Routes", []):
                        if route.get("NatGatewayId") == nat["NatGatewayId"]:
                            rt_node = RouteTable("RT")
                            sn >> rt_node >> nat_node

            # ======================
            # EC2
            # ======================
            for res in instances:
                for inst in res["Instances"]:
                    sid = inst.get("SubnetId")
                    iid = inst["InstanceId"]

                    if sid in subnet_map:
                        node = EC2(iid)
                        subnet_map[sid] >> node
                        ec2_nodes[iid] = node

                        

            # ======================
            # ALB + TARGET GROUPS
            # ======================
            tg_map = {}

            for tg in target_groups:
                tg_arn = tg["TargetGroupArn"]
                tg_node = ELB(tg["TargetGroupName"])
                tg_map[tg_arn] = tg_node

            for lb in lbs:
                lb_node = ELB(lb["LoadBalancerName"])

                # ALB → Subnets
                for az in lb.get("AvailabilityZones", []):
                    sid = az.get("SubnetId")
                    if sid in subnet_map:
                        subnet_map[sid] >> lb_node

                # ALB → TG → EC2
                try:
                    listeners = elbv2.describe_listeners(
                        LoadBalancerArn=lb["LoadBalancerArn"]
                    )["Listeners"]

                    for listener in listeners:
                        rules = elbv2.describe_rules(
                            ListenerArn=listener["ListenerArn"]
                        )["Rules"]

                        for rule in rules:
                            for action in rule.get("Actions", []):
                                if "TargetGroupArn" in action:
                                    tg_arn = action["TargetGroupArn"]

                                    if tg_arn in tg_map:
                                        lb_node >> tg_map[tg_arn]

                                        health = elbv2.describe_target_health(
                                            TargetGroupArn=tg_arn
                                        )

                                        for target in health["TargetHealthDescriptions"]:
                                            tid = target["Target"]["Id"]
                                            if tid in ec2_nodes:
                                                tg_map[tg_arn] >> ec2_nodes[tid]
                except:
                    pass

            # ======================
            # RDS
            # ======================
            for db in dbs:
                for subnet in db["DBSubnetGroup"]["Subnets"]:
                    sid = subnet["SubnetIdentifier"]
                    if sid in subnet_map:
                        subnet_map[sid] >> RDS(db["DBInstanceIdentifier"])

            # ======================
            # VPC ENDPOINTS
            # ======================
            for ep in endpoints:
                for sid in ep.get("SubnetIds", []):
                    if sid in subnet_map:
                        subnet_map[sid] >> Endpoint(
                            ep["ServiceName"].split(".")[-1]
                        )

    # ======================
    # TRANSIT GATEWAY
    # ======================
    tgw_nodes = {}

    for tgw in tgws:
        tgw_id = tgw["TransitGatewayId"]
        tgw_nodes[tgw_id] = TransitGateway(tgw_id)

    for att in tgw_attachments:
        if att["ResourceType"] == "vpc":
            vpc_id = att["ResourceId"]
            tgw_id = att["TransitGatewayId"]

            if tgw_id in tgw_nodes:
                tgw_node = tgw_nodes[tgw_id]

                for vpc in vpcs:
                    if vpc["VpcId"] == vpc_id:
                        VPC(vpc["CidrBlock"]) >> tgw_node