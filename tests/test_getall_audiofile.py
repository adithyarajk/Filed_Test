from AudioFile import app


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