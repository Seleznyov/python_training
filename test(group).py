# -*- coding: utf-8 -*-
import pytest
from python_traning.group import Group
from python_traning.application import Application

@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_app(app):
    # login
    app.login(username="admin", password="secret")
    # создание новой группы
    app.create_gruop(Group(name="1", header="1", footer="1"))
    # logout
    app.logout()