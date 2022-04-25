import json

with open('catalog.json', 'r') as f:
    # json -- текстовый формат, мы можем прочитать все содержимое
    # файла в переменную и сразу преобразовать с помощью json.loads
    content = f.read()
    catalog = json.loads(content)

for i in range(3):
    name = input('Введите наименование товара')
    count = int(input('Введите количество товара'))
    # если ключ (наименование товара) уже есть
    # в словаре
    if name in catalog:
        # увеличиваем его значение на count
        catalog[name] += count
    else:
        # иначе создаем ключ со значением count
        catalog[name] = count

with open('catalog.json', 'w') as f:
    # записываем все строку, полученную с помощью
    # json.dumps в файл
    content = json.dumps(catalog)
    f.write(content)
