import os
from pathlib import Path

list_of_file =[
    ".github/workflow/.gitkeep",
    "src/compo/__init__.py",
    "src/compo/data_ingestion.py",
    "src/compo/data_transformation.py",
    "src/compo/model_training.py",
    "src/compo/model_evaluation.py",
    "src/monodb_connect/__init__.py"
    "src/monodb_connect/mono_curd.py"
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/utils.py",
    "src/utils/__init__.py",
    "src/logger/logging.py",
    "src/exception/exception.py",
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/unit/unit.py",
    "tests/integration/__init__.py",
    "tests/integration/inti.py",
    "init_steup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "steup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/expiri.ipynb"

]


for filepath in list_of_file:
    filepath = Path(filepath)
    filedir, filename= os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass