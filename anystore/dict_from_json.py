import json
def from_json(file_name):
    with open(file_name, "r", encoding='utf-8') as read_file:
        dict = json.load(read_file)
        return dict