import json
import os


filename = input('Введите путь до файла')
if os.path.isfile(filename):
    with open(filename,encoding='utf-8'.format(filename)) as json_file:
        parsed = json.load(json_file)
        print(json.dumps(parsed, indent=4,ensure_ascii=False, sort_keys=True))
else:
    print('Такого файла не существует')


