import torch
from TTS.api import TTS


class TextToSpeech:
    def __init__(self, model_path="tts_models/multilingual/multi-dataset/xtts_v2", device=None):
        self.device = device if device else self.get_device()
        self.tts = self.init_tts(model_path, self.device)

    def init_tts(self, model_path, device):
        # Initialize the TTS model 
        tts = TTS(model_path, gpu=device == "cuda")
        return tts

    def get_device(self):
        return "cuda" if torch.cuda.is_available() else "cpu"


    def run_tts(self, text, speaker_wav, language, file_path=None):
        if file_path:
            self.tts.tts_to_file(text=text, speaker_wav=speaker_wav, language=language, file_path=file_path, speed=1.5)  
        else:
            return self.tts.tts(text=text, speaker_wav=speaker_wav, language=language, speed=1.5)  # And here
