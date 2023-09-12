import requests
from urllib.parse import quote

def fetch(fileName):
    url = f"https://4v5754t3r5.execute-api.us-east-2.amazonaws.com/default/sendToTranscribe?fileName={fileName}"
    sendToTranscribeResponse = requests.get(url)

    if sendToTranscribeResponse.status_code == 200:
        response_json = sendToTranscribeResponse.json()
        return response_json['transcriptionJobName']
    else:
        print(f'Failed to get data: {sendToTranscribeResponse.status_code}')
        return None

def fetchChatGPT(prompt):
    encoded_prompt = quote(prompt)
    url = f"https://f7l4hrm11h.execute-api.us-east-2.amazonaws.com/default/communicateChatGPTAPI?transcribedData={encoded_prompt}"
    chatGPTResponse = requests.get(url)

    if chatGPTResponse.status_code == 200:
        return chatGPTResponse.json()
    else:
        print(f'Failed to get data: {chatGPTResponse.status_code}')
        return None
