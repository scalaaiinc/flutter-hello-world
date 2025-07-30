import os

ENVIRONMENTS = {
    "playground": {
        "vpcId": os.environ.get("PLAYGROUND_VPC_ID", "vpc-12345678"),
        "subnetIds": os.environ.get("PLAYGROUND_SUBNET_IDS", "subnet-12345678,subnet-87654321").split(","),
        "domain": os.environ.get("PLAYGROUND_DOMAIN", "playground.example.com"),
        "cpu": 256,
        "memory": 512,
        "AutoScaleMinCapacity": 1,
        "AutoScaleMaxCapacity": 2,
    },
    "preview": {
        "vpcId": os.environ.get("PREVIEW_VPC_ID", "vpc-12345678"),
        "subnetIds": os.environ.get("PREVIEW_SUBNET_IDS", "subnet-12345678,subnet-87654321").split(","),
        "domain": os.environ.get("PREVIEW_DOMAIN", "preview.example.com"),
        "cpu": 512,
        "memory": 1024,
        "AutoScaleMinCapacity": 1,
        "AutoScaleMaxCapacity": 3,
    },
    "live": {
        "vpcId": os.environ.get("LIVE_VPC_ID", "vpc-12345678"),
        "subnetIds": os.environ.get("LIVE_SUBNET_IDS", "subnet-12345678,subnet-87654321").split(","),
        "domain": os.environ.get("LIVE_DOMAIN", "live.example.com"),
        "cpu": 1024,
        "memory": 2048,
        "AutoScaleMinCapacity": 2,
        "AutoScaleMaxCapacity": 5,
    },
}


def get_env():
    return ENVIRONMENTS 