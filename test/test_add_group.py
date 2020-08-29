# -*- coding: utf-8 -*-
import pytest
from python_traning.model.group import Group
from python_traning.fixture.application import Application

@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    # login
    app.session.login(username="admin", password="secret")
    # создание новой группы
    app.group.create(Group(name="1", header="1", footer="1"))
    # logout
    app.session.logout()