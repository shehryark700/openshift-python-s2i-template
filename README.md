# OpenShift Python S2I Deployment Template

## Overview

This project demonstrates how to deploy a Python application on OpenShift using Source-to-Image (S2I), OpenShift Templates, BuildConfigs, ImageStreams, DeploymentConfigs, Services, and Routes.

The application source code is pulled directly from GitHub and automatically built using the OpenShift Python builder image.

---

## Features

* OpenShift Template
* Source-to-Image (S2I) Build
* GitHub Integration
* ImageStream Management
* DeploymentConfig Deployment
* Service Exposure
* Route Creation
* Python Application Deployment
* Parameterized Template

---

## Architecture

```text
GitHub Repository
        │
        ▼
BuildConfig
        │
        ▼
Python S2I Builder Image
        │
        ▼
ImageStream
        │
        ▼
DeploymentConfig
        │
        ▼
Pod
        │
        ▼
Service
        │
        ▼
Route
        │
        ▼
User
```

---

## Prerequisites

* OpenShift Cluster
* OpenShift CLI (oc)
* Git
* GitHub Repository

---

## Deploy

Create a project:

```bash
oc new-project demo-project
```

Import template:

```bash
oc create -f templates/python-external-template.yaml
```

View parameters:

```bash
oc process --parameters -f templates/python-external-template.yaml
```

Deploy:

```bash
oc process python-dashboard-template | oc apply -f -
```

Verify build:

```bash
oc get builds
```

Verify pods:

```bash
oc get pods
```

Verify route:

```bash
oc get route
```

---

## Technologies Used

* OpenShift
* Red Hat CRC
* Source-to-Image (S2I)
* Python
* GitHub
* YAML
* BuildConfig
* ImageStreams
* DeploymentConfig
* Service
* Route

---

## Skills Demonstrated

* OpenShift Administration
* Application Deployment
* S2I Builds
* Template Development
* ImageStream Management
* Troubleshooting Builds
* Route Configuration
* OpenShift CLI Operations

---

## Author

Shehryar Khan

