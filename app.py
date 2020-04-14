
from flask import Flask, render_template, redirect, url_for, request
import pokemon_types

app = Flask(__name__)


@app.route('/')
def hello_world(name = None):
    return redirect(url_for('landing'))

@app.route('/landing', methods=['GET'])
def landing():
    poke_types = pokemon_types.get_poke_types()
    poke_german = {}
    poke_german['ground'] = 'boden'
    poke_german['dragon'] = 'drache'
    poke_german['ice'] = 'eis'
    poke_german['electric'] = 'elektro'
    poke_german['fairy'] = 'fee'
    poke_german['fire'] = 'feuer'
    poke_german['flying'] = 'flug'
    poke_german['ghost'] = 'geist'
    poke_german['rock'] = 'gestein'
    poke_german['poison'] = 'gift'
    poke_german['bug'] = 'kafer'
    poke_german['fighting'] = 'kampf'
    poke_german['normal'] = 'normal'
    poke_german['grass'] = 'pflanze'
    poke_german['psychic'] = 'psychic'
    poke_german['steel'] = 'stahl'
    poke_german['dark'] = 'unlicht'
    poke_german['water'] = 'wasser'
    return render_template('landing.html', poke_types=poke_types, poke_german=poke_german)


@app.route('/choose_show_types', methods=['GET', 'POST'])
def choose_show_types():

    print("Begin show types")
    
    poke_types = pokemon_types.get_poke_types()

    poke_type_selection = ''
    poke_type_selections = []
    poke_deets = {}
    if request.method == 'POST':
 
        print("Begin Get post values")
        poke_type_selections.append(request.form['ptype1-select'])
        poke_type_selections.append(request.form['ptype2-select'])
        poke_type_selections.append(request.form['pattack1-select'])
        poke_type_selection = ':'.join(poke_type_selections)
        print("End Get post values")
        
        if poke_type_selections[1] == '--select--':
            poke_type_selections[1] = None
        if poke_type_selections[2] == '--select--':
            poke_type_selections[2] = None
        
        poke_deets['sucks_against'] = pokemon_types.get_sucks_against(poke_type_selections[0],poke_type_selections[1],poke_type_selections[2])
        poke_deets['excells_against'] = pokemon_types.get_excells_against(poke_type_selections[0],poke_type_selections[1],poke_type_selections[2])

    print("End show types")

    return render_template('choose_show_types.html', poke_types=poke_types, poke_type_selections=poke_type_selections, poke_type_selection=poke_type_selection, poke_deets=poke_deets)
    

@app.route('/poke_types_deets', methods=['POST'])
def poke_types_deets():
    #TODO - get the strengths and weaknesses of this poke types
    poke_deets = {}
    poke_types = []
    poke_types.append(request.form['ptype1-select'])
    poke_types.append(request.form['ptype2-select'])
    poke_types.append(request.form['ptype3-select'])
    poke_type = ':'.join(poke_types)
    
    if poke_types[1] == '--select--':
        poke_types[1] = None
    if poke_types[2] == '--select--':
        poke_types[2] = None
    
    poke_deets['sucks_against'] = pokemon_types.get_sucks_against(poke_types[0],poke_types[1],poke_types[2])
    poke_deets['excells_against'] = pokemon_types.get_excells_against(poke_types[0],poke_types[1],poke_types[2])
    return render_template('poke_type_deets.html', poke_type=poke_type, poke_deets=poke_deets)#, poke_deets=poke_deets)


@app.route('/poke_type_deets/<poke_type>')
def poke_type_deets(poke_type):
    #TODO - get the strengths and weaknesses of this poke types
    poke_deets = {}
    poke_deets['super_effective'] = pokemon_types.get_super_effective(poke_type)
    poke_deets['not_effective'] = pokemon_types.get_not_effective(poke_type)
    poke_deets['vulnerable_to'] = pokemon_types.get_vulnerable_to(poke_type)
    poke_deets['resistant_to'] = pokemon_types.get_resistant_to(poke_type)

    poke_deets['sucks_against'] = pokemon_types.get_sucks_against(poke_type)
    poke_deets['excells_against'] = pokemon_types.get_excells_against(poke_type)
    return render_template('poke_type_deets.html', poke_type=poke_type, poke_deets=poke_deets)#, poke_deets=poke_deets)

@app.route('/fun_with_data')
def fun_with_data():
    return "<h1>Coming soon!! </h1>" + pokemon_types.say_hello()
