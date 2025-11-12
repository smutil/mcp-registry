# mcp-registry# MCP Registry

A Flask-based application that serves the Model Context Protocol (MCP) server registry. The application provides a web interface and API endpoints to browse and access MCP server configurations.

## Project Structure

```
mcp-registry/
├── src/
│   └── app.py              # Main Flask application
├── templates/
│   ├── index.html          # Home page template
│   └── detail.html         # Server detail page template
├── v0/
│   └── servers.json        # MCP server registry data
├── Dockerfile              # Docker configuration
├── requirements.txt        # Python project dependencies
├── Makefile                # Build and run automation
└── README.md               # This file
```

## Requirements

- Python 3.9+
- Flask 2.3.3
- Gunicorn 22.0.0

## Running Locally (Without Docker)

### 1. Set up a Python virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
python -m flask --app src.app run --host 0.0.0.0 --port 8080
```

Or using Gunicorn (production):

```bash
gunicorn -w 2 -b 0.0.0.0:8080 src.app:app
```

### 4. Access the application

Open your browser and navigate to:
- **Home page**: http://localhost:8080/
- **Server details**: http://localhost:8080/server/<id>
- **API endpoints**:
  - http://localhost:8080/v0/servers
  - http://localhost:8080/v0.1/servers
  - http://localhost:8080/registry
- **Health check**: http://localhost:8080/health

## Running with Docker

### Using Make (Recommended)

```bash
# Build the Docker image
make build

# Run the Docker container
make run

# Stop the container
make stop

# Clean up (remove image and container)
make clean

# Rebuild everything from scratch
make rebuild

# View logs
make logs

# Show all available commands
make help
```

### Manual Docker Commands

If you prefer not to use Make:

```bash
# Build
docker build -t mcp-registry:latest .

# Run
docker run -d -p 8080:8080 --name mcp-registry mcp-registry:latest

# View logs
docker logs mcp-registry

# Stop
docker stop mcp-registry

# Remove
docker rm mcp-registry
```

## API Endpoints

- **GET /**: Home page with list of all servers
- **GET /server/<id>**: Detailed view of a specific server
- **GET /v0/servers**: JSON API endpoint for server registry (v0)
- **GET /v0.1/servers**: JSON API endpoint for server registry (v0.1)
- **GET /registry**: JSON API endpoint for server registry
- **GET /health**: Health check endpoint

### Access the Application

Once running, the application will be available at http://localhost:8080/

## Configuration

The application loads server configurations from `v0/servers.json`. This file contains all MCP server definitions served by the registry.

## Development

For development, you can use Flask's development server:

```bash
export FLASK_APP=src.app
export FLASK_ENV=development
flask run --host 0.0.0.0 --port 8080
```

## License

See LICENSE file for details.