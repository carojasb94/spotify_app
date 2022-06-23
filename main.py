
from decouple import config

from spotify_app.etl.spotify_etl import SpotifyETL
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy

CLIENT_ID = config("SPOTIFY_CLIENT_ID", "")
CLIENT_SECRET = config("SPOTIFY_CLIENT_SECRET", "")
REDIRECT_URL = config("SPOTIPY_REDIRECT_URI", "")
print(CLIENT_ID, CLIENT_SECRET)

if __name__ == '__main__':
    
    db = object()
    sp_client = spotipy.Spotify(
        client_credentials_manager=SpotifyClientCredentials(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
        )
    )

    
    client = SpotifyETL(db, sp_client)
    client._login(CLIENT_ID, CLIENT_SECRET, REDIRECT_URL)
    # client.extract()
    pass

