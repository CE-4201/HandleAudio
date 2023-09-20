import boto3
import wave
import json
import time

s3 = boto3.client('s3')

def uploadToS3(file_path, bucket, fileName):
    s3.upload_file(file_path, bucket, fileName)
    print(f"S3 Upload: Successfully uploaded {fileName} to {bucket}.")

def findAudioLength(fileName):
    with wave.open(f"./audioFiles/{fileName}", "rb") as wav_file:
        frames = wav_file.getnframes()
        rate = wav_file.getframerate()
        audioLength = frames / float(rate)
    return audioLength

def fetch_transcription(fileName, retry_count=3):
    s3_client = boto3.client('s3')
    bucket_name = 'transcribe-text-output-bucket'
    object_key = f"{fileName}.json"

    for _ in range(retry_count):
        print(f"S3 Retrieval: Retrieving {object_key} from {bucket_name}")
        try:
            s3_response_object = s3_client.get_object(Bucket=bucket_name, Key=object_key)
            response_content = s3_response_object['Body'].read().decode('utf-8')

            json_content = json.loads(response_content)
            transcript_text = json_content['results']['transcripts'][0]['transcript']

            return transcript_text

        except Exception as e:
            print(f"S3 Retrieval: An error occurred: {e}")
            print("S3 Retrieval: Retrying in 3 seconds")
            time.sleep(3)

    return None

