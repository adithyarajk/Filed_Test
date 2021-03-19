from AudioFile import app
import pytest

@pytest.mark.run(order=11)
def test_GetAllAudioBook():
    response = app.test_client().get('/audiobook')
    assert type(response.json) == list
    for response_item in response.json:
        for key, value in response_item.items():
            assert key in ['id', 'name', 'duration','author','narrator', 'upload_time']
            if key in ['name', 'author', 'narrator'] :
                assert type(value) == str
            elif key == ['id', 'duration' ]:
                assert type(value) == int

@pytest.mark.run(order=12)
def testGetAllSongFile():
    response = app.test_client().get('/song')
    assert response.status_code == 200
    assert type(response.json) == list
    for response_item in response.json:
        for key, value in response_item.items():
            assert key in ['id', 'name', 'duration', 'upload_time']
            if key in ['id', 'duration']:
                assert type(value) == int
            elif key == 'name':
                assert  type(value) == str

@pytest.mark.run(order=13)
def test_GetAllPodcast():

    response = app.test_client().get('/podcast')
    assert type(response.json) == list
    for response_item in response.json:
        for key, value in response_item.items():
            assert key in ['id', 'name', 'duration', 'host', 'upload_time', 'participant1', 'participant2', 'participant3', 'participant4', 'participant5', 'participant6', 'participant7', 'participant8', 'participant9', 'participant10']
            if key in ['author',  'participant1' 'participant2', 'participant3', 'participant4', 'participant5', 'participant6', 'participant7', 'participant8', 'participant9', 'participant10'] :
                if value != None:
                    assert type(value) == str
            elif key in ['id', 'duration']:
                assert type(value) == int
