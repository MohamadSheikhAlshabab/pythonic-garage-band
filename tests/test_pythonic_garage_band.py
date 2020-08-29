from pythonic_garage_band import __version__
from pythonic_garage_band.pythonic_garage_band import Musician,Band,Bassist,Guitarist,Drummer
import pytest

def test_version():
    assert __version__ == '0.1.0'

@pytest.fixture
def data():
    michal=Guitarist("michal","Guitar")
    gasan=Bassist("gasan","Bass")
    jamil=Drummer("jamil","Drum")
    black_mirror=("Black Mirror",[michal,gasan,jamil])
    return {"jamil":jamil,"gasan":gasan,"michal":michal,"black_mirror":black_mirror}

def test_get_instrument(data):
    expected = "Bass"
    actual=data["gasan"].get_instrument()
    assert actual == expected

def test_to_list(data):
    expected = Band.to_list()
    actual=Band("black_mirror",["michal","gasan","jamil"]).to_list()
    assert actual == expected

def test_str(data):
    expected="michal"
    actual = data['michal'].__str__()
    assert expected == actual

def test_repr(data):
    expected = "gasan"
    actual = data['gasan'].__repr__()
    assert actual == expected

def test_play_solo(data):
    expected = "Trmmmm Teeerrm"
    actual=data["michal"].play_solo()
    assert actual == expected
