from flask import jsonify

from app import app
from data_loader import load_cv_data

cv_data = load_cv_data('cv_data.json')


@app.route('/')
def hello_world():
    return 'Alex Dragan CV!'


@app.route('/personal', methods=['GET'])
def get_personal_info():
    return jsonify(cv_data['personal'])


@app.route('/experience', methods=['GET'])
def get_experience():
    return jsonify(cv_data['experience'])


@app.route('/education', methods=['GET'])
def get_education():
    return jsonify(cv_data['education'])
