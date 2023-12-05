import json
from django.conf import settings
import os


def load_data_from_json(file_name):
    json_file_path = os.path.join(settings.BASE_DIR, 'data', file_name)
    with open(json_file_path, 'r', encoding='utf-8') as file:
        return json.load(file)
