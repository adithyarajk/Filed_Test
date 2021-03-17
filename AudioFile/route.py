from flask import request, Response, jsonify
from AudioFile import db, app
from AudioFile.AudioFileFactory import AudioFileFactory

@app.route('/', methods=['POST'])
def create_audio_file():
    if request.method == 'POST':
        try:
            audioFileType = request.json['audioFileType']
            audioFileMetadata = request.json['audioFileMetadata']
            audioFile = AudioFileFactory.createAudioFile(audioFileType, audioFileMetadata)
            db.session.add(audioFile)
            db.session.commit()
            return Response(status=200)
        except Exception as error:
            return Response(status=500)

@app.route('/<audioFileType>/<int:audioFileID>', methods= ['DELETE'])
def delete_audio_file(audioFileType, audioFileID):
    if request.method == 'DELETE':
        try:
            if AudioFileFactory.getAudioFileByID(audioFileType, audioFileID).delete() == True:
                db.session.commit()
                return Response(status=200)
        except Exception as error:
            return Response(status=500)

@app.route('/<audioFileType>/<int:audioFileID>', methods=['PATCH'])
def update_audio_file(audioFileType, audioFileID):
    if request.method == 'PATCH':
        try:
            audioFileMetadata = request.json
            AudioFileFactory.updateAudioFile(audioFileType, audioFileID, audioFileMetadata)
            return Response(status=200)
        except Exception as error:
            return Response(status=500)


@app.route('/<audioFileType>/<int:audioFileID>', methods=['GET'])
def get_audio_file(audioFileType, audioFileID):
    if request.method == 'GET':
        try:
            audioFile = AudioFileFactory.getAudioFileByID(audioFileType, audioFileID).first()
            return jsonify(audioFile)
        except Exception as error:
            return Response(status=500)

@app.route('/<audioFileType>', methods= ['GET'])
def get_all_audio_file(audioFileType):
    if request.method == 'GET':
        try:
            return jsonify([i.serialize for i in AudioFileFactory.getAllAudioFiles(audioFileType)]), 200
        except Exception as error:
            return Response(status=500)
