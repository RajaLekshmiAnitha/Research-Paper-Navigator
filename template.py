import os
from pathlib import Path
import logging


#login screen
logging.basicConfig(level=logging.INFO, format= '[%(asctime)s] : %(message)s')
#basicConfig is a function inside the logginng library


project_name = 'researchPaperNavigator'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",  #__init__.py is the constructor file, it initializes a module
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    'params.yaml',
    'app.py',
    'main.py',
    'Dockerfile',
    'requirements.txt',
    'setup.py',
    'research/trials.ipynb',
]


for filepath in list_of_files:
    filepath = Path(filepath)   #Path library is used to identify which operating system we are using, if it is OS or Windows
    #the filepaths given above contains both the folder and file names, so we need to split them to get the folder and file names separately
    filedir, filename = os.path.split(filepath)

    #now check if the directory exists, if not, create it
    if filedir not in ['', '.']:  #if filedir is not empty or '.' (root directory)
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created file: {filedir} for the file: {filename}")

    #if the file does not exist also check the file size, create it
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass    #create an empty file that's why we are just passing it
            logging.info(f"Created empty file: {filepath}")
    else:
        logging.info(f"File name: {filename} already exists")