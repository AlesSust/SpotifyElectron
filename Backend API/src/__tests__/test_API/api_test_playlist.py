from main import app as app
from fastapi.testclient import TestClient


client = TestClient(app)


def create_playlist(name: str, descripcion: str, foto: str,creador:str):

    url = f"/playlists/?nombre={name}&foto={foto}&descripcion={descripcion}&creador={creador}"

    payload = []

    response = client.post(
        url, json=payload, headers={"Content-Type": "application/json"}
    )

    return response


def get_playlist(name: str):

    response = client.get(f"/playlists/{name}")
    return response

def get_playlists(song_names: str):

    response = client.get(f"/playlists/multiple/{song_names}")
    return response


def update_playlist(
        name: str,
        descripcion: str,
        foto: str,
        nuevo_nombre: str = ""):

    if nuevo_nombre == "":
        url = f"/playlists/{name}/?foto={foto}&descripcion={descripcion}"

    else:
        url = f"/playlists/{name}/?foto={foto}&descripcion={descripcion}&nuevo_nombre={nuevo_nombre}"

    payload = []

    response = client.put(
        url, json=payload, headers={"Content-Type": "application/json"}
    )

    return response


def delete_playlist(name: str):
    response = client.delete(f"/playlists/{name}")
    return response


def get_all_playlists():
    response = client.get(f"/playlists/")
    return response
