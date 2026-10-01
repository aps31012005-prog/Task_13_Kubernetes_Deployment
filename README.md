# Task 12: Kubernetes Cluster Setup and Deployment

## Kubernetes Orchestration of a Containerized Deep Learning Application

---

## 1. Introduction

This project demonstrates the setup and deployment of a containerized deep learning application using Kubernetes. The application consists of a Flask REST API backend and a Streamlit frontend for CIFAR-10 image classification.

The application was previously containerized using Docker. In this task, Kubernetes is used to orchestrate the application components, manage containers through Deployments and Services, and provide communication between the frontend and backend.

The local Kubernetes cluster was created using Minikube with Docker as the container runtime.

---

## 2. Objective

The main objectives of this task are:

* To understand the fundamentals of Kubernetes orchestration.
* To set up a local Kubernetes cluster using Minikube.
* To deploy containerized applications using Kubernetes Deployments.
* To expose applications using Kubernetes Services.
* To verify Pod and Service operations.
* To establish communication between Streamlit and Flask components.
* To monitor the status of Kubernetes resources.
* To test the deployed deep learning prediction application.

---

## 3. Technologies Used

The following technologies and tools were used:

* Kubernetes
* Minikube
* kubectl
* Docker Desktop
* Docker
* Python
* Flask
* Streamlit
* TensorFlow
* NumPy
* Pillow
* CIFAR-10 CNN Model
* YAML configuration files
* Windows PowerShell
* Visual Studio Code

---

## 4. Application Architecture

The application contains two major components:

### Flask Backend

The Flask application provides a REST API for CIFAR-10 image prediction.

The API:

* Loads the trained CNN model.
* Receives an image through the `/predict` endpoint.
* Performs image preprocessing.
* Generates the prediction.
* Returns the predicted class and confidence.

### Streamlit Frontend

The Streamlit application provides a graphical user interface.

The frontend:

* Allows the user to upload an image.
* Communicates with the Flask REST API.
* Sends the uploaded image to the backend.
* Displays the predicted class.
* Displays the prediction confidence.

### Kubernetes Architecture

The Kubernetes deployment consists of:

```text
                    Kubernetes Cluster
                           |
             +-------------+-------------+
             |                           |
      Streamlit Pod                 Flask Pod
             |                           |
      Streamlit Service          Flask API Service
       (NodePort)                    (ClusterIP)
             |                           |
             +---------- API ------------+
                           |
                     CNN Model
                           |
                     CIFAR-10
```

---

## 5. Project Structure

```text
Task12_Kubernetes/
│
├── model/
│   └── cifar10_cnn.keras
│
├── pages/
│   └── 1_Image_Prediction.py
│
├── screenshots/
│   ├── 01_minikube_cluster_verification.png
│   ├── 02_minikube_docker_images.png
│   ├── 03_flask_pod_running.png
│   ├── 04_kubernetes_pods_running.png
│   ├── 05_kubernetes_services.png
│   ├── 06_kubernetes_streamlit_application.png
│   ├── 07_kubernetes_flask_api_health.png
│   ├── 08_kubernetes_frog_prediction.png
│   ├── 09_kubernetes_truck_prediction.png
│   ├── 10_kubernetes_deployments.png
│   ├── 11_kubernetes_cluster_resources.png
│   ├── 12_streamlit_flask_api_connected.png
│   ├── 13_kubernetes_streamlit_frog_prediction.png
│   └── 14_final_kubernetes_verification.png
│
├── app.py
├── flask_api.py
├── frog.png
├── truck.png
├── Dockerfile.flask
├── Dockerfile.streamlit
├── docker-compose.yml
├── .dockerignore
├── requirements.txt
├── flask-deployment.yaml
├── flask-service.yaml
├── streamlit-deployment.yaml
└── streamlit-service.yaml
```

---

## 6. Kubernetes Cluster Setup

Minikube was used to create a local Kubernetes cluster.

The cluster was started using the Docker driver:

```powershell
minikube start --driver=docker
```

The cluster status was verified using:

```powershell
minikube status
```

The Kubernetes node was then verified using:

```powershell
kubectl get nodes
```

The node successfully reached the `Ready` state.

---

## 7. Docker Images in Minikube

The Flask and Streamlit Docker images were built directly into the Minikube environment.

Flask image:

```powershell
minikube image build -t task12-flask-api:latest -f Dockerfile.flask .
```

Streamlit image:

```powershell
minikube image build -t task12-streamlit:latest -f Dockerfile.streamlit .
```

The available images were verified using:

```powershell
minikube image ls --format table
```

The following application images were available:

```text
task12-flask-api:latest
task12-streamlit:latest
```

The Kubernetes Deployments use:

```yaml
imagePullPolicy: Never
```

This allows Kubernetes to use the locally available Minikube images instead of attempting to pull them from an external container registry.

---

## 8. Flask Kubernetes Deployment

The Flask backend was deployed using `flask-deployment.yaml`.

The Deployment configuration defines:

* Deployment name: `flask-api`
* Replica count: 1
* Container name: `flask-api`
* Container port: 5000
* Docker image: `task12-flask-api:latest`

The Deployment was created using:

```powershell
kubectl apply -f flask-deployment.yaml
```

The Flask Pod was verified using:

```powershell
kubectl get pods
```

The Pod successfully reached the `Running` state.

---

## 9. Flask Kubernetes Service

A Kubernetes Service was created for the Flask backend using:

```powershell
kubectl apply -f flask-service.yaml
```

The Service is named:

```text
flask-api-service
```

It exposes port:

```text
5000
```

The Service type is:

```text
ClusterIP
```

ClusterIP allows other Pods inside the Kubernetes cluster to communicate with the Flask API.

---

## 10. Streamlit Kubernetes Deployment

The Streamlit frontend was deployed using `streamlit-deployment.yaml`.

The Deployment contains:

* Deployment name: `streamlit`
* Replica count: 1
* Container name: `streamlit`
* Container port: 8501
* Docker image: `task12-streamlit:latest`

The Deployment was created using:

```powershell
kubectl apply -f streamlit-deployment.yaml
```

The Pods were verified using:

```powershell
kubectl get pods
```

The Streamlit Pod successfully reached the `Running` state.

---

## 11. Streamlit Kubernetes Service

A Kubernetes Service was created for the Streamlit frontend using:

```powershell
kubectl apply -f streamlit-service.yaml
```

The Service is named:

```text
streamlit-service
```

It exposes port:

```text
8501
```

The Service type is:

```text
NodePort
```

NodePort allows the Streamlit application to be accessed from the local machine.

The Streamlit service URL was obtained using:

```powershell
minikube service streamlit-service --url
```

---

## 12. Kubernetes Resource Verification

The deployed resources were checked using:

```powershell
kubectl get pods,services,deployments
```

This command was used to verify:

* Running Pods
* Kubernetes Services
* Deployments
* Replica availability

Both Flask and Streamlit components were successfully deployed.

---

## 13. Flask API Health Verification

The Flask Service was temporarily exposed to the local machine using:

```powershell
kubectl port-forward service/flask-api-service 5000:5000
```

The Flask health endpoint was then accessed through:

```text
http://127.0.0.1:5000/
```

The API returned its health/status response, confirming that the Flask backend was running successfully inside Kubernetes.

---

## 14. API Prediction Testing

The Flask prediction endpoint was tested using CIFAR-10 sample images.

### Frog Image

The following command was used:

```powershell
curl.exe -X POST -F "image=@frog.png" http://127.0.0.1:5000/predict
```

The Flask API processed the image and returned a prediction response containing the predicted class and confidence.

### Truck Image

The truck image was also tested:

```powershell
curl.exe -X POST -F "image=@truck.png" http://127.0.0.1:5000/predict
```

The successful responses verified that the CNN model was accessible through the containerized Flask API.

---

## 15. Streamlit and Flask Integration

The Streamlit application communicates with the Flask backend using the Kubernetes Service name.

The API configuration used by the Streamlit application is:

```python
FLASK_API_URL = "http://flask-api-service:5000"
```

The Kubernetes Service name provides internal communication between the Streamlit Pod and Flask Pod.

The Streamlit interface includes a backend connection check that verifies the Flask API status.

A successful connection confirms communication between the two Kubernetes-managed application components.

---

## 16. End-to-End Prediction

An end-to-end prediction was performed through the Streamlit frontend.

The workflow was:

```text
User uploads image
        ↓
Streamlit Frontend
        ↓
flask-api-service
        ↓
Flask REST API
        ↓
CIFAR-10 CNN Model
        ↓
Prediction
        ↓
Flask JSON Response
        ↓
Streamlit Result Display
```

The prediction result and confidence value were displayed directly in the Streamlit interface.

This verified the complete application workflow inside the Kubernetes environment.

---

## 17. Kubernetes Commands Used

Important Kubernetes commands used during implementation include:

```powershell
minikube start --driver=docker
```

```powershell
minikube status
```

```powershell
kubectl get nodes
```

```powershell
minikube image ls --format table
```

```powershell
kubectl apply -f flask-deployment.yaml
```

```powershell
kubectl apply -f flask-service.yaml
```

```powershell
kubectl apply -f streamlit-deployment.yaml
```

```powershell
kubectl apply -f streamlit-service.yaml
```

```powershell
kubectl get pods
```

```powershell
kubectl get services
```

```powershell
kubectl get deployments
```

```powershell
kubectl get pods,services,deployments
```

```powershell
kubectl get all
```

```powershell
kubectl port-forward service/flask-api-service 5000:5000
```

```powershell
minikube service streamlit-service --url
```

```powershell
kubectl rollout restart deployment streamlit
```

```powershell
kubectl rollout status deployment streamlit
```

---

## 18. YAML Configuration Files

The project uses four Kubernetes YAML files:

### flask-deployment.yaml

Defines the Flask backend Deployment and its container configuration.

### flask-service.yaml

Creates an internal ClusterIP Service for Flask API communication.

### streamlit-deployment.yaml

Defines the Streamlit frontend Deployment and its container configuration.

### streamlit-service.yaml

Creates a NodePort Service to provide access to the Streamlit frontend.

Using separate Deployment and Service objects provides a clear separation between application management and network access.

---

## 19. Verification Results

The following operations were successfully verified:

| Operation                              | Result     |
| -------------------------------------- | ---------- |
| Minikube cluster setup                 | Successful |
| Kubernetes node verification           | Ready      |
| Flask Docker image                     | Available  |
| Streamlit Docker image                 | Available  |
| Flask Deployment                       | Running    |
| Streamlit Deployment                   | Running    |
| Flask Service                          | Available  |
| Streamlit Service                      | Available  |
| Flask health check                     | Successful |
| Frog API prediction                    | Successful |
| Truck API prediction                   | Successful |
| Streamlit-Flask connection             | Successful |
| Streamlit prediction                   | Successful |
| Final Kubernetes resource verification | Successful |

---

## 20. Observations

The following observations were made during the implementation:

1. Minikube provides a convenient local Kubernetes environment for development and testing.
2. Kubernetes Deployments manage application Pods and maintain the desired replica count.
3. Kubernetes Services provide stable network endpoints for application communication.
4. The Flask API was exposed internally using a ClusterIP Service.
5. The Streamlit frontend was exposed using a NodePort Service.
6. Kubernetes service names can be used for communication between Pods.
7. The local Docker images were loaded into the Minikube environment.
8. The `imagePullPolicy: Never` setting allowed Kubernetes to use the locally built images.
9. Pod and Deployment status can be monitored using `kubectl`.
10. Port forwarding can be used to test an internal Kubernetes Service from the local machine.
11. The complete Streamlit-to-Flask-to-CNN workflow was successfully tested.
12. Kubernetes provides a structured approach for managing multiple containerized application components.

---

## 21. Conclusion

This task successfully demonstrated the setup and deployment of a containerized deep learning application using Kubernetes and Minikube.

A local Kubernetes cluster was created and verified. The Flask REST API and Streamlit frontend were deployed using Kubernetes Deployments. Kubernetes Services were configured to provide internal backend communication and external frontend access.

The Flask API was tested using health checks and CIFAR-10 image predictions. The Streamlit frontend was also connected to the Flask backend using the Kubernetes Service name. Finally, an end-to-end image prediction workflow was successfully verified.

The implementation provided practical understanding of Kubernetes Pods, Deployments, Services, container images, networking, service discovery, and application monitoring.

---

## 22. Screenshots

The implementation was documented using 14 screenshots covering:

1. Minikube cluster verification
2. Minikube Docker images
3. Flask Pod running
4. Kubernetes Pods running
5. Kubernetes Services
6. Streamlit application
7. Flask API health check
8. Frog prediction through Flask API
9. Truck prediction through Flask API
10. Kubernetes Deployments
11. Kubernetes cluster resources
12. Streamlit-Flask API connection
13. Streamlit frog prediction
14. Final Kubernetes verification

---

## 23. Final Result

The Kubernetes deployment was completed successfully.

The final system consists of:

```text
Kubernetes / Minikube
        │
        ├── Flask Deployment
        │       └── Flask API Pod
        │             └── CIFAR-10 CNN Model
        │
        └── Streamlit Deployment
                └── Streamlit Pod
                        │
                        └── flask-api-service
```

The application successfully demonstrates container orchestration, service-based communication, API integration, and deep learning inference using Kubernetes.
