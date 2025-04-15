import boto3
import pandas as pd
import json
from datetime import datetime

RISKY_PORTS = [22, 3389, 3306, 5432, 6379, 9200]
findings = []

def get_all_regions():
    ec2 = boto3.client('ec2')
    regions = ec2.describe_regions()
    return [region['RegionName'] for region in regions['Regions']]

def detect_exposed_ports(region):
    ec2 = boto3.client('ec2', region_name=region)
    try:
        response = ec2.describe_security_groups()
    except Exception as e:
        print(f"❌ Failed in region {region}: {e}")
        return

    for sg in response['SecurityGroups']:
        sg_id = sg.get('GroupId')
        sg_name = sg.get('GroupName')
        vpc_id = sg.get('VpcId', 'N/A')

        for rule in sg.get('IpPermissions', []):
            protocol = rule.get('IpProtocol', 'ALL')
            from_port = rule.get('FromPort')

            for ip in rule.get('IpRanges', []):
                cidr = ip.get('CidrIp', '')
                if cidr == '0.0.0.0/0':
                    if from_port in RISKY_PORTS or from_port is None:
                        findings.append({
                            'Region': region,
                            'SecurityGroup': sg_name,
                            'SG_ID': sg_id,
                            'Port': from_port or 'ALL',
                            'Protocol': protocol,
                            'CIDR': cidr,
                            'VPC': vpc_id
                        })

            for ip in rule.get('Ipv6Ranges', []):
                cidr6 = ip.get('CidrIpv6', '')
                if cidr6 == '::/0':
                    if from_port in RISKY_PORTS or from_port is None:
                        findings.append({
                            'Region': region,
                            'SecurityGroup': sg_name,
                            'SG_ID': sg_id,
                            'Port': from_port or 'ALL',
                            'Protocol': protocol,
                            'CIDR': cidr6,
                            'VPC': vpc_id
                        })

def export_results():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    if not findings:
        print("✅ No public risky ports found.")
        return

    df = pd.DataFrame(findings)
    df.to_csv(f"exposed_ports_{timestamp}.csv", index=False)
    with open(f"exposed_ports_{timestamp}.json", "w") as f:
        json.dump(findings, f, indent=2)

    print(f"✅ Exported results to exposed_ports_{timestamp}.csv and .json")

if __name__ == "__main__":
    print("🚀 Starting multi-region security group audit...\n")
    regions = get_all_regions()
    for region in regions:
        detect_exposed_ports(region)
    export_results()
