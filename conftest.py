import pytest
from python_traning.fixture.application import Application

#scope="session"
#с помощью этого параметра браузер запускается только один раз при выполнении тестов

@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture