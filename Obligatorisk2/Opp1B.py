import pandas as pd
print(pd.__version__)


# Dette lager to forskjellige lister
tabell = {
    'name': ['Jabir', 'Abir', 'Dabir', 'Labir'],
    'gruppe': ['Gr1', 'Gr2', 'Gr3', 'Gr4']
    }
# Denne delen kombinerer listene i en tabell
StudentTabell = pd.DataFrame(tabell)

# Funksjonen som finner gruppen til en gitt student
# Input :: Input er navn på studenten og hvilken liste vi vil bruke
# Output :: Returverdi er da Navn på studenten og hvilken Gruppe de hører til
def FinnGr(Stud_navn, Liste):
    return Liste[Liste["name"] == Stud_navn]

print(FinnGr('Abir', StudentTabell))