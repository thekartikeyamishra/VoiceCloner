import os
import torch
from utils.voice_cloning import load_models, synthesize_speech
from utils.language_support import LANGUAGES, get_language_code


def save_audio(audio, filepath):
    torch.save(audio, filepath)


def main():
    print("Voice Cleaner - Text-to-Speech Synthesis")
    print("Supported Languages:")
    for code, name in LANGUAGES.items():
        print(f"{code}:{name}")

    # Loading Model
    tacotron2, waveglow = load_models()

    # Input text & language

    text = input("Enter the text to synthesize: ")
    language_name = input(
        "Enter the language (eg: Sanskrit, Hindi, English or any 22 official languages of Bharat(India) :")
    language_code = get_language_code(language_name)

    # Synthesize speech

    audio = synthesize_speech(text, tacotron2, waveglow, language=language_code)
    output_path = "data/synthesized_audio/synthesized_speech.wav"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    save_audio(audio, output_path)

    print(f"Audio saved at : {output_path}")


if __name__ == "__main__":
    main()
