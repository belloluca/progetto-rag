# Esercizio 3 — FastAPI

1. Avvia il backend (vedi README) e apri http://localhost:8000/docs.
   Prova l'endpoint `/health` dall'interfaccia.

2. Esegui i test dalla cartella `backend`:
   ```bash
   pytest
   ```

3. **TODO**: in `app/main.py` aggiungi un endpoint
   `POST /similarity` che riceve:
   ```json
   { "text_a": "...", "text_b": "..." }
   ```
   e restituisce la similarità coseno tra i due testi.
   - Definisci il body con una classe Pydantic (`class SimilarityRequest(BaseModel)`)
   - Riusa le funzioni dell'esercizio 2, spostandole in `app/rag/embeddings.py`

4. **TODO**: aggiungi un test in `tests/` per il nuovo endpoint.

Paragone con Angular: le classi Pydantic sono come le interface TypeScript,
ma i dati vengono anche **validati** a runtime.
