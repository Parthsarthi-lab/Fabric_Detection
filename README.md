# Fabric Detection Model

## Overview

This project implements a machine learning-based solution for detecting fabric types from images. The model is capable of classifying two types of fabrics, viz., corduroy and denim. 

Initially we started with six fabrics, viz., cotton, corduroy, denim, linen and wool. Through further literature review we narrowed down to corduroy and denim.

First the project was prototyped in jupyter notebooks and then the final solution was implemented in modular code structure ensuring that various components (training, feature extraction, deployment) are organized for ease of use, scaling, and further enhancement. This branch represents the stable and production-ready version of the project.


## Full Documentation

See the Wiki for this repository to gain a complete understanding of how this project was made.

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
