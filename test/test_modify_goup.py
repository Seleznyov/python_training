# -*- coding: utf-8 -*-
from python_traning.model.group import Group

def test_modify_group_name(app):
    # изменение группы
    if app.group.count() == 0:
        app.group.create(Group(header="1", footer="1"))
    app.group.modify_first_group(Group(name="new_name"))

def test_modify_group_header(app):
    # изменение группы
    if app.group.count() == 0:
        app.group.create(Group(name="1", footer="1"))
    app.group.modify_first_group(Group(header="new_header"))