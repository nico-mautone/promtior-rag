# Promtior RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot for Promtior that answers questions using company documentation and website content.

## Prerequisites

- Python 3.9+
- Docker (for containerized deployment)
- AWS Copilot CLI (for AWS deployment)
- OpenAI API key

## Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/promtior-rag.git
cd promtior-rag
```

### 2. Set up a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your_openai_api_key_here
```

### 5. Run the ingestion process

This step processes the documents and creates the vector store:

```bash
python -m ingest.run_ingest
```

### 6. Start the API server

```bash
uvicorn api.server:app --host 0.0.0.0 --port 8000
```

The API will be available at http://localhost:8000

## Docker Deployment

### 1. Build the Docker image

```bash
docker build -t promtior-rag .
```

### 2. Run the container

```bash
docker run -d \
  -p 8000:8000 \
  -v $(pwd)/store:/app/store \
  --env-file .env \
  --name promtior-rag \
  promtior-rag
```

The API will be available at http://localhost:8000

## AWS Deployment with Copilot CLI

### 1. Install AWS Copilot CLI

Follow the [official AWS Copilot installation instructions](https://aws.github.io/copilot-cli/docs/getting-started/install/).

### 2. Initialize and deploy the application

```bash
copilot init
```

During the initialization:
- Choose "App Runner" as the service type
- Use the local Dockerfile
- Set the port to 8000

### 3. Manage your deployment

To see the status of your service:

```bash
copilot svc status
```

To view logs:

```bash
copilot svc logs
```

To update your deployment:

```bash
copilot svc deploy
```

To pause the application:

```bash
copilot svc pause
```

To resume the application:

```bash
copilot svc resume
```

To delete the application:

```bash
copilot svc delete
```

### Notes

The application is currently paused (due to the potential cost of running the service), but once resumed, it will be accessible at the following URL provided by Copilot.
https://pvqdn8263x.eu-west-1.awsapprunner.com/