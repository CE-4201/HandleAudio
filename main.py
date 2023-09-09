import sendToS3

bucketName = "pre-transcribed-mp3-bucket"
sendToS3Response = sendToS3.uploadToS3("./audioFiles/test.mp3", bucketName, "test.mp3")
