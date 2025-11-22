import pytest
from television import Television

@pytest.fixture
def tv():
    return Television()



def test_init(tv):
    #expected values at their lowest
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"



def test_power(tv):
    tv.power()
    assert str(tv).startswith("Power = True")
    tv.power()
    assert str(tv).startswith("Power = False")



def test_mute_tv_off(tv):
    tv.mute()
    #tv off, mute doesnt go through
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"


def test_mute_volume(tv):
    tv.power()
    tv.volume_up() #vol =1
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"
    tv.mute() #mutes
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    tv.mute() #mute off
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"




def test_channel_tv_off(tv):
    tv.channel_up()
    tv.channel_down()
    #channels dont change while tv off
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"


def test_channel_max(tv):
    tv.power() #channel =0
    tv.channel_up() #channel =1
    tv.channel_up()#channel =2
    tv.channel_up()#channel =3
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"
    tv.channel_up()#channel =0
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"


def test_channel_down_min(tv):
    tv.power()# channel=0
    tv.channel_down() # channel=0 ->channel=3
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"



def test_volume_buttons_tv_off(tv):
    tv.volume_up()
    tv.volume_down()
    #buttons dont work because tv is off
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"


def test_volume_up_max(tv):
    tv.power()
    tv.volume_up() #vol=1
    tv.volume_up()  #vol=2
    tv.volume_up() #vol=2
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"


def test_volume_down_min(tv):
    tv.power()
    tv.volume_down() #vol=0, cant go below
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"


def test_volume_changes_up(tv):
    tv.power()
    tv.volume_up() #vol=1
    tv.mute() #muted/vol=0
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    tv.volume_up() #unmute then vol=2
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"


def test_volume_changes_down(tv):
    tv.power()
    tv.volume_up() #vol=1
    tv.volume_up() #vol=2
    tv.mute() #muted/vol=0
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"
