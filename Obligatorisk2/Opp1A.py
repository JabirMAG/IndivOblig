# Oppgave 1A 

# Denne lager listen vi vil bruke til my-string-length
Lengde = [5, 6, 7, 8, 1]

# string_length(liste) :: liste -> Int
# Input Vi putter inn listen vi vil bruke :: Liste
# Output :: Funksjonen gir oss hvor mange string det er i listen i hele tall :: Int
def string_length(liste): # String_length er funksjonen for å telle listen, (Liste) er input
    """ Denne funksjonen teller opp hvor mange String det er i en liste, og gir en
returverdi som viser dette. 
"""
    len(liste) # Mye simplere en pyret, Len vil da telle listen for oss

print(len(Lengde)) # Print av "Lengde" Listen


# Denne delen er for My-Max

# max(list) :: liste -> int
# Input :: Vi putter inn listen vi vil bruke :: Liste
# Output :: Returverdi er det høyeste tallet i listen :: Int
print(max(Lengde)) # Istedenfor en funksjon som på pyret så kan man bruke max(liste) i python