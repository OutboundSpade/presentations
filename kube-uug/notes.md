# UUG notes

## Key Terms

### Nodes
These are the physical or virtual machines that run containerized applications. Each node in a Kubernetes cluster runs a container runtime (like Docker) and the necessary services to communicate with the master and other nodes.

### Control Plane
Manages the state of the cluster, including scheduling applications, scaling applications, and rolling out updates.

### Pods
The basic building block in Kubernetes. A pod is the smallest deployable unit and represents a single instance of a running process in a cluster.

### Services
An abstraction that defines a set of pods and a policy to access them. Services enable a loose coupling between dependent parts of an application. A Service routes traffic across a set of Pods. Services are the abstraction that allows pods to die and replicate in Kubernetes without impacting your application.

### ReplicaSets
A higher-level abstraction over pods that ensures a specified number of pod replicas are running at any given time. It is often used for scaling applications.

### Deployments
A higher-level abstraction over ReplicaSets that provides declarative updates to applications. Deployments allow you to describe how applications should be deployed and updated over time.


## Demo commands

[Deploy an app](https://kubernetes.io/docs/tutorials/kubernetes-basics/deploy-app/deploy-intro/)

```bash
kubectl create deployment kubernetes-bootcamp --image=gcr.io/google-samples/kubernetes-bootcamp:v1
```

```bash
kubectl get deployments
```

```bash
kubectl expose deployment/kubernetes-bootcamp --type="NodePort" --port 8080
```

```bash
kubectl get svc
```

### scaling

```bash
kubectl scale deployments/kubernetes-bootcamp --replicas=4
```

```bash
kubectl get pods -o wide
```

