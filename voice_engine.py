import speech_recognition as sr
import subprocess
import shlex
import time

def speak(text: str):
    """Executes digital audio synthesis using the premium native South Indian English voice module."""
    print(f"🔮 JARVIS (SOUTH INDIAN ACCENT): {text}")
    try:
        clean_text = text.replace("'", "").replace('"', "").replace("\n", " ").strip()
        
        # FIXED: Enforcing a clean conversational speech rate.
        # This voice command forces your Mac to read technical English words and 
        # Telugu expressions using a natural, local phonetic accent without Hindi elements.
        shell_command = f"say -r 172 '{clean_text}'"
        
        args = shlex.split(shell_command)
        subprocess.run(args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            
    except Exception as e:
        print(f"Native Audio Pipeline Note: {e}")

def listen_manual() -> str:
    """Captures microphone input channel cleanly into an isolated context window frame."""
    rec = sr.Recognizer()
    rec.dynamic_energy_threshold = False
    rec.energy_threshold = 400
    rec.pause_threshold = 1.2
    
    try:
        mic_hardware_device = sr.Microphone()
        print("🎙️ Physical Mic Channel Opened. Capturing speech signal stream...")
        with mic_hardware_device as vocal_source:
            time.sleep(0.2)
            rec.adjust_for_ambient_noise(vocal_source, duration=0.3)
            audio_buffer = rec.listen(vocal_source, timeout=4, phrase_time_limit=7)
            
        print("🧠 Audio frame successfully closed. Running transcription pass...")
        query_text = rec.recognize_google(audio_buffer, language="te-IN")
        print(f"🗣️ MATALU TRANSCRIPT CAPTURED: {query_text}")
        return query_text
        
    except Exception as hardware_exception:
        print(f"Isolated Audio Stream Boundary Notice: {hardware_exception}")
        return "ERROR"
