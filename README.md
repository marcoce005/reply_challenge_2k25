# reply_challenge_2k25
Reply Code Challenge 2025

The Hack the Code Challenge Teen Edition is an international team-based competition combining coding and cybersecurity for high school students. Teams will solve 5 algorithm-based problems, each with 4 progressively challenging input files, plus a bonus CTF (Capture the Flag) input. Successfully solving the CTF bonus will double the points earned for the related problem. Teams have 6 hours to complete all the challenges.

# Python Cheat Sheet

## Indice
1. [Sintassi di Base](#sintassi-di-base)
2. [Tipi di Dati](#tipi-di-dati)
3. [Operazioni](#operazioni)
4. [Strutture di Controllo](#strutture-di-controllo)
5. [Funzioni](#funzioni)
6. [Classi e OOP](#classi-e-oop)
7. [Moduli e Pacchetti](#moduli-e-pacchetti)
8. [Gestione Eccezioni](#gestione-eccezioni)
9. [File Handling](#file-handling)
10. [Metodi di Liste e Stringhe](#metodi-di-liste-e-stringhe)

---

## Sintassi di Base
```python
# Stampa a schermo
greeting = "Hello, World!"
print(greeting)

# Commenti
dato = 10  # Questo è un commento
```

## Tipi di Dati
```python
intero = 10          # Int
virgola_mobile = 3.14 # Float
booleano = True      # Boolean
stringa = "Testo"    # String
lista = [1, 2, 3]    # List
tupla = (1, 2, 3)    # Tuple
dizionario = {"chiave": "valore"} # Dict
insieme = {1, 2, 3}  # Set
```

## Operazioni
```python
# Operazioni matematiche
somma = 5 + 3
sottrazione = 10 - 4
moltiplicazione = 3 * 4
divisione = 10 / 2
modulo = 10 % 3
potenza = 2 ** 3
```

## Strutture di Controllo
```python
# If-Else
x = 10
if x > 5:
    print("x è grande")
elif x == 5:
    print("x è 5")
else:
    print("x è piccolo")

# Ciclo For
for i in range(5):
    print(i)

# Ciclo While
n = 0
while n < 5:
    print(n)
    n += 1
```

## Funzioni
```python
def saluta(nome):
    return f"Ciao, {nome}!"

print(saluta("Mario"))
```

## Classi e OOP
```python
class Persona:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    def descrivi(self):
        return f"{self.nome} ha {self.eta} anni"

persona = Persona("Alice", 30)
print(persona.descrivi())
```

## Moduli e Pacchetti
```python
# Importare moduli
import math
print(math.sqrt(16))

# Importare solo una funzione specifica
from random import randint
print(randint(1, 10))
```

## Gestione Eccezioni
```python
try:
    risultato = 10 / 0
except ZeroDivisionError:
    print("Errore: divisione per zero")
finally:
    print("Operazione conclusa")
```

## File Handling
```python
# Scrittura su file
with open("file.txt", "w") as f:
    f.write("Ciao Mondo")

# Lettura da file
with open("file.txt", "r") as f:
    contenuto = f.read()
    print(contenuto)
```

## Metodi di Liste e Stringhe

### Metodi delle Liste
```python
lista = [1, 2, 3, 4]
lista.append(5)  # Aggiunge un elemento alla fine
lista.insert(1, 10)  # Inserisce 10 in posizione 1
lista.remove(2)  # Rimuove il primo 2 trovato
lista.pop()  # Rimuove l'ultimo elemento
lista.reverse()  # Inverte la lista
lista.sort()  # Ordina la lista
indice = lista.index(3)  # Trova l'indice del valore 3
conteggio = lista.count(1)  # Conta il numero di volte che 1 appare
lista.extend([6, 7, 8])  # Aggiunge più elementi alla lista
nuova_lista = lista.copy()  # Crea una copia della lista
lista.clear()  # Svuota la lista
```

### Metodi delle Stringhe
```python
testo = "ciao mondo"
maiuscolo = testo.upper()  # "CIAO MONDO"
minuscolo = testo.lower()  # "ciao mondo"
caps = testo.capitalize()  # "Ciao mondo"
titolo = testo.title()  # "Ciao Mondo"
invertito = testo.swapcase()  # "CIAO MONDO" -> "ciao mondo"
lunghezza = len(testo)  # Lunghezza della stringa
sostituito = testo.replace("mondo", "Python")  # "ciao Python"
parti = testo.split(" ")  # Divide la stringa in una lista
unito = "-".join(parti)  # Unisce la lista con "-"
trovato = testo.find("m")  # Trova l'indice della prima "m"
inizia = testo.startswith("ciao")  # True
finisce = testo.endswith("mondo")  # True
rimosso = testo.strip()  # Rimuove spazi iniziali e finali
```

---

Questo cheat sheet fornisce una panoramica rapida delle funzionalità principali di Python!

