# Fabric Detection Model

## Overview

This project implements a machine learning-based solution for detecting fabric types from images. The model is capable of classifying two types of fabrics, viz., corduroy and denim. 

Initially we started with six fabrics, viz., cotton, corduroy, denim, linen and wool. Through further literature review we narrowed down to corduroy and denim. 

First the project was prototyped in jupyter notebooks and then the final solution was implemented in modular code structure ensuring that various components (training, feature extraction, deployment) are organized for ease of use, scaling, and further enhancement. This branch represents the stable and production-ready version of the project.

## Details of the branches of this repository

1. `main` branch: Contains the stable and production-ready version of the project
2. `laptop_notebooks_branch` : All the prototyping jupyter notebooks made and executed on our local system.
3. `colab_notebooks_branch`: All the prototyping Google Colaboratory notebooks made and executed using Google Colab Pro due to compute resource limitation on our local laptop. _Note: This branch was made after the laptop_notebooks_branch and contains the final prototyping code._
4.  `development_branch` : Contains all the integrated changes after exmperimentation. Follows modular code sturcture.
5.  `final_train_pipeline` : Feature branch of development_branch. Cotains the finalized code for training pipeline
6.  `deployment_pipeline`: Feature branch of development_branch. Contains the finalized code for deployment pipeline.
7.  `ebs_deployment`: Feature branch of deployment_branch. This branch was used to make changes in the deployment pipeline to integrate ElasticBeanstalk & S3 configurations in our code.

_**To understand branch specific code refer to the respective branch's README.md**_

## Pipelines in the project

1. **Training Pipeline**

   i. **Nested Cross Validatin Pipeline**:<br>
   Performs nested cross validation with RandomizedSearchCV to select the best model hyperparameters and evaluate the model performance through cross validation.

   ii. **Final Training Pipeline**:<br>
   Trains the best selected model from nested cross validation pipeline on the entire training data.

2. **Deployment Pipeline**<br>

Creates a flask web application to use the trained model from the **Training Pipeline** . This code has been configured to be used in ElasticBeanstlak environment wiht S3 storage. You cannot directly run the flask web application on your local system.

## How to execute each pipeline?

1. Training Pipeline:
   ```bash
   python execute_cross_validation.py  # Performs nested cross validation
   python execute_final_model_training.py # Performs the final model training on the entire training data
   ```

2. Deployment Pipeline: You need to make certain changes in the feature_engineering components and prediction components to run this pipeline locally with the following code. Otherwise deploy into ElasticBeanstlak environment and store the Training Pipeline artifacts in an S3 bucket, then you need not to run the following code.
   ```bash
   python deployment/app.py
   ```

## Full Documentation

See the Wiki for this repository to gain a complete understanding of how this project was made.
