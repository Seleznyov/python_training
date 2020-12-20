# -*- coding: utf-8 -*-
from python_traning.model.group import Group
# 1-й стопособ который был
# import pytest
# from python_traning.data.groups import constant as testdata

# 1-й стопособ который был
# @pytest.mark.parametrize("group",testdata, ids=[str(x) for x in testdata])
def test_add_group(app,json_groups):
    group = json_groups
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
