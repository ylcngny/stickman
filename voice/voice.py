from transformers import VitsModel, AutoTokenizer
import torch
import torchaudio


# https://huggingface.co/facebook/mms-tts-eng
class VoiceHandler:
    def __init__(self):
        pass

    def create(self, text):
        # Load model and tokenizer
        model_name = "facebook/mms-tts-eng"
        model = VitsModel.from_pretrained(model_name)
        tokenizer = AutoTokenizer.from_pretrained(model_name)

        # Tokenize and prepare inputs
        inputs = tokenizer(text, return_tensors="pt")

        # Generate waveform
        with torch.no_grad():
            outputs = model(**inputs)
            if hasattr(outputs, "waveform"):
                output_waveform = outputs.waveform
            else:
                raise AttributeError("The model does not have a 'waveform' attribute.")

        # Define output file path
        output_file = "./voice/voice.wav"

        # Save waveform as audio file
        torchaudio.save(output_file, output_waveform.cpu(), 16000)

        print(f"Audio waveform saved as '{output_file}'")
