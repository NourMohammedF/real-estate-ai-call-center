import os
import pyaudio
import wave
import stt
import llm
from tts import TextToSpeech

AUDIO_INPUT = "audio/input/customer.wav"
AUDIO_OUTPUT = "audio/output/response.wav"

def record_audio(output_path, duration=5, rate=16000):
    """
    تسجيل صوت العميل.
    """
    chunk = 1024
    channels = 1
    format = pyaudio.paInt16

    audio = pyaudio.PyAudio()
    stream = audio.open(format=format, channels=channels, rate=rate, input=True, frames_per_buffer=chunk)

    print("🎤 تسجيل الصوت...")

    frames = []
    for _ in range(0, int(rate / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    audio.terminate()

    with wave.open(output_path, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(audio.get_sample_size(format))
        wf.setframerate(rate)
        wf.writeframes(b''.join(frames))

    print("✅ تم حفظ التسجيل:", output_path)

def run_call():
    """
    تشغيل المكالمة بالكامل.
    """
    # تهيئة محول النص إلى كلام
    tts = TextToSpeech()
    
    # بدء الاستماع المستمر
    stt.listen_continuously()

if __name__ == "__main__":
    run_call()
