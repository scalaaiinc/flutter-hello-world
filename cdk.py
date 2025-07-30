#!/usr/bin/env python3
import aws_cdk as cdk
from cdk.stack import FlutterHelloWorld

app = cdk.App()
FlutterHelloWorld(app, "FlutterHelloWorld")
app.synth() 