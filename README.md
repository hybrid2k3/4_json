# Парсер файлов JSON

Скрипт принимает на вход файл json и выводит его в удобном для чтения виде: добавляет переносы строк, отступы слева и пробелы.

Состоит из двух функций:
load_data - отвечает за загрузку входных данных
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

На выходе имеем отформатированный JSON который удобно читать:
```json
           "properties": {
                "Attributes": {
                    "Address": "Мартеновская улица, дом 23",
                    "AdmArea": "Восточный административный округ",
                    "ClarificationOfWorkingHours": null,
                    "District": "район Новогиреево",
                    "IsNetObject": "нет",
                    "Name": "МАГАЗИН «РОЗЛИВНОЕ ПИВО»",
                    "OperatingCompany": null,
                    "PublicPhone": [
                        {
                            "PublicPhone": "(929) 678-86-50"
                        }
                    ],
                    "TypeService": "реализация продовольственных товаров",
                    "WorkingHours": [
                        {
                            "DayOfWeek": "понедельник",
                            "Hours": "11:00-23:00"
                        },
                        {
                            "DayOfWeek": "вторник",
                            "Hours": "11:00-23:00"
                        },
                        {
                            "DayOfWeek": "среда",
                            "Hours": "11:00-23:00"
                        },
                        {
                            "DayOfWeek": "четверг",
                            "Hours": "11:00-23:00"
                        },
                        {
                            "DayOfWeek": "пятница",
                            "Hours": "11:00-23:00"
                        },
                        {
                            "DayOfWeek": "суббота",
                            "Hours": "11:00-23:00"
                        },
                        {
                            "DayOfWeek": "воскресенье",
                            "Hours": "11:00-23:00"
                        }
                    ],
                    "global_id": 25156878
                },
                "DatasetId": 1854,
                "ReleaseNumber": 2,
                "RowId": "9e3243be-5148-46e5-9139-1e9a93f00928",
                "VersionNumber": 1
```

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке ― [DEVMAN.org](https://devman.org)
