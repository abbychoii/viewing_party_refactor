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
    # assert