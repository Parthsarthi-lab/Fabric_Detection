# Fabric Detection Model

## Overview

This project implements a machine learning-based solution for detecting fabric types from images. The model is capable of classifying different types of fabrics such as corduroy, denim, and linen. It has been built using a combination of image processing techniques, feature extraction methods, and machine learning algorithms.

The project has been developed with modular code, ensuring that various components (training, feature extraction, deployment) are organized for ease of use, scaling, and further enhancement. This branch represents the stable and production-ready version of the project.

## Features

- **Fabric Classification**: Supports classification of fabric types like corduroy, denim, and linen.
- **Image Processing**: Pre-processes the images for better classification accuracy.
- **In-Memory Processing**: Images are processed directly in-memory without being stored on disk, ensuring a fast and lightweight solution.
- **Deployment-Ready**: Includes configurations for deploying the model on AWS Elastic Beanstalk with minimal setup.

## Project Structure

- **`artifacts/`**: Stores model artifacts such as the trained model, configurations, and logs.
- **`common/`**: Contains utility scripts such as the configuration manager.
- **`deployment/`**: Contains the deployment pipeline code, including the `Flask` app for serving predictions.
- **`training/`**: Includes the training pipeline code for creating and validating the model.
- **`requirements.txt`**: Lists all the dependencies needed for the project.
- **`app.py`**: The main Flask application that serves predictions.

## Installation

To set up the environment for this project, follow the steps below:

### Prerequisites

- Python 3.8+
- AWS account (for Elastic Beanstalk deployment)
- Virtual environment (optional, but recommended)

### Steps

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/fabric_detection_model.git
    cd fabric_detection_model
    ```

2. **Set up Virtual Environment** (optional):
    ```bash
    python -m venv fabric_env
    source fabric_env/bin/activate   # For Linux/Mac
    fabric_env\Scripts\activate      # For Windows
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up AWS Elastic Beanstalk** (for deployment):
    - Set up AWS Elastic Beanstalk and configure your environment.
    - Configure your S3 bucket for storing artifacts (e.g., model, processed images).

## Usage

### Running the Flask Application Locally

You can run the model prediction service locally using the Flask web app.

```bash
python deployment/app.py
