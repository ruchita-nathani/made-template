# Install required packages from requirements.txt
pip install --upgrade pip
pip install -r ./requirements.txt

# Run your Python file
pytest ./test_pipeline.py

echo "The pytest has been completed."