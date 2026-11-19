"""Salvataggio e ricerca dei chunk su PostgreSQL + pgvector.

Settimana 2 — TODO:
- crea la tabella chunks (id, document, page, content, embedding vector(768))
- salva i chunk con il loro embedding
- search(query_embedding, k) -> i k chunk più simili (distanza coseno)
"""
