# Docker commands:

### Basic Commands
1. `docker --version`: Get the installed Docker version.
2. `docker info`: Display system-wide information about Docker and its components.
   
### Working with Images
3. `docker pull [image]`: Download an image from a registry (like Docker Hub).
4. `docker build -t [name] .`: Build an image from a Dockerfile, tagging it with a name.
5. `docker images`: List all available images on the local machine.
6. `docker rmi [image]`: Remove a Docker image.

### Managing Containers
7. `docker run [image]`: Create and start a container from an image.
8. `docker ps`: Show running containers.
9. `docker ps -a`: Show all containers (running and stopped).
10. `docker stop [container_id]`: Gracefully stop a running container.
11. `docker start [container_id]`: Start a stopped container.
12. `docker restart [container_id]`: Restart a container.
13. `docker rm [container_id]`: Remove a stopped container.

### Interactive Mode and Logging
14. `docker run -it [image]`: Run a container in interactive mode (typically with a shell).
15. `docker logs [container_id]`: View the logs of a running container.
   
### Docker Compose
16. `docker-compose up`: Build and start containers defined in `docker-compose.yml`.
17. `docker-compose down`: Stop and remove resources defined in `docker-compose.yml`.
   
### Networking and Port Mapping
18. `docker run -p [host_port]:[container_port] [image]`: Map a host port to a container port.
19. `docker network ls`: List all Docker networks.

### Data and Volumes
20. `docker volume create [volume_name]`: Create a new volume.
21. `docker volume ls`: List all volumes.
22. `docker volume rm [volume_name]`: Remove a volume.

### Dockerfile and Docker Compose File
- A `Dockerfile` provides a set of instructions for building a Docker image.
- A `docker-compose.yml` file allows you to define and run multi-container Docker applications.

### Miscellaneous
23. `docker exec -it [container_id] [command]`: Execute a command inside a running container.
24. `docker search [term]`: Search the Docker Hub for images.
25. `docker login`: Log in to the Docker Hub registry.
26. `docker push [image]`: Push an image to a registry.
