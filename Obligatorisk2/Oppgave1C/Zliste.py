import pytest

# Oppgave 1C
# 9.1.8.2

# Funksjonen vil printe ut ord som bare inneholder bokstaven Z
# Input :: Ordliste :: list
# Output :: Ordliste som har Z :: list
def all_z_words(wordlist: list) -> list:
    """Produce list of words from the input that contain 'z'."""
    zlist = []  # Start with an empty list
    for wd in wordlist:
        if "z" in wd:
            zlist = [wd] + zlist  # Add word containing 'z' to the list
    return zlist

# Output
Ord = ["pizza", "zebra", "house", "buzz", "apple", "crazy"]
z_words = all_z_words(Ord)
print(z_words)  # Output: ['crazy', 'buzz', 'zebra', 'pizza']

# Testblokk

assert all_z_words(["pizza", "zebra", "house", "buzz", "apple", "crazy"]) == ['crazy', 'buzz', 'zebra', 'pizza']


# Filter Z bort med filter istedenfor
# Input :: Ordliste :: list
# Output :: Ord med Z :: list
def z_words(listen):
    """ Denne funksjonen filtrerer bort ord som ikke inneholder Z """
    listen = list(filter(lambda word: 'Z' in word, listen))
    return listen

Z_Liste = ["Zer", "Zyntanell", "Dantallian", "Jabir", "Zan"]
print(z_words(Z_Liste))

assert z_words(["Zer", "Zyntanell", "Dantallian", "Jabir", "Zan"]) == ['Zer', 'Zyntanell', 'Zan']