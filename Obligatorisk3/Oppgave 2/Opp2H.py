import pandas as pd
import matplotlib.pyplot as plt
# Altair funket ikke for meg, bruker matplotlib


# Last inn data (forutsetter at dette allerede er gjort)
kgdata = pd.read_excel("ssb-barnehager.xlsx", sheet_name="KOSandel120000",
                       header=3,
                       names=['kom','y15','y16','y17','y18','y19','y20','y21','y22','y23'],
                       na_values=['.', '..'])

# Rens dataene
for coln in ['y15','y16','y17','y18','y19','y20','y21','y22','y23']:
    mask_over_100 = (kgdata[coln] > 100)
    kgdata.loc[mask_over_100, coln] = float("nan")

kgdata.loc[724:779, 'kom'] = "NaN"
kgdata["kom"] = kgdata['kom'].str.split(" ").apply(lambda x: x[1] if len(x) > 1 else "")
kgdata_no_meta = kgdata.drop(kgdata.index[724:])

# Filtrer de rensede dataene
# renset_kb = kgdata_no_meta


"""Lag et diagram, som viser den gjennomsnittlige prosenten for år 2015 - 2023 for
10 kommuner, som har data for alle årene, og som har den høyeste prosenten av
barn i barnehagen i ett- og to-årsalderen"""
# Problemløsningsstrategi
# 1. Lag en ny tabell med dataene som ikke har tomrom
# 2. Sorter tabellen sånn at bare top 10 høyeste blir vist fram
# 3. Lag en diagram med tabellen fra 2.

# Oppgave 2H
# 1. Fjerner alt NaN med dropNA
kg_drop = kgdata.dropna()
# print(kg_drop)

# 2. Sorter Tabellen
# Lag ny kolonne som inneholder maksverdien for hver kommune fra 2015 til 2023
kg_drop['høyeste_verdi'] = kg_drop[['y15', 'y16', 'y17', 'y18', 'y19', 'y20', 'y21', 'y22', 'y23']].max(axis=1)

# Hent topp 10 kommuner basert på høyeste verdi
kg_høy = kg_drop.nlargest(10, 'høyeste_verdi')

# Dropp 'høyeste_verdi'-kolonnen for å beholde de opprinnelige årene
kg_høy = kg_høy.drop(columns=['høyeste_verdi'])

# Vis topp 10-tabellen med verdier fra alle år
print("Topp 10 kommuner basert på høyeste verdi fra 2015-2023:")
print(kg_høy)

# 3. Lag diagrammet
kg_høy.set_index('kom').T.plot(kind='bar', figsize=(10, 6))
plt.title('Topp 10 kommuner basert på høyeste verdi (2015-2023)')
plt.xlabel('År')
plt.ylabel('Prosent')
plt.xticks(rotation=0)
plt.legend(title='Kommune', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
