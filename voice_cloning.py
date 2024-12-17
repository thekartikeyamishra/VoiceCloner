import torch
from utils.text_processing import clean_text


def load_models():
    tecotron2 = torch.hub.load("nvidia/DeepLearningExamples:torchhub", "nvidia_tacotron2")
    waveglow = torch.hub.load("nvidia/DeepLearningExamples:torchhub", "nvidia_waveglow")
    waveglow.eval()
    return tecotron2, waveglow


def synthesize_speech(text, tecotron2, waveglow, language="en"):
    text = clean_text(text, language)
    sequence = tecotron2.text_to_sequence(text, ["english_cleaner"])
    with torch.no_grad():
        mel_output, mel_output_postnet, _, _ = tecotron2.infer(sequence)
        audio = waveglow.infer(mel_output_postnet)

    return audio
