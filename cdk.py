#!/usr/bin/env python3
import os
import aws_cdk as cdk
from cdk.stack import FlutterHelloWorld

app = cdk.App()
environment_name = app.node.try_get_context("environment_name") or 'playground'
FlutterHelloWorld(
    app,
    "FlutterHelloWorld",
    stack_env=environment_name,
    env=cdk.Environment(
        account=os.getenv("CDK_DEFAULT_ACCOUNT"), region=os.getenv("CDK_DEFAULT_REGION")
    ),
)
app.synth() 
