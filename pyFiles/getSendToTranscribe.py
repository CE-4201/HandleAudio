import requests

def fetch(fileName):
    url = f"https://4v5754t3r5.execute-api.us-east-2.amazonaws.com/default/sendToTranscribe?fileName={fileName}"
    sendToTranscribeResponse = requests.get(url)

    if sendToTranscribeResponse.status_code == 200:
        print(sendToTranscribeResponse.json())
    else:
        print(f'Failed to get data: {sendToTranscribeResponse.status_code}')
