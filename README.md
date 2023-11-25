# learn_climate_chatboot

## Installation

This application's scaffolding was created using langchaing-cli with the rag-weaviate template:

```bash
langchain app new my-app --package rag-weaviate
```
Check the default [README](docs/SCAFFOLDING.md) for more context.

You don't need to recreate the steps described in the original README. Instead clone this repository and use docker-compose for local development.

### Running the vector DB

You can execute a single local instance of weaviate database by running:

```
docker compose up weaviate -d
```
Check for the status of the weaviate service with:

```
docker ps -a | grep weaviate
```

The local weaviate service will expose an endpoint in `http://localhost:8080`, so mind the host URL config for instantiating the client:

```
mport weaviate
import json

client = weaviate.Client(
    url = "http://localhost:8080",  # Replace with your endpoint
    additional_headers = {
        "X-OpenAI-Api-Key": "YOUR-OPENAI-API-KEY"  # Replace with your inference API key
    }
)
```
Check this [section](https://weaviate.io/developers/weaviate/quickstart#can-i-use-another-deployment-method) for more configs.