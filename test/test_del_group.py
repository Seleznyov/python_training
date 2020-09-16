# -*- coding: utf-8 -*-
from python_traning.model.group import Group

def test_del_group(app):
    # создание новой группы
    if app.group.count() == 0:
        app.group.create(Group(name="1", header="1", footer="1"))
    app.group.delete_first_group()