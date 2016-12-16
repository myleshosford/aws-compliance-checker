#
# @title: AWS Compliance Checker
# @escription: Query AWS Config for non-compliant resources and feed this into ITSM workflow
# @author Myles Hosford
#


from __future__ import print_function
import json
from datetime import datetime
import boto3

# metadata
VERSION = "0.1"

# AWS clients
config_client = boto3.client('config')


def get_checks():
    print("[+] Starting compliance check...\n")
    response = config_client.describe_config_rules()
    for n in response['ConfigRules']:
        print(n['ConfigRuleName'])

    print("\nGetting compliance status")
    response = config_client.get_compliance_details_by_config_rule(ConfigRuleName='ResourcesMustBeTagged')



get_checks()