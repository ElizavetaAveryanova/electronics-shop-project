import pytest
from src.phone import Phone

@pytest.fixture
def phone_fixture1():
    """Создаем экземпляр класса в фикстуре"""
    return Phone("iPhone 14", 120_000, 5, 2)

@pytest.fixture
def phone_fixture2():
    """Создаем 2-й экземпляр класса в фикстуре"""
    return Phone("Смартфон", 10000, 20, 0)

def test___repr__(phone_fixture1, phone_fixture2):
    assert repr(phone_fixture1) == "Phone('iPhone 14', 120000, 5, 2)"
    assert repr(phone_fixture2) == "Phone('Смартфон', 10000, 20, 0)"

def test___str__(phone_fixture1, phone_fixture2):
    assert str(phone_fixture1) == 'iPhone 14'
    assert str(phone_fixture2) == 'Смартфон'

def test_number_of_sim(phone_fixture1, phone_fixture2):
    assert phone_fixture1.number_of_sim == 2
    with pytest.raises(Exception):
        phone_fixture2.number_of_sim = 0
        type(phone_fixture2.number_of_sim) is not int

