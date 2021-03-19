from AudioFile import app
import tests.audio_file_stub

def test_read_audiobook():
    data = tests.audio_file_stub.audiobook['audioFileMetadata']['id']
    response = app.test_client().get(f"/audiobook/{data}")
    assert response.status_code == 200

def test_read_podcast():
    data = tests.audio_file_stub.podcast['audioFileMetadata']['id']
    response = app.test_client().get(f"/podcast/{data}")
    assert response.status_code == 200
def test_read_song():
    data = tests.audio_file_stub.song['audioFileMetadata']['id']
    response = app.test_client().get(f"/song/{data}")
    assert response.status_code == 200
