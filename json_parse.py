import json
import os
import sys

filename = sys.argv[1]
if os.path.isfile(filename):
    with open(filename,encoding='utf-8'.format(filename)) as json_file:
        parsed = json.load(json_file)
        print(json.dumps(parsed, indent=4,ensure_ascii=False, sort_keys=True))
else:
    print('Такого файла не существует')


