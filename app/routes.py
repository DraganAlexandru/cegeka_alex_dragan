from flask import jsonify

from app import app
from cv_data import cv_data


@app.route('/')
def hello_world():
    """
    Render the homepage.

    Returns:
        str: A simple welcome message.
    """
    return 'Alex Dragan CV!'


@app.route('/personal', methods=['GET'])
def get_personal_info():
    """
    Retrieve personal information from the CV data.

    Returns:
        dict: JSON data containing personal information.
    """
    return jsonify(cv_data['personal'])


@app.route('/experience', methods=['GET'])
def get_experience():
    """
    Retrieve experience information from the CV data.

    Returns:
        dict: JSON data containing experience information.
    """
    return jsonify(cv_data['experience'])


@app.route('/education', methods=['GET'])
def get_education():
    """
    Retrieve education information from the CV data.

    Returns:
        dict: JSON data containing education information.
    """
    return jsonify(cv_data['education'])
