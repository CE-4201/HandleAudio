import sendToS3

bucketName = "base64-mp3-files-bucket"
sendToS3Response = sendToS3.uploadToS3("./audioFiles/test.mp3", bucketName, "test.mp3")
