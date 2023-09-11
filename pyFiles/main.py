import handleS3
import getSendToTranscribe
import time

bucketName = "pre-transcribed-mp3-bucket"
sendToS3Response = handleS3.uploadToS3('./audioFiles/test1.mp3', bucketName, "test1.mp3")
getSendToTranscribeResponse = getSendToTranscribe.fetch("test1.mp3")
audioLen = handleS3.findAudioLength("test1.mp3")
print("waiting ", audioLen, " seconds")
time.sleep(audioLen)
transcription = handleS3.fetch_transcription("test1.mp3")
print(transcription)




