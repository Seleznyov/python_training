# -*- coding: utf-8 -*-
from python_traning.model.group import Group

def test_add_group(app):
    # создание новой группы
    app.group.create(Group(name="1", header="1", footer="1"))
