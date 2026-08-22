import os
from pathlib import Path
from typing import Final

import requests


API_URL: Final = "https://api.publicai.co/v1/chat/completions"
API_KEY: Final = os.getenv("AINA_API_KEY")
MODEL_NAME: Final = "BSC-LT/salamandra-7b-instruct-tools-16k"

ROOT_DIR: Final = Path(__file__).resolve().parents[3]
CONTEXT_FILE: Final = ROOT_DIR / "data" / "context" / "ai" / "el_teu_arxiu.txt"


def main() -> None:
    if not API_KEY:
        raise RuntimeError("No s'ha configurat la variable d'entorn AINA_API_KEY.")

    try:
        context_txt = CONTEXT_FILE.read_text(encoding="utf-8").strip()
    except FileNotFoundError as exc:
        raise RuntimeError(
            f"No s'ha trobat el fitxer de context: {CONTEXT_FILE}"
        ) from exc

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {
                "role": "system",
                "content": (
                    "Ets l'assistent de demostració del projecte d'anàlisi WiFi "
                    "desenvolupat durant UAB THE HACK! 2025. "
                    "Respon en català utilitzant exclusivament les dades sintètiques "
                    "del context proporcionat. No facis afirmacions sobre l'estat real "
                    "de la xarxa WiFi de la UAB ni inventis dades."
                ),
            },
            {
                "role": "user",
                "content": (
                    "Basant-te exclusivament en el següent context, respon la pregunta. "
                    "Si la informació no hi apareix, indica que no està disponible.\n\n"
                    f"--- CONTEXT ---\n{context_txt}\n"
                    "--- PREGUNTA ---\n"
                    "Quin AP fictici té la intensitat mitjana de senyal més baixa?"
                ),
            },
        ],
        "max_tokens": 500,
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    try:
        response = requests.post(
            API_URL,
            headers=headers,
            json=payload,
            timeout=60,
        )
        response.raise_for_status()
    except requests.RequestException as exc:
        raise RuntimeError(
            f"No s'ha pogut contactar amb l'API d'AINA: {exc}"
        ) from exc

    data = response.json()

    try:
        answer = data["choices"][0]["message"]["content"].strip()
    except (KeyError, IndexError, TypeError) as exc:
        raise RuntimeError(
            "La resposta rebuda de l'API d'AINA no té el format esperat."
        ) from exc

    print(answer)


if __name__ == "__main__":
    main()
