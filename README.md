# Task 13: Deploying Deep Learning Applications on Kubernetes

## Overview

This project demonstrates the deployment and external exposure of a containerized deep learning application in a Kubernetes environment.

The application consists of a **Flask-based Deep Learning API** for CIFAR-10 image classification and a **Streamlit frontend** for user interaction. Kubernetes Deployment and Service manifests are used to manage, deploy, and expose these application components.

The project also demonstrates replica scaling, resource configuration, and RollingUpdate deployment strategy.

---

## Objective

To deploy and expose containerized deep learning applications in a Kubernetes environment and verify their accessibility and functionality.

---

## Technologies Used

* Python
* TensorFlow / Keras
* Flask
* Streamlit
* Docker
* Kubernetes
* Minikube
* kubectl
* PowerShell
* CIFAR-10 Dataset

---

## Application Architecture

The application consists of two main components:

### 1. Flask API

The Flask backend loads the trained CIFAR-10 deep learning model and provides an API endpoint for image prediction.

**Port:** `5000`

### 2. Streamlit Frontend

The Streamlit application provides a graphical interface where users can upload CIFAR-10 images and view prediction results.

**Port:** `8501`

### Kubernetes Services

* Flask API → `ClusterIP`
* Streamlit → `NodePort`

The Flask API is used for internal communication within the Kubernetes cluster, while the Streamlit service is exposed externally for browser access.

---

## Project Structure

```text
Task13_Kubernetes_Deployment/
│
├── model/
│   └── cifar10_cnn.keras
│
├── pages/
│   └── 1_Image_Prediction.py
│
├── screenshots/
│
├── app.py
├── flask_api.py
├── Dockerfile.flask
├── Dockerfile.streamlit
├── docker-compose.yml
├── flask-deployment.yaml
├── flask-service.yaml
├── streamlit-deployment.yaml
├── streamlit-service.yaml
├── requirements.txt
├── .dockerignore
├── frog.png
├── truck.png
└── README.md
```

---

## Kubernetes Deployment Configuration

Two Kubernetes Deployment manifests are used:

* `flask-deployment.yaml`
* `streamlit-deployment.yaml`

Each application is configured with **2 replicas** to demonstrate workload scaling.

The deployments also use the **RollingUpdate** strategy.

---

## Resource Configuration

CPU and memory requests and limits are configured for the application containers.

### Requests

```text
CPU: 250m
Memory: 512Mi
```

### Limits

```text
CPU: 500m
Memory: 1Gi
```

This configuration demonstrates Kubernetes resource management for deployed workloads.

---

## Kubernetes Services

### Flask API Service

```text
Service Name: flask-api-service
Type: ClusterIP
Port: 5000
Target Port: 5000
```

The Flask API uses a ClusterIP service for internal communication within the Kubernetes cluster.

### Streamlit Service

```text
Service Name: streamlit-service
Type: NodePort
Port: 8501
Target Port: 8501
```

The Streamlit application uses a NodePort service to allow external browser access.

---

## Deployment Commands

Start the Minikube Kubernetes cluster:

```powershell
minikube start --driver=docker
```

Verify the cluster:

```powershell
minikube status
```

Check Kubernetes nodes:

```powershell
kubectl get nodes
```

Apply the Flask deployment:

```powershell
kubectl apply -f flask-deployment.yaml
```

Apply the Streamlit deployment:

```powershell
kubectl apply -f streamlit-deployment.yaml
```

Apply the Flask service:

```powershell
kubectl apply -f flask-service.yaml
```

Apply the Streamlit service:

```powershell
kubectl apply -f streamlit-service.yaml
```

---

## Deployment Verification

Check deployments:

```powershell
kubectl get deployments
```

Check running pods:

```powershell
kubectl get pods
```

Check services:

```powershell
kubectl get services
```

Check rollout status:

```powershell
kubectl rollout status deployment/flask-api
kubectl rollout status deployment/streamlit
```

---

## Replica Scaling

The deployments are configured with two replicas.

The replica status can be verified using:

```powershell
kubectl get deployments
```

The running application pods can be verified using:

```powershell
kubectl get pods
```

This demonstrates that multiple instances of the application workloads can run within the Kubernetes environment.

---

## External Application Access

The Streamlit application can be exposed using Minikube:

```powershell
minikube service streamlit-service --url
```

The generated URL can be opened in a web browser to access the Streamlit application.

---

## Flask API Testing

The Flask API health endpoint can be tested using:

```powershell
curl.exe http://127.0.0.1:5000/
```

A successful response confirms that the Flask prediction API is running.

---

## Application Testing

The deployed Streamlit application was tested using sample CIFAR-10 images.

Test images include:

* `frog.png`
* `truck.png`

The application successfully processed the uploaded images and displayed the corresponding prediction results and confidence values.

---

## Results

The Kubernetes deployment was successfully completed.

The following results were verified:

* Flask API deployed successfully.
* Streamlit application deployed successfully.
* Multiple replicas were created for the workloads.
* Kubernetes Services were successfully configured.
* Flask API accessibility was verified.
* Streamlit application was externally accessible.
* RollingUpdate deployment completed successfully.
* CPU and memory resource configurations were applied.
* CIFAR-10 image prediction was successfully tested.

---

## Observations

The Kubernetes environment successfully managed the Flask API and Streamlit application as separate workloads.

The use of separate Services allowed internal Flask API communication and external Streamlit access.

Replica configuration demonstrated the ability to run multiple instances of application components, while resource requests and limits provided controlled resource allocation.

The RollingUpdate strategy allowed the deployment configuration to be updated without manually recreating the complete application environment.

---

## Conclusion

This task successfully demonstrated the deployment and exposure of a containerized deep learning application using Kubernetes.

Kubernetes Deployment manifests were created and configured for the Flask API and Streamlit frontend. Services were configured to provide internal and external connectivity. The deployment was further enhanced using multiple replicas, resource requests and limits, and a RollingUpdate strategy.

The successful deployment, service accessibility, application testing, and Kubernetes verification confirm that the deep learning application was successfully deployed in a Kubernetes environment.

---

