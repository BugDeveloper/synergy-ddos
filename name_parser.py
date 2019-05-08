import requests
import htmlement
import json
r = requests.get('https://ru.wikipedia.org/wiki/Категория:Русские_женские_имена')


root = htmlement.fromstring(r.content)
lst = []
write = False

for item in root.iterfind(".//a"):
    if not item.text:
        continue
    name = item.text.split()[0]

    if name == 'Авдей' or 'Агафья':
        write = True
    if not write:
        continue
    if 'https://' in name:
        break

    with open("names.txt", "a") as names_file:
        names_file.write(name + ', ')
