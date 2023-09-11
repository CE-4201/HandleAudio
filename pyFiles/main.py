import handleS3
import getSendToTranscribe

bucketName = "pre-transcribed-mp3-bucket"
# sendToS3Response = handleS3.uploadToS3('./audioFiles/test.mp3', bucketName, "test.mp3")
# getSendToTranscribeResponse = getSendToTranscribe.fetch("test.mp3")
handleS3.findAudioLength("test.mp3")



