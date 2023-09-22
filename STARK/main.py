# 1
import anyio
from stark import run, CommandsManager, Response
from stark.interfaces.vosk import VoskSpeechRecognizer
from stark.interfaces.silero import SileroSpeechSynthesizer

# 2
VOSK_MODEL_URL = 'https://alphacephei.com/vosk/models/vosk-model-small-ru-0.22.zip'
SILERO_MODEL_URL = 'https://models.silero.ai/models/tts/ru/ru_v3.pt'

# 3
recognizer = VoskSpeechRecognizer(model_url=VOSK_MODEL_URL)
synthesizer = SileroSpeechSynthesizer(model_url=SILERO_MODEL_URL)
manager = CommandsManager()

# 4
@manager.new('привет')
def hello_command() -> Response:
    text = voice = 'Привет, мир!'
    return Response(text=text, voice=voice)

# 5
async def main():
    await run(manager, recognizer, synthesizer)

if __name__ == '__main__':
    anyio.run(main)