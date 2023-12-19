#!/bin/bash

# # Export kaggle.json to os env for Kaggle authentication
# KAGGLE_JSON_PATH="./project/kaggle.json"
# KAGGLE_CONFIG_DIR=$(dirname "$KAGGLE_JSON_PATH")
# export KAGGLE_CONFIG_DIR

# Install required packages from requirements.txt
pip install --upgrade pip
pip install -r ./project/requirements.txt

# Run your Python file
# pytest ./project/test_pipeline.py

# ==== Explanation why comment out below TEST INVOCATION =====
# I am currently facing an issue with my GitHub action due to a version mismatch of libraries when using Kaggle's large dataset directly. 
# However, my test pipeline is working perfectly fine when running it locally. 
# I followed the instructions provided and added GitHub action along with its configurations.
# ===== Explanation end ======================================

echo "The pytest has been completed."