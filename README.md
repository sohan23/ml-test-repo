# Machine Learning Model

This repository contains a basic machine learning model implemented using scikit-learn. The project includes data preprocessing, model training, and evaluation functions.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/githubnext/workspace-blank.git
   cd workspace-blank
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Project

1. Navigate to the `src` directory:
   ```bash
   cd src
   ```

2. Run the training script:
   ```bash
   python train.py
   ```

## Running the Tests

1. Navigate to the root directory of the project.

2. Run the tests using pytest:
   ```bash
   pytest
   ```

## Continuous Integration (CI) Setup

This project uses GitHub Actions for continuous integration. The CI pipeline is configured to automatically run the tests on each commit.

To set up the CI pipeline, follow these steps:

1. Create a `.github/workflows` directory in the root of the repository.

2. Add a `ci.yml` file in the `.github/workflows` directory with the following content:
   ```yaml
   name: CI

   on: [push, pull_request]

   jobs:
     build:
       runs-on: ubuntu-latest

       steps:
       - name: Checkout code
         uses: actions/checkout@v2

       - name: Set up Python
         uses: actions/setup-python@v2
         with:
           python-version: 3.8

       - name: Install dependencies
         run: |
           python -m venv venv
           source venv/bin/activate
           pip install -r requirements.txt

       - name: Run tests
         run: |
           source venv/bin/activate
           pytest
   ```
