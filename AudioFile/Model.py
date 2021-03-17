from AudioFile import db
from datetime import datetime


class Podcast(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    uploaded_time = db.Column(db.DateTime, default=datetime.utcnow)
    host = db.Column(db.String(100), nullable=False)
    participant1 = db.Column(db.String(100), nullable=True)
    participant2 = db.Column(db.String(100), nullable=True)
    participant3 = db.Column(db.String(100), nullable=True)
    participant4 = db.Column(db.String(100), nullable=True)
    participant5 = db.Column(db.String(100), nullable=True)
    participant6 = db.Column(db.String(100), nullable=True)
    participant7 = db.Column(db.String(100), nullable=True)
    participant8 = db.Column(db.String(100), nullable=True)
    participant9 = db.Column(db.String(100), nullable=True)
    participant10 = db.Column(db.String(100), nullable=True)

    def __repr__(self) -> str:
        return f"{self.id} - {self.name}"

    @classmethod
    def createPodcast(cls, podcast):

        return Podcast(id=podcast['id'], name=podcast['name'], duration=podcast['duration'], host=podcast['host'],
                       participant1= podcast.get('participant1'),
                       participant2=podcast.get('participant2'),
                       participant3=podcast.get('participant3'),
                       participant4=podcast.get('participant4'),
                       participant5=podcast.get('participant5'),
                       participant6=podcast.get('participant6'),
                       participant7=podcast.get('participant7'),
                       participant8=podcast.get('participant8'),
                       participant9=podcast.get('participant9'),
                       participant10=podcast.get('participant10'),
                       )

    @classmethod
    def updatePodcast(cls, audioFileID, audioFileMetadata):
        Podcast.query.filter_by(id=audioFileID).first().delete()
        db.session.add(Podcast.createPodcast(audioFileMetadata))
        db.session.commmit()

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'duration': self.duration,
            'upload_time': self.uploaded_time,
            'host': self.host,
            'participant1': self.participant1,
            'participant2': self.participant2,
            'participant3': self.participant3,
            'participant4': self.participant4,
            'participant5': self.participant5,
            'participant6': self.participant6,
            'participant7': self.participant7,
            'participant8': self.participant8,
            'participant9': self.participant9,
            'participant10': self.participant10,
        }


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    uploaded_time = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.id} - {self.name}"

    @classmethod
    def createSong(cls, song):
        return Song(id=song['id'], name=song['name'], duration=song['duration'])

    @classmethod
    def updateSong(cls,audioFileID, audioFileMetadata):
        Song.query.filter_by(id=audioFileID).first().delete()
        db.session.add(Song.createSong(audioFileMetadata))
        db.session.commit()

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'duration': self.duration,
            'upload_time': self.uploaded_time,
        }

class Audiobook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    narrator = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    uploaded_time = db.Column(db.Integer, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.id} - {self.name}"

    @classmethod
    def createAudioBook(cls, request):
        song = request
        return Audiobook(id=song['id'], name=song['name'], duration=song['duration'], author=song['author'],
                         narrator=song['narrator'])

    @classmethod
    def updateAudioBook(cls, audioFileID, audioFileMetadata):
        Audiobook.query.filter_by(id=audioFileID).first().delete()
        db.session.add(Audiobook.createAudioBook(audioFileMetadata))
        db.session.commit()

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'author': self.author,
            'narrator': self.narrator,
            'duration': self.duration,
            'upload_time': self.uploaded_time,
        }