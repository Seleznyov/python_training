# -*- coding: utf-8 -*-
from python_traning.model.group import Group
import pytest
import random
import string

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

@pytest.mark.parametrize("group",testdata, ids=[str(x) for x in testdata])
def test_add_group(app,group):
    # Создание новой группы
    old_list = app.group.get_group_list()
    # group = Group(name="1", header="1", footer="1")
    app.group.create(group)
    # Добвлена хеш функиция count()
    assert len(old_list)+1 == app.group.count()
    new_list = app.group.get_group_list()
    old_list.append(group)
    assert sorted(old_list, key=Group.id_or_max) == sorted(new_list, key=Group.id_or_max)


# def test_add_empty_group(app):
#     # Создание новой пустой группы
#     # Добавлено кэширование
#     old_list = app.group.get_group_list()
#     group = Group(name="", header="", footer="")
#     app.group.create(group)
#     new_list = app.group.get_group_list()
#     assert len(old_list)+1 == len(new_list)
#     old_list.append(group)
#     assert sorted(old_list, key=Group.id_or_max) == sorted(new_list, key=Group.id_or_max)
