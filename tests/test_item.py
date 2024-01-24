"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from config import DICT_DIR
from src.item import Item
from src.phone import Phone

@pytest.fixture
def item_fixture():
    """Создаем экземпляр класса в фикстуре"""
    return Item("Смартфон", 10000, 20)

def test___repr__(item_fixture):
    assert repr(item_fixture) == "Item('Смартфон', 10000, 20)"


def test___str__(item_fixture):
    assert str(item_fixture) == 'Смартфон'

def test_calculate_total_price(item_fixture):
    assert item_fixture.calculate_total_price() == 200000

def test_apply_discount(item_fixture):
    Item.pay_rate = 0.8
    item_fixture.apply_discount()
    assert item_fixture.price == 8000.0

def test_instantiate_from_csv():
    Item.instantiate_from_csv(DICT_DIR)
    assert len(Item.all) == 5
    item_fixture = Item.all[0]
    assert item_fixture.name == 'Смартфон'

def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

def test___add__():
    item1 = Item("Смартфон", 10000, 20)
    phone1 = Phone("iPhone 14", 120_000, 5, 2)

    assert phone1 + phone1 == 10
    assert item1 + phone1 == 25
    assert item1 + item1 == 40
    with pytest.raises(Exception):
        item1 + 5