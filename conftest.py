import pytest
import json
from python_traning.fixture.application import Application
import os.path
import importlib
#scope="session"
# C помощью этого параметра браузер запускается только один раз при выполнении тестов

fixture = None
target = None

@pytest.fixture
def app(request):
    global fixture
    global target
    # browser = request.config.getoption("--browser")
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(config_file) as file:
            target = json.load(file)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=target["browser"])
    fixture.session.ensure_login(username=target["username"], password=target["password"])
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    # Не знаю почему не могу поменять в конфигурации на другое значение, отрабаытвают только по дефолтным
    # parser.addoption("--browser",action="store",default="chrome")
    parser.addoption("--target", action="store", default="target.json")

def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture,testdata ,ids=[str(x) for x in testdata])

def load_from_module(module):
    return importlib.import_module("data.%s"% module).constant