# Flutter Hello World

A simple Flutter web application deployed to AWS Fargate using CDK infrastructure.

## Overview

This project demonstrates how to:
- Create a Flutter web application
- Deploy it to AWS Fargate using CDK
- Set up automated CI/CD with GitHub Actions
- Use multi-environment deployments (playground, preview, live)

## Project Structure

```
flutter-hello-world/
├── lib/
│   └── main.dart              # Flutter application code
├── web/                       # Flutter web configuration
├── cdk/
│   ├── __init__.py
│   ├── env.py                 # Environment configuration
│   └── stack.py               # CDK stack definition
├── .github/
│   └── workflows/
│       └── main.yml           # GitHub Actions workflow
├── Dockerfile                 # Multi-stage Docker build
├── nginx.conf                 # Nginx configuration
├── cdk.json                   # CDK configuration
├── cdk.py                     # CDK entry point
└── pyproject.toml            # Python project configuration
```

## Local Development

### Prerequisites

- Flutter SDK (3.24.5 or later)
- Dart SDK
- Python 3.11+
- AWS CDK CLI
- Docker

### Running Locally

1. **Install Flutter dependencies:**
   ```bash
   flutter pub get
   ```

2. **Run the Flutter app locally:**
   ```bash
   flutter run -d chrome
   ```

3. **Run Flutter tests:**
   ```bash
   flutter test
   ```

4. **Build for web:**
   ```bash
   flutter build web
   ```

### CDK Development

1. **Install Python dependencies:**
   ```bash
   pip install -e ".[dev]"
   ```

2. **Synthesize CDK stack:**
   ```bash
   cdk synth
   ```

3. **Deploy to playground environment:**
   ```bash
   cdk deploy --context environment_name=playground
   ```

## Deployment

The application uses a multi-stage Docker build process:

1. **Build Stage:** Uses Debian to install Flutter and build the web application
2. **Production Stage:** Uses nginx to serve the built Flutter web app

### Docker Build

```bash
docker build -t flutter-hello-world .
```

### CDK Deployment

The CDK stack creates:
- ECS Fargate service
- Application Load Balancer
- Auto Scaling configuration
- CloudWatch logs
- Route53 DNS configuration (if domain is provided)

## CI/CD Pipeline

The project uses GitHub Actions for automated deployment:

### Environments

- **Playground:** Deployed on pushes to `feature/*` branches
- **Preview:** Deployed on pushes to `main` branch
- **Live:** Deployed on release creation

### Workflow Steps

1. **Test Job:**
   - Set up Flutter environment
   - Run `flutter pub get`
   - Run `flutter analyze`
   - Run `flutter test`
   - Build Flutter web app

2. **Deploy Jobs:**
   - Set up Python and AWS CDK
   - Configure AWS credentials
   - Deploy CDK stack to target environment

## Configuration

### Environment Variables

The following environment variables can be configured:

- `PLAYGROUND_VPC_ID` / `PREVIEW_VPC_ID` / `LIVE_VPC_ID`: VPC ID for each environment
- `PLAYGROUND_SUBNET_IDS` / `PREVIEW_SUBNET_IDS` / `LIVE_SUBNET_IDS`: Subnet IDs (comma-separated)
- `PLAYGROUND_DOMAIN` / `PREVIEW_DOMAIN` / `LIVE_DOMAIN`: Domain names for each environment

### AWS Secrets

The following GitHub secrets are required:

- `CODEARTIFACT_DOMAIN`: AWS CodeArtifact domain
- `CODEARTIFACT_REPOSITORY`: AWS CodeArtifact repository
- `LIVE_CICD_AWS_KEY` / `LIVE_CICD_AWS_SECRET`: AWS credentials for CodeArtifact access
- `PLAYGROUND_CICD_AWS_KEY` / `PLAYGROUND_CICD_AWS_SECRET`: AWS credentials for playground environment
- `PREVIEW_CICD_AWS_KEY` / `PREVIEW_CICD_AWS_SECRET`: AWS credentials for preview environment
- `LIVE_CICD_AWS_KEY` / `LIVE_CICD_AWS_SECRET`: AWS credentials for live environment

## Architecture

The application is deployed using:

- **AWS Fargate:** Serverless container compute
- **ECS:** Container orchestration
- **Application Load Balancer:** Traffic distribution
- **Auto Scaling:** Automatic scaling based on demand
- **CloudWatch:** Logging and monitoring
- **Route53:** DNS management (optional)

## Contributing

1. Create a feature branch: `git checkout -b feature/your-feature`
2. Make your changes
3. Run tests: `flutter test`
4. Commit your changes: `git commit -m "Add your feature"`
5. Push to the branch: `git push origin feature/your-feature`
6. Create a Pull Request

## License

This project is licensed under the MIT License.
