import altair as alt
import pandas as pd
import pytest 
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

source = pd.DataFrame({
    'Year': ['y15', 'y16', 'y17', 'y18', 'y19', 'y20', 'y21', 'y22', 'y23'],
    'Prosent': [28, 55, 43, 91, 81, 53, 19, 87, 52]
})

chart = alt.Chart(source).mark_bar().encode(
    x='Year',
    y='Prosent'
)

def test_contains_moss():
    assert renset_kb['kom'].loc[0] == 'Halden'
    assert renset_kb['kom'].loc[1] == 'Moss'
