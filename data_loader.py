import json


def load_cv_data(file_path):
    try:
        with open(file_path, 'r') as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        raise FileNotFoundError("CV data file not found.")
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Error parsing JSON: {str(e)}", e.doc, e.pos)
