# 📚 Progetto RAG — Assistente per documenti

Un assistente AI a cui carichi documenti (PDF, appunti, manuali) e fai domande.
Risponde **solo** in base ai documenti caricati e **cita le fonti** (file e pagina).

> Progetto di studio e portfolio: la pipeline RAG è scritta a mano, senza framework come LangChain, per capire ogni passaggio.

## Come funziona

```
PDF ──► estrazione testo ──► chunking ──► embedding ──► pgvector
                                                          │
domanda ──► embedding ──► ricerca dei chunk più simili ◄──┘
                                   │
                                   ▼
                     LLM (domanda + chunk) ──► risposta con citazioni
```

## Stack

| Livello | Tecnologia |
|---|---|
| Frontend | Angular |
| Backend | Python + FastAPI |
| Database vettoriale | PostgreSQL + pgvector (Docker) |
| Embedding | Ollama `nomic-embed-text` (sviluppo) / Gemini (produzione) |
| LLM | Ollama (sviluppo) / Groq o Gemini (produzione) |
| Parsing PDF | PyMuPDF |

## Struttura

```
progetto-rag/
├── backend/
│   ├── app/
│   │   ├── main.py          # API FastAPI
│   │   ├── config.py        # configurazione da .env
│   │   └── rag/             # pipeline RAG
│   │       ├── loader.py      # estrazione testo dai PDF
│   │       ├── chunking.py    # divisione in chunk
│   │       ├── embeddings.py  # testo → vettori
│   │       ├── store.py       # salvataggio e ricerca su pgvector
│   │       └── generator.py   # risposta dell'LLM con citazioni
│   ├── tests/
│   └── requirements.txt
├── frontend/                # app Angular (da generare con ng new)
├── data/documents/          # PDF di prova (non versionati)
├── eval/                    # domande di test per valutare le risposte
├── exercises/               # esercizi delle basi (settimana 1)
├── docs/                    # roadmap e diario degli esperimenti
└── docker-compose.yml       # PostgreSQL + pgvector
```

## Avvio rapido

### Requisiti
- Python 3.11+
- Docker Desktop
- [Ollama](https://ollama.com) con i modelli:
  ```bash
  ollama pull nomic-embed-text
  ollama pull llama3.2
  ```

### Database
```bash
docker compose up -d
```

### Backend
```bash
cd backend
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # macOS/Linux
pip install -r requirements.txt
copy .env.example .env        # Windows (cp su macOS/Linux)
uvicorn app.main:app --reload
```
API su http://localhost:8000. Documentazione interattiva su http://localhost:8000/docs.

## Roadmap

Vedi [docs/roadmap.md](docs/roadmap.md).

- [ ] Settimana 1 — Basi: Python, FastAPI, embedding
- [ ] Settimana 2 — Upload PDF, chunking, pgvector
- [ ] Settimana 3 — Chat con LLM e citazioni (MVP)
- [ ] Settimana 4 — Frontend Angular
- [ ] Settimana 5 — Ricerca ibrida e valutazione
- [ ] Settimana 6 — Deploy, demo, rifinitura

## Esperimenti e risultati

I test sulle diverse strategie (dimensione dei chunk, reranking, ecc.) sono annotati in [docs/esperimenti.md](docs/esperimenti.md).
