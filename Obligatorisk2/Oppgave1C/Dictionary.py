# 9.22 
# Ordbok som inneholder romnavn og antall seter
rom_dict = {
    "RomA": 30,
    "RomB": 45,
    "RomC": 100
}

# 1. Sjekke hvor mange seter det er i RomA
print("Antall seter i RomA:", rom_dict["RomA"])

# 2. Sjekke hvor mange seter RomA har, og legge til 10
print("Antall seter i RomA etter oppdatering:", rom_dict["RomA"] + 10)


# 3. Sjekke om at det er 50 plasser
#  Sjekker om at det er 50 
# Input :: Hvilket Rom man putter inn :: Table
# Output :: Viser om at rommet har plass :: String
def rom_filter(rom_navn):
    if rom_dict[rom_navn] >= 50:
        return f"{rom_navn} har nok plass."
    else:
        return f"{rom_navn} har ikke nok plass."

# Sjekker om RomC har nok plass
print(rom_filter("RomC"))