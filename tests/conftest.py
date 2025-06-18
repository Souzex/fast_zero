import pytest
from fastapi.testclient import TestClient
from src.fast_zero.app_dedezao import app_dedezinho

@pytest.fixture()    
def clientao():
    return TestClient(app_dedezinho)