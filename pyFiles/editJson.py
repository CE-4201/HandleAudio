import json
import os

def write_message_to_json(msg_type, msg_content):
    json_file_path = "../frontend/assets/messages.json"
    messages = []

    if os.path.exists(json_file_path):
        with open(json_file_path, 'r') as f:
            messages = json.load(f)

    new_entry = {"type": msg_type, "message": msg_content}
    messages.append(new_entry)

    with open(json_file_path, 'w') as f:
        json.dump(messages, f)

def clear_messages_json():
    file_path = "../frontend/assets/messages.json"
    with open(file_path, 'w') as f:
        json.dump([], f)
        print("messages.json cleared")

def delete_all_files_in_audioFiles():
    directory = "./audioFiles"
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")


