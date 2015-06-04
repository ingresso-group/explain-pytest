import pytest
from animals.models import Cat

def test_cat(db):
    cats = Cat.objects.all()
    print cats
    assert False
