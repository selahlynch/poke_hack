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

dfti = dfti.replace({'1': 0.5, '0':0.25, '2':2, '.':1})

dfti

#%%
#dfti.to_csv("/data1/home/selah/pokemon_type_chart.csv")

#%%
print("flush")

#%%
def get_poke_types():
    return type_names_data

#%%
def get_super_effective(poke_type): #{{poke_type}} is super effective against ...
    types = dfti.loc[poke_type.lower()]
    se_types = types[types>1.0]
    return se_types

def get_not_effective(poke_type):
    types = dfti.loc[poke_type.lower()]
    se_types = types[types<1.0]
    return se_types

def get_resistant_to(poke_type):
    types = dfti[poke_type.lower()]
    se_types = types[types<1.0]
    return se_types

def get_vulnerable_to(poke_type): #{{poke_type}} is vulnerable to ...
    types = dfti[poke_type.lower()]
    se_types = types[types>1.0]
    return se_types

#%%  TESTING
#temp = get_super_effective('fairy')
get_not_effective('fairy')
#temp = get_resistant_to('fairy')
#temp = get_vulnerable_to('fairy')
#%%

#Who does poke_type suck against
def get_relative_power_chart(poke_type1, poke_type2=None, attack_type=None):
    dmg_from = 1/dfti[poke_type1.lower()]
    
    if poke_type2:
        dmg_from2 = 1/dfti[poke_type2.lower()]
        dmg_from = dmg_from*dmg_from2
    
    same_type_bonus = None
    if attack_type:
        if attack_type == poke_type1:
            same_type_bonus = True
    else:
        attack_type = poke_type1
    
    dmg_to = dfti.loc[attack_type.lower()]
    if same_type_bonus:
        dmg_to = dmg_to * 1.2

    df = pd.concat([dmg_from, dmg_to], axis=1)
    df.columns = ["defence","attack"]
    df['relative_power'] = dmg_to * dmg_from
    return df
    
def get_sucks_against(poke_type1, poke_type2=None, attack_type=None):
    rp = get_relative_power_chart(poke_type1, poke_type2, attack_type)
    return rp[rp.relative_power < 1].sort_values('relative_power', ascending=True)

def get_excells_against(poke_type1, poke_type2=None, attack_type=None):
    rp = get_relative_power_chart(poke_type1, poke_type2, attack_type)
    return rp[rp.relative_power > 1].sort_values('relative_power', ascending=False)

#%%
    
get_relative_power_chart('fairy')
get_sucks_against('fairy')

get_excells_against('fire', None, 'electric') #growlithe

get_excells_against('fire') #unspecified attack
get_excells_against('fire', None, 'fire') #with attack specified

get_relative_power_chart('bug').sort_values('relative_power', ascending=False)


#%%




