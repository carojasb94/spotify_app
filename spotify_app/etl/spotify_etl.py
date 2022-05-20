
from abc import (ABC, abstractmethod)
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy


class DBBackend(ABC):
    
    

    @abstractmethod
    def connect(self, arg1):
        pass

    def connect(self, arg1):
        pass



spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

results = spotify.current_user_recently_played(limit=50, after=None, before=None)
