
from urllib import request
import pandas as pd
import requests
import datetime


DB_PATH = "sqlite://my_tracks.sqlite"
USER_ID = ""
TOKEN = "BQD7sEIp0dCFiTbpuxHusU4fuHOFaEo23dikm-zU-_w6Xtj07ZRBBDzr3dyO2iYZ0daE37pBiD7DqO0PjXWY1LyvQk0AdvXAw38MjFpqSaQBK6hegmYfc7_f-sQAyUC76OiT4r52WxHo-CJDRmA8qH5WfzEC"
LIMIT = 50
URL = "https://api.spotify.com/v1/me/player/recently-played?limit={limit}&after={after}"


def get_range():
    """
    Returns:
        _type_: _description_
    """
    today = datetime.datetime.today()
    yesterday = today - datetime.timedelta(days=1)
    yesterday_timestamp = int(yesterday.timestamp()) *1000
    return yesterday_timestamp


def get_headers():
    return {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN}",
    }


def get_tracks(auth_token: str = None):
    """_summary_

    Args:
        auth_token (None): _description_
    """
    formated_url = URL.format(limit=LIMIT, after=get_range())
    print(f"Calling {formated_url}")
    resp = requests.get(formated_url, headers=get_headers())

    data =  resp.json()
    songs = list()
    artist = list()
    played_at = list()
    timestamps = list()
    
    for d in data.get("items", []):
        songs.append(d["track"]["name"])
        artist.append(d["track"]["album"]["artists"][0]["name"])
        played_at.append(d["played_at"])
        timestamps.append(d["played_at"][0:10])

    songs_dict = {
        "song_name": songs,
        "artist_name": artist,
        "played_at": played_at,
        "timestamp": timestamps,
    }
    songs_df = pd.DataFrame(songs_dict, columns=songs_dict.keys())
    print(songs_df)
    # import ipdb; ipdb.set_trace()    
    print(data.get("next", ""))
    print(data.get("cursors", {}))


def save_tracks(tracks: list):
    pass


def to_pd():
    pass


if __name__ == '__main__':
    
    get_tracks()

