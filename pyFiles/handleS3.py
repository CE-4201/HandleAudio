import boto3
from mutagen.mp3 import AudioSegment

s3 = boto3.client('s3')

def uploadToS3(file_path, bucket, fileName):
    s3.upload_file(file_path, bucket, fileName)
    print(f"Successfully uploaded {fileName} to {bucket}.")

def findAudioLength(fileName) :
    audio = AudioSegment.from_file(f"./audioFiles/{fileName}")
    length_in_miliseconds = len(audio)
    return length_in_miliseconds + 2000