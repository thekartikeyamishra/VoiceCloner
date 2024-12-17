# VoiceCloner
The Voice Cloner is a Python-based project that leverages Tacotron 2 and WaveGlow models for text-to-speech (TTS) synthesis and basic voice cloning. This project supports 22 official Indian languages, including Sanskrit, making it versatile for multilingual text input.

Here's the **detailed README.md** file for your project:

---

# Voice Cloner Using Audio Synthesis Models 

The **Voice Cloner** is a Python-based project that leverages **Tacotron 2** and **WaveGlow** models for **text-to-speech (TTS) synthesis** and **basic voice cloning**. This project supports **22 official Indian languages**, including **Sanskrit**, making it versatile for multilingual text input.

The project is optimized for CPU usage using **pre-trained models**, enabling developers and enthusiasts to quickly synthesize speech.

---

## **Features**

### 1. **Text-to-Speech Synthesis**
- Generate speech audio for the provided text.
- Supports English and Indian languages such as **Hindi, Bengali, Tamil, Telugu, and Sanskrit**.

### 2. **Basic Voice Cloning**
- Mimics voice patterns and generates audio with similar speech characteristics.

### 3. **CLI-Based Interface**
- User-friendly command-line interface for generating and saving audio files.

---

## **Project Folder Structure**

Below is the organized structure of the project:

```bash
VoiceCloner/
├── data/
│   ├── samples/                  # Sample audio clips for cloning
│   ├── synthesized_audio/        # Directory for storing generated audio
├── models/
│   ├── tacotron2/                # Pre-trained Tacotron 2 model for text-to-mel
│   ├── waveglow/                 # Pre-trained WaveGlow model for audio synthesis
├── utils/
│   ├── __init__.py               # Initializes the utils module
│   ├── text_processing.py        # Cleans and preprocesses input text
│   ├── voice_cloning.py          # Core logic for voice synthesis
│   ├── language_support.py       # Provides support for multiple languages
├── main.py                       # Entry point to run the project
├── requirements.txt              # Project dependencies
├── LICENSE                       # License information
└── README.md                     # Detailed documentation (this file)
```

---

## **Installation Instructions**

Follow these steps to set up and run the project on your local machine:

### **1. Clone the Repository**
```bash
git clone https://github.com/thekartikeyamishra/VoiceCloner.git
cd VoiceCloner
```

### **2. Set Up the Environment**
Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate    # On Windows: .venv\Scripts\activate
```

### **3. Install Dependencies**
Install the required libraries:
```bash
pip install -r requirements.txt
```

### **4. Run the Application**
Execute the CLI application:
```bash
python main.py
```

---

## **How It Works**

1. **Text Input**: Enter any text and choose the desired language (supports 22 languages).
2. **Speech Synthesis**: The text is processed using **Tacotron 2** and converted into mel spectrograms.
3. **Audio Generation**: The **WaveGlow** vocoder generates high-quality audio from the mel spectrogram.
4. **Save Output**: The generated audio is saved in the `data/synthesized_audio/` directory as a `.wav` file.

---

## **Dependencies**

The project requires the following Python libraries:

```plaintext
torch
numpy
librosa
```

Install these dependencies using the provided `requirements.txt`.

---

## **Supported Languages**

The following languages are currently supported:

- **English**  
- **Hindi**  
- **Bengali**  
- **Tamil**  
- **Telugu**  
- **Gujarati**  
- **Malayalam**  
- **Marathi**  
- **Kannada**  
- **Punjabi**  
- **Odia**  
- **Assamese**  
- **Urdu**  
- **Sindhi**  
- **Sanskrit**  

Additional languages can be added in the future with phonetic support.

---

## **Future Enhancements**

This is the **basic version** of the Voice Cloner. Future plans include:

1. **GUI Support**: A graphical interface for ease of use.
2. **Advanced Voice Cloning**: Speaker embedding for personalized voice synthesis.
3. **Support for Additional Models**: Integration with **FastSpeech** and other synthesis models.
4. **Multi-Language Extensions**: Support for more global languages.

---

## **Contributions**

Contributions are welcome! Feel free to:
1. **Fork the Repository**.
2. Create a **Feature Branch**.
3. Submit a **Pull Request** with your improvements.

---

## **Contact**

If you have any questions, feedback, or suggestions, feel free to reach out!

---

Let’s bring multilingual speech synthesis to the next level. 🚀  
**Star ⭐ the project if you find it useful!**

```bash
git clone https://github.com/thekartikeyamishra/VoiceCloner.git
```

---

