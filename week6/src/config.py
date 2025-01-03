import os

# Get the current directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define paths
MODEL_PATH = os.path.join(BASE_DIR, '../models/model_file.pkl')
LOG_PATH = os.path.join(BASE_DIR, '../logs/app.log')
DATA_PATH = os.path.join(BASE_DIR, '../data/')
DOCKERFILE_PATH = os.path.join(BASE_DIR, '../Dockerfile')
REQUIREMENTS_PATH = os.path.join(BASE_DIR, '../requirements.txt')

# Print paths for verification (optional)
if __name__ == "__main__":
    print("Model Path:", MODEL_PATH)
    print("Log Path:", LOG_PATH)
    print("Data Path:", DATA_PATH)
    print("Dockerfile Path:", DOCKERFILE_PATH)
    print("Requirements Path:", REQUIREMENTS_PATH)