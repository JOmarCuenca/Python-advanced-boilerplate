#! /bin/bash

# Assert we are at the root of the project
if [ ! -f "requirements.txt" ]
then
    echo "This script should be run at the root of the project"
    exit 1
fi

# Assert we have python3 installed
if ! command -v python3 &> /dev/null
then
    echo "python3 could not be found"
    exit 1
fi

# Assert we have pip3 installed
if ! command -v pip3 &> /dev/null
then
    echo "pip3 could not be found"
    exit 1
fi

# Create the env
echo "Creating the virtual environment"
python3 -m venv env && source env/bin/activate

# Install the requirements
pip install -r requirements.txt

# Assert we have pre-commit installed
if ! command -v pre-commit &> /dev/null
then
    echo "pre-commit could not be found"
    exit 1
fi

# Install the pre-commit hooks
echo "Installing the pre-commit hooks"
pre-commit install

# Deactivate the env
deactivate

# Done
echo "Done :D"
