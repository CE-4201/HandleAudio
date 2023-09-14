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

