# JSON Generator API

This Flask application generates random JSON data based on user-specified properties using OpenAI's GPT-3 model.

## Setup and Installation

### Prerequisites

- Python 3.8+
- Docker (optional, for containerized deployment)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/shishir1337/jsongen.git
    cd jsongen
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Set your OpenAI API key in the application:

    ```python
    openai.api_key = "your-openai-api-key"
    ```

### Running the Application

#### Locally

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. The application will be accessible at `http://127.0.0.1:5000`.

#### Using Docker

1. Build the Docker image:

    ```bash
    docker build -t jsongen:latest .
    ```

2. Run the Docker container:

    ```bash
    docker-compose -f black4app.yml up
    ```

3. The application will be accessible at `http://127.0.0.1:5000`.

## Usage

Send a POST request to the `/generate-json` endpoint with the following JSON payload:

```json
{
    "user_input": "property1, property2, property3",
    "num_objects": 5
}
```

### Example Request

```bash
curl -X POST http://127.0.0.1:5000/generate-json -H "Content-Type: application/json" -d '{
    "user_input": "name, age, city",
    "num_objects": 3
}'
```

### Example Response

```json
[
    {
        "name": "John Doe",
        "age": "25",
        "city": "New York"
    },
    {
        "name": "Jane Smith",
        "age": "30",
        "city": "Los Angeles"
    },
    {
        "name": "Alice Johnson",
        "age": "28",
        "city": "Chicago"
    }
]
```

## Files

- `app.py`: The main Flask application file.
- `black4app.yml`: Docker Compose configuration file.
- `Dockerfile`: Dockerfile for building the container image.
- `requirements.txt`: List of required Python packages.

## License

This project is licensed under the GPL-2.0-or-later License. See the [LICENSE](https://www.gnu.org/licenses/gpl-2.0.html) file for details.

---

Make sure to replace `your-openai-api-key` with your actual OpenAI API key.
