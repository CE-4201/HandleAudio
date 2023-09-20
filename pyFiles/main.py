import handleS3
import getSendToTranscribe
import time
import editJson
import handleMic

while True:
    fileName = handleMic.createFileName()
    print(fileName)
    handleMic.main_function(fileName)

    bucketName = "pre-transcribed-mp3-bucket"
    sendToS3Response = handleS3.uploadToS3(f'./audioFiles/{fileName}', bucketName, fileName)

    getSendToTranscribeResponse = getSendToTranscribe.fetch(fileName)
    print(f"Send to Transcribe Lambda: Transcription Job {getSendToTranscribeResponse} sent")

    audioLen = handleS3.findAudioLength(fileName)
    print("S3 Retrieval: Waiting", audioLen, "seconds")
    time.sleep(audioLen)

    transcription = handleS3.fetch_transcription(getSendToTranscribeResponse)
    editJson.write_message_to_json("transcribed", transcription)
    print(f"Input: {transcription}")

    chatGPT = getSendToTranscribe.fetchChatGPT(transcription)
    editJson.write_message_to_json("recieved", chatGPT)
    print(f"Output: {chatGPT}")
