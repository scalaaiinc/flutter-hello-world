import os

import aws_cdk as cdk
import aws_cdk.aws_ecs as ecs
import aws_cdk.aws_route53 as route53
from aws_cdk.aws_ecr_assets import DockerImageAsset, NetworkMode, Platform
from aws_cdk.aws_logs import RetentionDays
from constructs import Construct
from scala_cdk.ecs import FargateServiceParameters
from scala_cdk.ecs.fargate import FargateServiceHelper, get_code_artifact_repo_url_secrets

from cdk.env import get_env


class FlutterHelloWorld(cdk.Stack):
    def __init__(self, scope: Construct, construct_id: str, stack_env: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self._region = os.environ.get("CDK_DEPLOY_REGION", os.environ["CDK_DEFAULT_REGION"])
        self._account_id = os.environ["CDK_DEFAULT_ACCOUNT"]
        self._stack_name = "flutter-hello-world"
        self._owner_team = "scala"
        
        # Get environment from context
        self._env = get_env()[stack_env]
        self._stack_env = stack_env

        task_environmental_variables = {
            "environmentName": self._stack_env,
            "awsAccountId": self._account_id,
            "awsDefaultRegion": self._region,
        }
        abs_path = os.path.join(os.path.dirname(__file__), "..")

        image = DockerImageAsset(
            self,
            "DockerImage",
            directory=abs_path,
            network_mode=NetworkMode.HOST,
            platform=Platform.LINUX_ARM64,
            build_secrets=get_code_artifact_repo_url_secrets(abs_path, self._region),
        )
        runtime_platform = ecs.RuntimePlatform(
            operating_system_family=ecs.OperatingSystemFamily.LINUX,
            cpu_architecture=ecs.CpuArchitecture.ARM64,
        )

        fargate_parameters = FargateServiceParameters(
            auto_scale_task_count_max_capacity=self._env["AutoScaleMaxCapacity"],
            task_log_group_name="/aws/fargate/" + self._stack_name,
            docker_image_asset=image,
            vpc_id=self._env["vpcId"],
            subnet_ids=self._env["subnetIds"],
            auto_scale_task_count_min_capacity=self._env["AutoScaleMinCapacity"],
            cpu=self._env["cpu"],
            memory_limit_mib=self._env["memory"],
            runtime_platform=runtime_platform,
            task_log_group_retention_policy=RetentionDays.ONE_DAY,
        )

        domain = self._env["domain"]
        hosted_zone = route53.HostedZone.from_lookup(
            self,
            "HostedZone",
            domain_name='.'.join(domain.split(".")[1:]),
        )

        fargate_service_helper = FargateServiceHelper(
            self,
            self._stack_name,
            task_environmental_variables,
            fargate_parameters,
            domain=domain,
            domain_zone=hosted_zone,
        ) 
