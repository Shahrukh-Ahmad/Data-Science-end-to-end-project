import os
from pathlib import Path
import logging

# The os module lets you interact with the operating system.
# os → OS-level operations (files, dirs, env variables)

# Path (pathlib) → Modern, clean file path handling

# logging → Record and manage logs instead of print




# Sets up logging with INFO level.
# This means messages like logging.info() will be displayed in the console.
logging.basicConfig(level=logging.INFO)



# Define project name
project_name=  "End-to-End Data Science Project"


# List all files to create

list_of_files = [
    # ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_tranier.py",
    f"src/{project_name}/components/model_monitering.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"
]


# Path(filepath) → makes it easier to work with file paths.
# os.path.split() → separates the directory and file name.
for filepath in list_of_files:
    filepath = Path(filepath)     # Convert string path to Path object
    filedir, filename = os.path.split(filepath)     # Split into folder and file





# os.path.exists(filepath) → checks if the file already exists.
# os.path.getsize(filepath) == 0 → checks if the file is empty.
# with open(filepath,'w') as f: → creates the file if it doesn’t exist.
# Logging messages tell us whether the file was created or already exists.
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    
    else:
        logging.info(f"{filename} is already exists")