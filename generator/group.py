from python_traning.model.group import Group
import random
import string
import os.path
import json
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
name_file = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

# Функция по генерации случ чисел
def random_string(prefics, maxlen):
    # Добавим string.punctuation (знаки пунктуации)
    symbols = string.ascii_letters+string.digits+" "*10
    return prefics + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

# Первый варианг герации данных (одна пустая строка, и остальные случайные наборы)
testdata = [Group(name="", header="", footer="")]+[
    Group(name=random_string("name",10), header=random_string("header",10), footer=random_string("footer",10))
    for i in range(n)
]

# Второй вариант полный перебор
# testdata=[Group(name=name, header=header, footer=footer)
#     for name in ["", random_string("name",10)]
#     for header in ["", random_string("header",10)]
#     for footer in ["", random_string("footer",10)]
# ]

new_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", name_file)

with open(new_file, "w") as file:
    jsonpickle.set_encoder_options("json", indent=2)
    file.write(jsonpickle.encode(testdata))
    # file.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))