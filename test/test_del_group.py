# -*- coding: utf-8 -*-
from python_traning.model.group import Group
from random import randrange

def test_del_group(app):
    # Предусловие (создание новой группы)
    if app.group.count() == 0:
        app.group.create(Group(name="1", header="1", footer="1"))
    # Удаление группы
    old_list = app.group.get_group_list()
    index = randrange(len(old_list))
    app.group.delete_group_by_index(index)
    new_list = app.group.get_group_list()
    assert len(old_list) - 1 == len(new_list)
    del old_list[index]
    assert old_list == new_list