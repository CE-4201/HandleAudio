import wave
import pyaudio
import keyboard
from dataclasses import dataclass, asdict
from typing import List
import time

@dataclass
class StreamParams:
    format: int = pyaudio.paInt16
    channels: int = 1
    rate: int = 44100
    frames_per_buffer: int = 1024
    input: bool = True
    output: bool = False

    def to_dict(self) -> dict:
        return asdict(self)


class Recorder:
    def __init__(self, stream_params: StreamParams) -> None:
        self.stream_params = stream_params
        self._pyaudio = pyaudio.PyAudio()
        self._stream = self._pyaudio.open(**self.stream_params.to_dict())
        self._frames: List[bytes] = []

    def start_recording(self) -> None:
        print("Start recording...")
        self._frames.clear()

    def stop_recording(self, save_path: str) -> None:
        print("Stop recording")
        self._save_wav_file(save_path)

    def record_chunk(self) -> None:
        audio_data = self._stream.read(self.stream_params.frames_per_buffer)
        self._frames.append(audio_data)

    def _save_wav_file(self, save_path: str) -> None:
        with wave.open(save_path, "wb") as wav_file:
            wav_file.setnchannels(self.stream_params.channels)
            wav_file.setsampwidth(self._pyaudio.get_sample_size(self.stream_params.format))
            wav_file.setframerate(self.stream_params.rate)
            wav_file.writeframes(b"".join(self._frames))

    def close(self) -> None:
        self._stream.close()
        self._pyaudio.terminate()

def main_function(fileName: str):
    stream_params = StreamParams()
    recorder = Recorder(stream_params)
    recording = False
    keep_running = True
    last_keypress_time = 0  # For debouncing the 'd' key
    debounce_interval = 0.5  # 500 milliseconds for the 'd' key

    def start_recording(e):
        nonlocal recording, last_keypress_time
        current_time = time.time()
        if not recording and current_time - last_keypress_time > debounce_interval:
            recorder.start_recording()
            recording = True
            last_keypress_time = current_time

    def stop_recording(e):
        nonlocal recording, keep_running, last_keypress_time
        current_time = time.time()
        if recording and current_time - last_keypress_time > debounce_interval:
            recorder.stop_recording(f"./audioFiles/{fileName}")
            recording = False
            last_keypress_time = current_time
            print("Press 'Enter' to continue.")

    def handle_enter(e):
        nonlocal keep_running
        keep_running = False

    keyboard.on_press_key("d", start_recording)
    keyboard.on_release_key("d", stop_recording)
    keyboard.on_press_key("enter", handle_enter)

    print("Listening for keypresses... Press 'd' to start and stop recording.")

    while keep_running:
        if recording:
            recorder.record_chunk()

    keyboard.unhook_all()  # Remove all keyboard hooks

def createFileName():
    return f"recording_{int(time.time() * 1000)}.wav"
