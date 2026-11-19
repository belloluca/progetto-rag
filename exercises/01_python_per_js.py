"""
Esercizio 1 — Python visto da uno sviluppatore JavaScript
Esegui con:  python exercises/01_python_per_js.py

Completa ogni TODO. Quando tutti gli assert passano, vedrai "Tutto ok!".

Promemoria JS → Python:
  const x = [1, 2]         →  x = [1, 2]
  arr.map(n => n * 2)      →  [n * 2 for n in arr]
  arr.filter(n => n > 1)   →  [n for n in arr if n > 1]
  { name: "a" }            →  {"name": "a"}
  `ciao ${nome}`           →  f"ciao {nome}"
  function f(a, b = 1) {}  →  def f(a, b=1):
"""

# TODO 1: crea una lista con i quadrati dei numeri da 1 a 5 (usa range e una list comprehension)
squares = None
assert squares == [1, 4, 9, 16, 25]

# TODO 2: dalla lista di parole, tieni solo quelle con più di 4 lettere
words = ["rag", "embedding", "chunk", "llm", "vettore"]
long_words = None
assert long_words == ["embedding", "chunk", "vettore"]

# TODO 3: scrivi una funzione che divide un testo in pezzi di `size` caratteri
# (è il chunking più semplice possibile: lo riuserai nella settimana 2)
def split_text(text, size):
    pass

assert split_text("abcdefgh", 3) == ["abc", "def", "gh"]

# TODO 4: data una lista di dizionari, restituisci i nomi dei documenti con più di 10 pagine
docs = [
    {"name": "manuale.pdf", "pages": 42},
    {"name": "nota.pdf", "pages": 2},
    {"name": "tesi.pdf", "pages": 80},
]
big_docs = None
assert big_docs == ["manuale.pdf", "tesi.pdf"]

print("Tutto ok!")
