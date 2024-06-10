import openai
import pyperclip
from pynput import keyboard
from dotenv import load_dotenv
import os
import subprocess

# Încarcă cheia API din fișierul .env
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

if not api_key:
    subprocess.run(['osascript', '-e', 'display notification "API key not found in .env file" with title "Script"'])
    raise ValueError("API key not found in .env file")

openai.api_key = api_key

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
                show_notification("Failed to get response from both GPT-4 and GPT-3.5")
                return None
        else:
            show_notification(f"Error: {str(e)}")
            return None
    except openai.error.AuthenticationError:
        show_notification("Incorrect API key")
        return None
    except Exception as e:
        show_notification(f"Error: {str(e)}")
        return None

# Funcție pentru a afișa o notificare în macOS
def show_notification(message):
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
                    show_notification("Ready")
            else:
                show_notification("Clipboard is empty")

    except AttributeError:
        pass
    except Exception as e:
        show_notification(f"Error: {str(e)}")

# Ascultă pentru apăsările de taste
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
