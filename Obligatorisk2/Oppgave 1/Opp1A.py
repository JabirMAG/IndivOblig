# Oppgave 1A 
# string_length(liste) :: liste -> Int
# Input Vi putter inn listen vi vil bruke :: Liste
# Output :: Funksjonen gir oss hvor mange string det er i listen :: Int
def my_str_len(liste): # String_length er funksjonen for å telle listen, (Liste) er input
    siffer = 0
    for string in liste:
        for char in string:
            siffer += 1
    return siffer

Lengde = ["Hello_World", "Goodbye_World", "Wonderful_World"] # Listen vi bruker for funksjonen





print(my_str_len(Lengde)) # Printer ut funksjonen

Tall = [1, 3, 4, 10, 5, 7]

# Denne delen er for My-Max

# max(list) :: liste -> int
# Input :: Vi putter inn listen vi vil bruke :: Liste
# Output :: Returverdi er det høyeste tallet i listen :: Int
print(max(Tall)) # Vi kan bruke en innebygd funksjon for dette