# GPT Copy Paste

Trimite automat intrebarile copiate la GPT-4 si copiaza raspunsurile in clipboard.

## Instalare

1. Clonează acest repository:

    ```sh
    git clone https://github.com/vladamisici/CopyPasteGPT
    cd gpt_copy_paste
    ```

2. Creează un fișier `.env` și adaugă cheia ta API OpenAI:
    https://platform.openai.com/api-keys

    ```sh
    echo "OPENAI_API_KEY=your_openai_api_key_here" > .env
    ```

3. Rulează scriptul de instalare:

    ```sh
    chmod +x installer.sh
    ./installer.sh
    ```

4. Activează mediul virtual și rulează scriptul principal:

    ```sh
    source venv/bin/activate
    python main.py
    ```

## Utilizare

Apasă Command-C pentru a copia o întrebare și Command-V pentru a lipi răspunsul generat de GPT-4.
