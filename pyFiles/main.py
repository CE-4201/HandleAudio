import handleS3
import getSendToTranscribe
import time

bucketName = "pre-transcribed-mp3-bucket"
fileName = "yisakgit .mp3"
sendToS3Response = handleS3.uploadToS3(f'./audioFiles/{fileName}', bucketName, fileName)
getSendToTranscribeResponse = getSendToTranscribe.fetch(fileName)
print(f"Send to Transcribe Lambda: Transcription Job {getSendToTranscribeResponse} sent")
audioLen = handleS3.findAudioLength(fileName)
print("S3 Retrieval: Waiting", audioLen, "seconds")
time.sleep(audioLen)
transcription = handleS3.fetch_transcription(getSendToTranscribeResponse)
print(transcription)