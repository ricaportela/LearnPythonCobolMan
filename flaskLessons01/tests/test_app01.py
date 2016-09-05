import pytest

from flaskLessons01.learning01 import app


@pytest.mark.usefixtures('client_class')
class TestApp:
    @pytest.fixture
    def test_home(self):
        response = self.client.get("/")
        assert response.data.decode('utf-8') == "<h1>Testando...</h1>"
        assert response.status_code == 200
