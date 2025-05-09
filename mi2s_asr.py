import base64
import requests

import threading
import pyaudio
import wave
import sys
import cv2
from aiy.voice.audio import play_wav


class Recorder:
    def __init__(self):
        self.recording = False

    def start_recording(self):
        sample_format = pyaudio.paInt16
        channels = 1
        sample_rate = 16000
        chunk = 1024
        self.output_file = "audio.wav"

        self.audio = pyaudio.PyAudio()

        self.stream = self.audio.open(format=sample_format,
                                      channels=channels,
                                      rate=sample_rate,
                                      input=True,
                                      frames_per_buffer=chunk)

        self.frames = []

        self.recording = True
        print("Recording... Press Enter to stop.")

        while self.recording:
            data = self.stream.read(chunk)
            self.frames.append(data)

        self.stop_recording()

    def stop_recording(self):
        print("Recording finished.")
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()

        # Save the recorded audio
        with wave.open(self.output_file, 'wb') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(self.audio.get_sample_size(pyaudio.paInt16))
            wf.setframerate(16000)
            wf.writeframes(b''.join(self.frames))
        
        print(f"Audio saved as {self.output_file}")

    def record(self):
        self.recording = True
        record_thread = threading.Thread(target=self.start_recording)
        record_thread.start()
        play_wav("start.wav")
        # while self.recording:
        cv2.waitKey(3000)  # 處理一次 GUI 事件、並回傳 keycode
        #     if key == ord('s'):    # 使用者在 OpenCV 視窗按下 s
        self.recording = False
        # input()  # Wait for the user to press Enter
        record_thread.join()


def main():
    url = 'http://140.116.245.149:5002/proxy'
    file_path = 'audio.wav' 

    with open(file_path, 'rb') as file:
        raw_audio = file.read()

        audio_data = base64.b64encode(raw_audio)
        data = {
            'lang': 'STT for course',
            'token': '2025@ME@asr',
            'audio': audio_data.decode()
        }
        response = requests.post(url, data=data)

    if response.status_code == 200:
        data = response.json()
        print(f"辨識结果: {data['sentence']}")
        return data['sentence']
    else:
        data = response.json()
        print(data)
        print(f"錯誤信息: {data['error']}")

if __name__ == '__main__':
    main()
