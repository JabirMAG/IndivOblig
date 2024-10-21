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
renset_kb = kgdata_no_meta


"""Lag et diagram, som viser den gjennomsnittlige prosenten for år 2015 - 2023 for
10 kommuner, som har data for alle årene, og som har den høyeste prosenten av
barn i barnehagen i ett- og to-årsalderen"""

# Output


# Oppgave 2H
# Input: Navn på Kommunen :: Str
# Output: diagram av kommune :: Diagram
# Funksjon for å plotte data for en valgt kommune
def plot_kommune(kommune):
    """ Lager en diagram av kommunen vi velger """
    kommune_data = renset_kb[renset_kb['kom'] == kommune]
    if kommune_data.empty:
        print(f"Kommunen '{kommune}' finnes ikke i datasettet.")
        return
    
    # Forbered dataene for plotting
    år = ['y15', 'y16', 'y17', 'y18', 'y19', 'y20', 'y21', 'y22', 'y23']
    prosent = kommune_data[år].values.flatten()

    # Lager diagrammet
    plt.figure(figsize=(10, 6))
    plt.plot(år, prosent, marker='o', linestyle='-', color='b')
    plt.title(f'Prosent av barn i ett- og to-årsalderen i barnehagen for {kommune}')
    plt.xlabel('År')
    plt.ylabel('Prosent')
    plt.grid(True)
    plt.xticks(ticks=range(len(år)), labels=[f'20{årstall[1:]}' for årstall in år])
    plt.show()

# Kall funksjonen med en spesifikk kommune
plot_kommune("Oslo")  # Erstatt "Oslo" med kommunen du vil plotte

