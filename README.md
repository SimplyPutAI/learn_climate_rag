# learn_climate_chatboot

## Installation

This application's scaffolding was created using langchaing-cli with the rag-weaviate template:

```bash
langchain app new my-app --package rag-weaviate
```

Check the default [README](docs/SCAFFOLDING.md) for more context.

You don't need to recreate the steps described in the original README. Instead clone this repository and use [docker-compose](https://smallsharpsoftwaretools.com/tutorials/use-colima-to-run-docker-containers-on-macos/) for local development.

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

### Running a Jupyter Notebook

For running a local Jupyter Notebook, please execute from a new terminal session the following command:

```
docker compose up jupyter
```

This will provide a URL (at the end of the logs) in which you can find the notebook running. The URL usually is `http://127.0.0.1:8888/lab`. If you need to start your notebook with a specific dependency already installed, add the dependency in `notebooks/requirements.txt` before running the docker compose command.

### Running the API

In order to run the web service you can execute:

```
docker compose up web -d
```

and go to the playground in `http://127.0.0.1:8000/rag-weaviate/playground/`. Also, the API specs are found in `http://127.0.0.1:8000/docs`.