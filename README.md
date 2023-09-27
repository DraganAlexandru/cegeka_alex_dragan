# Alex Dragan Cegeka Interview

## Description

Flask application that queries data from CV.

## Prerequisites

- Python (version 3.9)
- [Pip](https://pip.pypa.io/en/stable/)
- [Virtualenv](https://pypi.org/project/virtualenv/) (recommended for virtual environments)

## Installation

1. Clone the repository to your local machine:

  ```bash
  git clone https://github.com/DraganAlexandru/cegeka_alex_dragan/tree/master
  ```

2. Navigate to the project directory
  
  ```bash
  cd cegeka_alex_dragan
  ```

3. Create a virtual environment (recommended):

  ```bash
  virtualenv venv
  ```

4. Activate the virtual environment:

  On macOS and Linux:
  
  ```bash
  source venv/bin/activate
  ```

On Windows:

  ```bash
  .\venv\Scripts\activate
  ```

5. pip install -r requirements.txt
  
  ```bash
  pip install -r requirements.txt
  ```

## Usage

Running the Flask App

1. Make sure you are in the project directory, and the virtual environment is activated.
   
2. Start the Flask development server:

  ```bash
  python run.py
  ```
3. Open a web browser and go to http://localhost:5000/ to access the application.

Using the CLI

To display CV data using the CLI, you can run the following command in the terminal:
  
  ```bash
  python cli.py display_cv_data [section]
  ```

Replace [section] with one of the following options: personal, experience, or education.

For example, to display personal information:

  ```bash
  python cli.py display_cv_data personal
  ```

## Running tests

Running the Flask tests
  
  ```bash
  python -m pytest tests/test_app.py
  ```

Running the CLI tests
  
  ```bash
  python -m unittest tests.test_cli
  ```
