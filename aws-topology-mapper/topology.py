import boto3
from diagrams import Diagram, Cluster
from diagrams.aws.network import VPC, PublicSubnet, PrivateSubnet, InternetGateway, NATGateway, RouteTable

region = "ca-central-1"
ec2 = boto3.client("ec2", region_name=region)

vpcs = ec2.describe_vpcs()["Vpcs"]
subnets = ec2.describe_subnets()["Subnets"]
igws = ec2.describe_internet_gateways()["InternetGateways"]
natgws = ec2.describe_nat_gateways()["NatGateways"]
rts = ec2.describe_route_tables()["RouteTables"]

with Diagram("AWS VPC Network Topology", show=False):

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

            subnet_nodes = {}
            private_subnets = []

            # Subnets + détection public/privé
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

                if is_public:
                    sn = PublicSubnet(cidr)
                else:
                    sn = PrivateSubnet(cidr)
                    private_subnets.append((sn, used_rt))

                vpc_node >> sn
                subnet_nodes[subnet["SubnetId"]] = sn

            # NAT + liaison réelle aux subnets privés
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
