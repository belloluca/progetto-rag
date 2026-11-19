from fastapi import FastAPI

from app.config import settings

app = FastAPI(title="Progetto RAG", version="0.1.0")


@app.get("/health")
def health():
    """Verifica che l'API sia attiva."""
    return {"status": "ok", "embedding_model": settings.embedding_model}


# Prossimi endpoint (settimane 2-3):
# POST /documents  -> carica un PDF e lo indicizza
# GET  /documents  -> elenco dei documenti caricati
# POST /ask        -> fa una domanda e riceve risposta + fonti
