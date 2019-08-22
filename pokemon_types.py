type_names_data = "normal fire water electric grass ice fighting poison ground flying psychic bug rock ghost dragon dark steel fairy".split()
type_interactions_data = '''
............10..1.
.11.22.....21.1.2.
.21.1...2...2.1...
..211...02....1...
.12.1..121.12.1.1.
.11.21..22....2.1.
2....2.1.11120.221
....2..11...11..02
.2.21..2.0.12...2.
...12.2....21...1.
......22..1....01.
.1..2.11.12..1.211
.2...21.12.2....1.
0.........2..2.1..
..............2.10
......1...2..2.1.1
.111.2......2...12
.1....21......221.
'''

type_interaction_rows = type_interactions_data.split()

type_interaction_cells = [list(row) for row in type_interaction_rows]


import pandas as pd
import numpy as np

dfti = pd.DataFrame(type_interaction_cells, index=type_names_data, columns=type_names_data)
#columns are defence
#rows of attack

dfti = dfti.replace({'1': 0.5, '0':0, '2':2, '.':1})

dfti

#%%Ahhh team rocket is threatening me with water!!!

water_attack = dfti.loc['water']
water_defense = dfti['water']


water_attack[water_attack < 1].index.tolist()
water_defense[water_defense > 1].index.tolist()

#%%
print("flush")
#%%

## I have a combined rock/water type with ground moves... who might I be good at challenging???

#who is rock good at attacking?
#who is water good at attacking?
#who is water safe against?
#who is rock safe against?
#who are ground moves good against?

#%%
poke_type = "fire"
poke_type


#%%
def say_hello():
    return "Pika!"

#%%
def get_super_effective(poke_type):
    types = dfti.loc[poke_type.lower()]
    se_types = types[types>1.0]
    return se_types

def get_not_effective(poke_type):
    types = dfti.loc[poke_type.lower()]
    se_types = types[types<1.0]
    return se_types

def get_resistant_to(poke_type):  #I am resistant to water OR water is resistant to me
    types = dfti[poke_type.lower()]
    se_types = types[types<1.0]
    return se_types

def get_vulnerable_to(poke_type):
    types = dfti[poke_type.lower()]
    se_types = types[types>1.0]
    return se_types


#%%

get_super_effective('water')
get_not_effective('water')
get_resistant_to('water')
get_vulnerable_to('water')

#%%

