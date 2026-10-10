# Real Estate AI Call Center

AI-powered call center system for real estate businesses. Handles inbound/outbound calls with speech-to-text, LLM processing, and text-to-speech.

## Features

- **Speech-to-Text**: Real-time transcription using Whisper
- **LLM Processing**: Intelligent response generation with Mistral
- **Text-to-Speech**: Natural voice synthesis
- **Call Handling**: Automated call routing and management
- **Multi-language Support**: Arabic and English

## Architecture

```
Audio Input → STT (Whisper) → LLM (Mistral) → TTS → Audio Output
```

## Components

| Module | Description |
|--------|-------------|
| `main.py` | Main entry point |
| `scripts/stt.py` | Speech-to-text with Whisper |
| `scripts/llm.py` | LLM integration |
| `scripts/tts.py` | Text-to-speech |
| `scripts/call_handler.py` | Call flow management |
| `scripts/gui.py` | Desktop interface |

## Setup

1. Create virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # or .venv\Scripts\activate on Windows
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download models (Whisper, Mistral, TTS) - place in `models/` folder

4. Run:
   ```bash
   python main.py
   ```

## Configuration

Edit `config/` files for:
- Model paths
- Audio device settings
- LLM parameters
- Voice settings

## Requirements

- Python 3.10+
- CUDA-compatible GPU (recommended)
- Microphone and speakers

## License

MIT