# Парсер файлов JSON

Скрипт принимает на вход файл json и выводит его в удобном для чтения виде: добавляет переносы строк, отступы слева и пробелы.

Состоит из двух функций:
load_data - отвечает за обработку входных данных
pretty_print - отвечает за вывод файла

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash
python json_parse.py <path to json file> # может понадобиться вызов python3 вместо python, зависит от настроек операционной системы
```
Импортироване функции и запуск :
```python
from  json_parse import load_data, pretty_print_json

pretty_print_json(load_data('<path to json file>')) # для Windows путь до файла обязательно пишем через двойной бэкслеш. Например : C:\\users\\root\\myfile.json
```
Запуск на Windows происходит аналогично.

Пример :

`python C:\Users\root\json_parse.py C:\Users\root\alco_shops.json`

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке ― [DEVMAN.org](https://devman.org)
