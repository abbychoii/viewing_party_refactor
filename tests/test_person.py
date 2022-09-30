import pytest
from viewing_party.person import Person

def test_add_watched():
    # Arrange
    kimia = Person('kimia', ['Bee Movie'], ['abby','nancy'], ['netflix'])

    # self, name, watched, friends, subscriptions):
    # Act
    kimia.add_watched('Titanic')
    # Assert
    assert(kimia.watched[1] =='Titanic')
    assert(len(kimia.watched)==2)

def test_get_num_watched():
    kimia = Person('kimia', ['Bee Movie'], ['abby','nancy'], ['netflix'])

    num_watched= kimia.get_num_watched()

    assert(num_watched == 1)