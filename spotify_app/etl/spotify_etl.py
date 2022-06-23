
from abc import (ABC, abstractmethod)
import spotipy
from spotipy.oauth2 import (SpotifyOAuth, SpotifyClientCredentials)
from decouple import config

class DBBackend(ABC):
    
    @abstractmethod
    def connect(self, arg1):
        pass

    def connect(self, arg1):
        pass


class SpotifyETL(object):

    def __init__(self, db_backend, client):
        self.db_backend = db_backend
        self.client = client
        
    def _login(self, id, secret, uri):
        # scope = "user-library-read"
        scope = "user-read-recently-played"        
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=id,
            client_secret=secret,
            redirect_uri=uri,
            scope=scope))
        print(sp)
        res = sp.current_user_recently_played(limit=50, after=None, before=None)
        res.get("items")
        import ipdb; ipdb.set_trace()
        return sp
        

    def extract(self):
        results = self.client.current_user_recently_played(limit=50, after=None, before=None)
        print(results)
        import ipdb; ipdb.set_trace()
        return results        

    def transform(self):
        pass

    def load(self):
        pass

