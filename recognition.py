import speech_recognition as sr
from pydub import AudioSegment
import whisper
import io
import warnings

rec = sr.Recognizer()

model = whisper.load_model("small.en")

with sr.Microphone() as source:
    print("Calibrating for ambient noise...")
    rec.adjust_for_ambient_noise(source)
    print("Calibration completed. Speak now.")

with sr.Microphone() as source:
    audio = rec.listen(source, phrase_time_limit=10)

audio_data = audio.get_wav_data()
audio_file = io.BytesIO(audio_data)
audio_segment = AudioSegment.from_file(audio_file, format="wav")
audio_segment.export("output.flac", format="flac")

flac_file = "output.flac"
wav_file = "output.wav"
audio = AudioSegment.from_file(flac_file, format="flac")
audio.export(wav_file, format="wav")

with warnings.catch_warnings():
    warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead")
    tran = model.transcribe(wav_file)
    # testing if the transcription works
    print(tran["text"])
