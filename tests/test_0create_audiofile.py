from AudioFile import app
import tests.audio_file_stub

def test_create_audiobook():

    data = tests.audio_file_stub.audiobook
    response = app.test_client().post('/', json=data)
    assert response.status_code == 200
