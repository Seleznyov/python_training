from python_traning.model.group import Group
import random
import string


constant = [
    Group(name="name1", header="header1", footer="footer1"),
    Group(name="name2", header="header2", footer="footer2")
]

# Функция по генерации случ чисел
def random_string(prefics, maxlen):
    # Добавим string.punctuation (знаки пунктуации)
    symbols=string.ascii_letters+string.digits+" "*10
    return prefics +"".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

# Первый варианг герации данных (одна пустая строка, и остальные случайные наборы)
# testdata=[Group(name="", header="", footer="")]+[
#     Group(name=random_string("name",10), header=random_string("header",10), footer=random_string("footer",10))
#     for i in range(5)
# ]

# Второй вариант полный перебор
testdata=[Group(name=name, header=header, footer=footer)
    for name in ["", random_string("name",10)]
    for header in ["", random_string("header",10)]
    for footer in ["", random_string("footer",10)]
]