import json
import os
import pprint
import sys


def load_data(filepath):
    if os.path.isfile(filepath):
        with open(filepath, encoding='utf-8') as json_file:
            json_data = json.load(json_file)
            return json_data

def pretty_print_json(json_data):
    pprint.pprint(json_data)


if __name__ == '__main__':
    
    filepath = sys.argv[1]
    if os.path.isfile(filepath):
        with open(filepath, encoding='utf-8') as json_file:
            json_data = json.load(json_file)
            pprint.pprint(json_data)
    else:
        print('Такого файла не существует')
