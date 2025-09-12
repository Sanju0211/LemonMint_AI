import logging
from fastrtc import ReplyOnPause, Stream, get_stt_model, get_tts_model
from ollama import chat

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Initialize models
stt_model = get_stt_model()  # Default: moonshine/base
tts_model = get_tts_model()  # Default: kokoro


def echo(audio):
    """
    Handles incoming audio:
    1. Converts audio -> text (STT).
    2. Sends text to LLM (Ollama chat).
    3. Converts response -> audio (TTS).
    Also prints conversation logs to console.
    """
    try:
        # Step 1: Speech-to-Text
        transcript = stt_model.stt(audio)

        if not transcript.strip():
            logging.warning("Empty transcript received. Skipping response.")
            return

        # Print transcript to console (conversation log)
        print(f"\n🧑 You: {transcript}")

        # Step 2: Query Ollama Chat
        response = chat(
            model="gemma3:1b",
            messages=[{"role": "user", "content": transcript}],
        )
        response_text = response["message"]["content"].strip()

        # Print LLM response to console (conversation log)
        print(f"🤖 Bot: {response_text}")

        # Step 3: Text-to-Speech (Streamed)
        for audio_chunk in tts_model.stream_tts_sync(response_text):
            yield audio_chunk

    except Exception as e:
        logging.error(f"Error in echo function: {e}")
        return


if __name__ == "__main__":
    try:
        # Setup FastRTC stream
        stream = Stream(
            ReplyOnPause(echo),
            modality="audio",
            mode="send-receive"
        )
        logging.info("Launching FastRTC audio stream UI...")
        stream.ui.launch()
    except KeyboardInterrupt:
        logging.info("Application stopped by user.")
    except Exception as e:
        logging.error(f"Failed to launch stream: {e}")

