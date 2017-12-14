import json
import os
import pprint
import sys


def load_data(filepath):
    if os.path.isfile(filepath):
        with open(filepath, encoding='utf-8') as json_file:
            data = json.load(json_file)
            return data

def pretty_print_json(data):
    pprint.pprint(data)


if __name__ == '__main__':
    
    filepath = sys.argv[1]
    if os.path.isfile(filepath):
        with open(filepath, encoding='utf-8') as json_file:
            json_parsed = json.load(json_file)
            pprint.pprint(json_parsed)
    else:
        print('Такого файла не существует')
