# Oppgave 1C
# 9.1.1 Konvertering av vekt på månen
# Input :: Hvor mye man veier på jorden :: Int
# Output :: Hvor mye man veier på månen :: Int
def vekt_månen(vekt_jorden):
    """ Denne funksjonen er for å regne ut hvor mye man veier på månen"""
    vekt_jorden = vekt_jorden * 1/6
    return vekt_jorden

print(vekt_månen(50)) # Printer ut output
