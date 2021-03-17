
from AudioFile.Model import Song, Audiobook, Podcast

class AudioFileFactory:

    @classmethod
    def createAudioFile(cls, audioFileType, audioFileMetadata) -> object:
        if audioFileType == 'song':
            return Song.createSong(audioFileMetadata)
        if audioFileType == 'audiobook':
            return Audiobook.createAudioBook(audioFileMetadata)
        if audioFileType == 'podcast':
            return Podcast.createPodcast(audioFileMetadata)

    @classmethod
    def getAudioFileByID(cls, audioFileType, audioFileID):
        if audioFileType == 'song':
            return Song.query.filter_by(id=int(audioFileID))
        if audioFileType == 'audiobook':
            return Audiobook.query.filter_by(id=audioFileID)
        if audioFileType == 'podcast':
            return Podcast.query.filter_by(id=audioFileID)

    @classmethod
    def updateAudioFile(cls, audioFileType, audioFileID, audioFileMetadata):
        if audioFileType == 'song':
            Song.updateSong(audioFileID, audioFileMetadata)
        if audioFileType == 'audiobook':
            Audiobook.updateAudioBook(audioFileID, audioFileMetadata)
        if audioFileType == 'podcast':
            Podcast.updatePodcast(audioFileID, audioFileMetadata)

    @classmethod
    def getAllAudioFiles(cls, audioFileType):
        if audioFileType == 'song':
            allAudioFile = Song.query.all()
        if audioFileType == 'audiobook':
            allAudioFile = Audiobook.query.all()
        if audioFileType == 'podcast':
            allAudioFile = Podcast.query.all()
        return allAudioFile