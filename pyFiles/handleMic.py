import wave
import pyaudio
import keyboard
from dataclasses import dataclass, asdict
from typing import List
import time

@dataclass
class StreamParams:
    format: int = pyaudio.paInt16
    channels: int = 2
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
    recording = False  # Flag for recording state
    keep_running = True  # Flag for loop control

    def start_recording(e):
        nonlocal recording
        if not recording:
            recorder.start_recording()
            recording = True

    def stop_recording(e):
        nonlocal recording, keep_running
        if recording:
            recorder.stop_recording(f"./audioFiles/{fileName}")
            recording = False
            print("Press 'Enter' to continue.")  # Prompt user
            input()  # Wait for Enter key
            keep_running = False  # Set this flag to False to end the loop

    keyboard.on_press_key("d", start_recording)
    keyboard.on_release_key("d", stop_recording)

    print("Listening for keypresses... Press 'd' to start and stop recording.")

    while keep_running:  # Use the flag here
        if recording:
            recorder.record_chunk()

def createFileName():
    return f"recording_{int(time.time() * 1000)}.wav"
