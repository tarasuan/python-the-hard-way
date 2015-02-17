from nose.tools import *
from ex48 import lexicon1

def test_directions():
    assert_equal(lexicon1.scan("north"), [('direction', 'north')])