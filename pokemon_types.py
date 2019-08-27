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
print("flush")

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

#%%  TESTING
#temp = get_super_effective('fairy')
temp = get_not_effective('fairy')
#temp = get_resistant_to('fairy')
#temp = get_vulnerable_to('fairy')
for (ptype, pcoef) in temp.iteritems():
    print("{}x damage to {}".format(pcoef, ptype))
#%%

#Who does poke_type suck against
def get_relative_power_chart(poke_type):
    d_from = 1/dfti[poke_type.lower()]
    d_to = dfti.loc[poke_type.lower()]
    df = pd.concat([d_from, d_to], axis=1)
    df.columns = ["d_from","d_to"]
    df['relative_power'] = d_to * d_from
    return df
    
def get_sucks_against(poke_type):
    rp = get_relative_power_chart(poke_type)
    return rp[rp.relative_power < 1].sort_values('relative_power', ascending=True)

def get_excells_against(poke_type):
    rp = get_relative_power_chart(poke_type)
    return rp[rp.relative_power > 1].sort_values('relative_power', ascending=False)

#%%
    
#temp = get_relative_power_chart('fairy')
temp = get_sucks_against('fairy')

#%%
print( "Fairy sucks against...")
print( "type - damage from - damage to")

for (ptype, (coef_to, coef_from, pr)) in temp.iterrows():
    print("{} - {} - {}".format(ptype, coef_from, coef_to))
    


