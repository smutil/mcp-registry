.PHONY: build run stop clean help

IMAGE_NAME := mcp-registry
CONTAINER_NAME := mcp-registry-container
PORT := 8080

help:
	@echo "Available targets:"
	@echo "  make build       - Build the Docker image"
	@echo "  make run         - Run the Docker container"
	@echo "  make stop        - Stop the running container"
	@echo "  make clean       - Remove the Docker image and container"
	@echo "  make rebuild     - Clean, build, and run"
	@echo "  make logs        - Show container logs"

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run -d -p $(PORT):8080 --name $(CONTAINER_NAME) $(IMAGE_NAME)
	@echo "Container running at http://localhost:$(PORT)"

stop:
	docker stop $(CONTAINER_NAME) || true
	docker rm $(CONTAINER_NAME) || true

clean: stop
	docker rmi $(IMAGE_NAME) || true

rebuild: clean build run

logs:
	docker logs -f $(CONTAINER_NAME)
