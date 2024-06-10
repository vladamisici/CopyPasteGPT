import openai
import pyperclip
from pynput import keyboard
from dotenv import load_dotenv
import os
import subprocess
import argparse

# Încarcă cheia API din fișierul .env
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

if not api_key:
    print("API key not found in .env file")
    raise ValueError("API key not found in .env file")

openai.api_key = api_key

# Configurarea argumentelor de linie de comandă
parser = argparse.ArgumentParser(description='GPT Copy Paste Script')
parser.add_argument('--stealth', action='store_true', help='Run in stealth mode (no notifications)')
args = parser.parse_args()

# Funcție pentru a trimite întrebarea la GPT-4 și a primi răspunsul
def ask_gpt(question, model="gpt-4-turbo"):
    try:
        response = openai.Completion.create(
            engine=model,
            prompt=question,
            max_tokens=150
        )
        answer = response.choices[0].text.strip()
        return answer
    except openai.error.InvalidRequestError as e:
        if "model" in str(e):
            if model == "gpt-4-turbo":
                return ask_gpt(question, model="gpt-3.5-turbo")
            else:
                if not args.stealth:
                    show_notification("Failed to get response from both GPT-4 and GPT-3.5")
                return None
        else:
            if not args.stealth:
                show_notification(f"Error: {str(e)}")
            return None
    except openai.error.AuthenticationError:
        if not args.stealth:
            show_notification("Incorrect API key")
        return None
    except Exception as e:
        if not args.stealth:
            show_notification(f"Error: {str(e)}")
        return None

# Funcție pentru a afișa o notificare în macOS
def show_notification(message):
    if not args.stealth:
        subprocess.run(['osascript', '-e', f'display notification "{message}" with title "Script"'])

# Funcție care va fi apelată la apăsarea unei taste
def on_press(key):
    try:
        # Verifică dacă Command-C a fost apăsat
        if key == keyboard.Key.cmd and keyboard.is_pressed('c'):
            # Obține textul copiat
            question = pyperclip.paste()
            if question:
                # Trimite întrebarea la GPT-4
                answer = ask_gpt(question)
                if answer:
                    # Pune răspunsul în clipboard
                    pyperclip.copy(answer)
                    # Afișează notificarea
                    if not args.stealth:
                        show_notification("Ready")
            else:
                if not args.stealth:
                    show_notification("Clipboard is empty")

    except AttributeError:
        pass
    except Exception as e:
        if not args.stealth:
            show_notification(f"Error: {str(e)}")

# Ascultă pentru apăsările de taste
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
