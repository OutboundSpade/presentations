---
marp: true
theme: default
paginate: true
footer: "Docker for Web Developers (C) 2023, Ray Steen"
---
<!-- class: invert -->

# Docker for Web Developers
Building and deploying web applications using containers

![bg width:300px right](assets/vertical-logo-monochromatic.webp)

---
## Downloading the web application

```bash
git clone https://github.com/OutboundSpade/nuxt-demo.git
```

---
## Analyzing the Dockerfile

```dockerfile
FROM node:18

WORKDIR /data

COPY package.json .

RUN yarn install

COPY . .

RUN yarn build

ENV MONGO_URI=mongodb://mongodb

CMD node .output/server/index.mjs
```

---
## Building the container (optional)


```bash
docker build -t <username>/nuxt-demo .
```

---
## Pushing the container to Docker Hub (optional)

```bash
docker login
```
```bash
docker push <username>/nuxt-demo
```
---
# Basic Docker Deployment
## Creating the network

```bash
docker network create web
```

## Deploying the database

```bash
docker run -d --name mongodb --network web mongo
```

---

## Deploying the web application

```bash
docker run -d --name website --network web -p 80:3000 outboundspade48/nuxt-demo
```

---
## Cleaning up

```bash
docker kill website mongodb
```
```bash
docker rm website mongodb
```
```bash
docker network rm web
```
---
# Docker Swarm Deployment

## Starting the Visualizer (optional)

```bash
docker run -d -p 8080:8080 -v /var/run/docker.sock:/var/run/docker.sock dockersamples/visualizer
```

## Initializing the swarm

```bash
docker swarm init --advertise-addr 192.168.0.XX
```
---
## Joining the worker nodes

```bash
docker swarm join --token XXXXXX-X-X... 192.168.0.XX:XXXX
```
### Optional: Prevent manager from running workloads

```bash
docker node update --availability drain node1
```
---
## Creating the network

```bash
docker network create -d overlay db-internal
```

## Deploying the database

```bash
docker service create --replicas 1 --name mongodb --network db-internal mongo
```
---
## Deploying the web application

```bash
docker service create --replicas 3 --name website \
--network db-internal -p 80:3000 outboundspade48/nuxt-demo
```
---
## Scaling the web application

```bash
docker service scale website=5
```
---
## Deploying a new version

```bash
docker service update --image outboundspade48/nuxt-demo:v1.1 website
```
---
# Resources

- [Get Started with Docker](https://www.docker.com/get-started)
- [Get Docker](https://docs.docker.com/get-docker/)
- [Docker playground](https://labs.play-with-docker.com/)
- [Use the Docker command line](https://docs.docker.com/engine/reference/commandline/cli/)

## Container Images used
- [mongo](https://hub.docker.com/_/mongo)
- [node](https://hub.docker.com/_/node)
- [outboundspade48/nuxt-demo](https://hub.docker.com/r/outboundspade48/nuxt-demo)