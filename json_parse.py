import json
import os
import sys


def untreated_json_data(filepath):
    if os.path.isfile(filepath):
        with open(filepath, encoding='utf-8') as json_file:
            json_data = json.load(json_file)
            return json_data


def pretty_print_json(json_data):
    print(json.dumps(json_data, indent=4,ensure_ascii=False, sort_keys=True))


if __name__ == '__main__':
    filepath = sys.argv[1]
    data_json = untreated_json_data(filepath)
    pretty_print_json(data_json)
