import pandas as pd

# Import av Data
kgdata = pd.read_excel("ssb-barnehager.xlsx", sheet_name="KOSandel120000",
                       header=3,
                       names=['kom','y15','y16','y17','y18','y19','y20','y21','y22','y23'],
                       na_values=['.', '..'])

# Vasking av data 
for coln in ['y15','y16','y17','y18','y19','y20','y21','y22','y23']:
    mask_over_100 = (kgdata[coln] > 100) 
    kgdata.loc[mask_over_100, coln] = float("nan")

kgdata.loc[724:779, 'kom'] = "NaN"

# Filtrerer ut kun navn på kommune fra kom feltet og setter kom lik denne verdien
kgdata["kom"] = kgdata['kom'].str.split(" ").apply(lambda x: x[1] if len(x) > 1 else "")

# Dette må gjøres for å unngå ikke relevante felt i vid tabell
kgdata_no_meta = kgdata.drop(kgdata.index[724:])

# Vasket data
renset_kb = kgdata_no_meta 

# print(renset_kb)

# -----------------------

# Oppgave 2A - Hvilken kommune har høyest andel barn i et til to-års alderen i 2023
høyest = renset_kb['y23'].max()

# Lager en tabell med kommunene som har høyest prosent andel barn på Barnehage
kommuner_med_høyest = renset_kb[renset_kb['y23'] == høyest]

# Print 
print("Kommuner med høyest andel barn i et til to-års alderen i 2023")
print(kommuner_med_høyest[['kom', 'y23']])

# ------------------------

# Oppgave 2B - Hvilken Kommune har lavest andel barn i et til to-års alderen i 2023

lavest = renset_kb['y23'].min()

# Lager en tabell med kommunene som har lavest andel barn på Barnehage 
kommuner_med_lavest = renset_kb[renset_kb['y23'] == lavest]

# Print
print("Kommuner med lavest andel barn i et til to-års alderen i 2023")
print(kommuner_med_lavest[['kom', 'y23']])


# ------------------------

