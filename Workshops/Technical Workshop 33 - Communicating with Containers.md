___
### Prework

 _1. What are 'volumes' in Docker?

**Volumes** in Docker are a way to store data generated and used by Docker containers.

_2. What are the benefits of using 'Docker Compose'?_

**Docker Compose** is a tool for defining and running multi-container Docker applications. It simplifies the management of multiple containers.

_3. How does inter-container communication work using Docker Compose?_

When using Docker Compose, inter-container communication is handled automatically through a network that Compose sets up.

By default, all containers defined in a `docker-compose.yml` file are connected to the same network. This allows them to communicate with each other. Containers can refer to each other by the service name defined in the `docker-compose.yml` file.
