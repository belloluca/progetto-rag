"""
Esercizio 2 — I primi embedding
Prerequisiti: Ollama avviato e `ollama pull nomic-embed-text`
Esegui dalla cartella backend (con il venv attivo):
    python ../exercises/02_embeddings.py

Obiettivo: capire che frasi con significato simile hanno vettori "vicini",
anche quando usano parole diverse. È la base di tutto il RAG.
"""
import httpx
import numpy as np

OLLAMA_URL = "http://localhost:11434"
MODEL = "nomic-embed-text"


def embed(text: str) -> list[float]:
    """TODO 1: chiama Ollama e restituisci il vettore del testo.

    Endpoint: POST {OLLAMA_URL}/api/embed
    Body JSON: {"model": MODEL, "input": text}
    La risposta ha la forma {"embeddings": [[...numeri...]]}
    Suggerimento: httpx.post(url, json=..., timeout=30).json()
    """
    pass


def cosine_similarity(a: list[float], b: list[float]) -> float:
    """TODO 2: similarità coseno tra due vettori.

    Formula: (a · b) / (|a| * |b|)
    Con numpy: np.dot(a, b) e np.linalg.norm(a)
    Risultato vicino a 1 = significato simile, vicino a 0 = non correlati.
    """
    pass


if __name__ == "__main__":
    question = "Come posso restituire un prodotto difettoso?"
    sentences = [
        "Il reso degli articoli danneggiati è gratuito entro 30 giorni.",
        "La garanzia copre i difetti di fabbricazione per 24 mesi.",
        "Il nostro negozio è aperto dal lunedì al sabato.",
        "La pizza margherita ha pomodoro, mozzarella e basilico.",
    ]

    # TODO 3: calcola l'embedding della domanda e di ogni frase,
    # poi stampa le frasi ordinate dalla più simile alla meno simile,
    # con il punteggio accanto.

    # TODO 4 (riflessione): la prima frase non contiene la parola "restituire",
    # eppure dovrebbe risultare la più simile. Perché?
    # Scrivi la risposta in docs/esperimenti.md.

    vector = embed(question)
    if vector:
        print(f"Dimensioni del vettore: {len(vector)}")
