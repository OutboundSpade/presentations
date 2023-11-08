# UUG notes

## Docker commands reference

### Pull a container from docker hub
```bash
docker pull <name>
```

### List images
```bash
docker images
```

### Create and run a container

```bash
docker run -d -p 80:80 --name web nginx
```

### List running containers
```bash
docker ps
```

### List all containers
```bash
docker ps -a
```

### Remove a container
```bash
docker rm web
```

### Create a network
```bash
docker network create <name>
```

### List networks
```bash
docker network ls <name>
```

### Remove networks
```bash
docker network rm <name>
```

