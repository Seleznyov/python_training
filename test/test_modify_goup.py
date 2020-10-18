# -*- coding: utf-8 -*-
from python_traning.model.group import Group
from random import randrange

def test_modify_group_name(app):
    # Предусловие (создание новой группы)
    if app.group.count() == 0:
        app.group.create(Group(header="1", footer="1"))
    # Изменение группы
    old_list = app.group.get_group_list()
    group = Group(name="new_name")
    index = randrange(len(old_list))
    group.id = old_list[index].id
    app.group.modify_group_by_index(group,index)
    new_list = app.group.get_group_list()
    assert len(old_list) == len(new_list)
    old_list[index] = group
    assert sorted(old_list, key=Group.id_or_max) == sorted(new_list, key=Group.id_or_max)

# def test_modify_group_header(app):
#     # изменение группы
#     if app.group.count() == 0:
#         app.group.create(Group(name="1", footer="1"))
#     app.group.modify_first_group(Group(header="new_header"))