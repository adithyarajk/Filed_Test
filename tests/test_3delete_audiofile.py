from AudioFile import app
import tests.audio_file_stub

def test_delete_podcast():
    id = tests.audio_file_stub.podcast['audioFileMetadata']['id']
    response = app.test_client().delete(f"/song/{id}")
    assert response.status_code == 200
def test_delete_song():
    id = tests.audio_file_stub.song['audioFileMetadata']['id']
    response = app.test_client().delete(f"/song/{id}")
    assert response.status_code == 200
def test_delete_audiobook():
    id = tests.audio_file_stub.audiobook['audioFileMetadata']['id']
    response = app.test_client().delete(f"/song/{id}")
    assert response.status_code == 200
