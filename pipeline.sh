#!/bin/bash

echo "Step 1: Creating datasets"
venv/Scripts/python.exe data_creation.py

echo "Step 2: Preprocessing data"
venv/Scripts/python.exe model_preprocessing.py

echo "Step 3: Training model"
venv/Scripts/python.exe model_preparation.py

echo "Step 4: Testing model"
venv/Scripts/python.exe model_testing.py

echo "Pipeline finished"