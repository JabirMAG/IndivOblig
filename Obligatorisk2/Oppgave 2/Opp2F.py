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

# Filtrerer ut kun navn på kommunbe fra kom feltet og setter kom lik denne verdien
kgdata["kom"] = kgdata['kom'].str.split(" ").apply(lambda x: x[1] if len(x) > 1 else "")

# Dette må gjøres for å unngå ikke relevante felt i vid tabell
kgdata_no_meta = kgdata.drop(kgdata.index[724:])

# Vasket data
renset_kb = kgdata_no_meta 

# print(renset_kb)

# -----------------------

# Oppgave 2F - Hva er den gjennomsnittliget prosenten for alle barn fra 2015 til 2023 
renset_kb['gjennomsnitt_mean'] = renset_kb[['y23', 'y22', 'y21', 'y20', 'y19', 'y18', 'y17', 'y16', 'y15']].mean(axis=1, skipna=True)

# Finner gjennomsnitt prosenten mellom y15 og y23
mean_gjennomsnitt = renset_kb['gjennomsnitt_mean'].mean()

print("Gjennomsnittlig andel av barn som går på barnehage i kommunene mellom 2015 og 2023")
print(mean_gjennomsnitt)

# ------------------------

