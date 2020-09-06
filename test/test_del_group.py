# -*- coding: utf-8 -*-

def test_del_group(app):
    # login
    app.session.login(username="admin", password="secret")
    # создание новой группы
    app.group.delete_first_group()
    # logout
    app.session.logout()