import pytest
from lib.music_class import MusicListening

# test to see if we can add tracks 
def test_add_method_adds_tracks():
    musiclistening = MusicListening([])

    assert musiclistening.storage == []

    musiclistening.add_tracks("some track")

    assert musiclistening.storage == ["some track"]

def test_returns_list_of_tracks():
    musiclistening = MusicListening(["track1", "track2"])
    musiclistening.add_tracks("some track")
    musiclistening.add_tracks("some other track")
    musiclistening.add_tracks("some different track")

    assert musiclistening.list_all() == musiclistening.storage

def test_returns_empty_list_when_nothing_was_added():
     musiclistening = MusicListening([])

     assert musiclistening.list_all() == musiclistening.storage

def test_add_method_only_adds_strings():
    musiclistening = MusicListening([])
    with pytest.raises(Exception) as e:
        musiclistening.add_tracks(1)
    assert str(e.value) == "Track name must be a string"

    


