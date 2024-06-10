# GPT Copy Paste

Trimite automat întrebarile copiate la GPT-4 și copiază răspunsurile în clipboard.

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

### Mod Notificări

Implicit, scriptul va afișa notificări în colțul din dreapta sus al ecranului pentru a te informa despre diverse stări, cum ar fi:
- Când răspunsul este gata și a fost copiat în clipboard ("Ready").
- Dacă există probleme cu cheia API ("Incorrect API key").
- Alte erori care ar putea apărea.

### Mod Stealth

Pentru a rula scriptul în modul stealth (fără notificări), folosește următoarea comandă:

```sh
python main.py --stealth
