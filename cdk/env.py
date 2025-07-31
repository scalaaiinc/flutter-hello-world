ENVIRONMENTS = {
    "playground": {
        "vpcId": "vpc-09a336bc51ebc097e",
        "subnetIds": [
            "subnet-0933b0bb314dcdc60",
            "subnet-07e07050f56ac0920",
            "subnet-09069cfc18f7c22fe",
        ],
        "domain": "playground.scala.ai",
        "subDomainName": "flutter-hello-world",
        "cpu": 256,
        "memory": 1024,
        "AutoScaleMinCapacity": 1,
        "AutoScaleMaxCapacity": 3,
    },
    "preview": {
        "vpcId": "",
        "subnetIds": [],
        "domain": "preview.scala.technology",
        "subDomainName": "flutter-hello-world",
        "cpu": 512,
        "memory": 1024,
        "AutoScaleMinCapacity": 1,
        "AutoScaleMaxCapacity": 3,
    },
    "live": {
        "vpcId": "",
        "subnetIds": [],
        "domain": "scala.ai",
        "subDomainName": "flutter-hello-world",
        "cpu": 1024,
        "memory": 2048,
        "AutoScaleMinCapacity": 2,
        "AutoScaleMaxCapacity": 5,
    },
}


def get_env():
    return ENVIRONMENTS 
