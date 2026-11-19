# Roadmap — 6 settimane

Ritmo: ~1 ora dal lunedì al venerdì + 3-4 ore nel weekend.

## Settimana 1 — Basi
Obiettivo: capire cos'è un embedding e saper creare un'API in Python.

- [ ] Installare Python, Docker Desktop e Ollama
- [ ] `exercises/01_python_per_js.py` — Python visto da uno sviluppatore JS
- [ ] `exercises/02_embeddings.py` — primi embedding e similarità coseno
- [ ] `exercises/03_fastapi.md` — avviare il backend e aggiungere un endpoint
- [ ] Annotare in `docs/esperimenti.md` cosa hai osservato

✅ Fine settimana: sai spiegare a voce cos'è un embedding e perché due frasi diverse possono essere "vicine".

## Settimana 2 — Indicizzazione
- [ ] `loader.py`: testo dai PDF con numero di pagina
- [ ] `chunking.py`: chunk con overlap, scritto a mano
- [ ] `store.py`: tabella su pgvector, salvataggio e ricerca
- [ ] Endpoint `POST /documents`

## Settimana 3 — Domande e risposte (MVP)
- [ ] `generator.py`: prompt con contesto e citazioni
- [ ] Endpoint `POST /ask`
- [ ] Prime 10 domande di test in `eval/questions.json`

## Settimana 4 — Frontend Angular
- [ ] Upload dei documenti
- [ ] Chat
- [ ] Pannello con le fonti citate

## Settimana 5 — Qualità
- [ ] Ricerca ibrida (parole chiave + semantica)
- [ ] Script di valutazione su `eval/`
- [ ] Confronto tra dimensioni di chunk diverse

## Settimana 6 — Rilascio
- [ ] Provider cloud (Groq/Gemini) al posto di Ollama
- [ ] Deploy
- [ ] README finale con risultati e video demo
