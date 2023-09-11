import boto3
from mutagen.mp3 import MP3
import json

s3 = boto3.client('s3')

def uploadToS3(file_path, bucket, fileName):
    s3.upload_file(file_path, bucket, fileName)
    print(f"Successfully uploaded {fileName} to {bucket}.")

def findAudioLength(fileName) :
    audio = MP3(f"./audioFiles/{fileName}")
    audioLength = audio.info.length
    return audioLength + 3

def fetch_transcription(fileName):
    s3_client = boto3.client('s3')
    bucket_name = 'transcribe-text-output-bucket'
    object_key = f'Transcribe-{fileName}.json'

    try:
        s3_response_object = s3_client.get_object(Bucket=bucket_name, Key=object_key)
        response_content = s3_response_object['Body'].read().decode('utf-8')

        json_content = json.loads(response_content)
        transcript_text = json_content['results']['transcripts'][0]['transcript']

        return transcript_text

    except Exception as e:
        print(f"An error occurred: {e}")
        return None