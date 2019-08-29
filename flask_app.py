
# A very simple Flask Hello World app for you to get started with...
# https://flask.palletsprojects.com/en/1.1.x/quickstart/#quickstart

from flask import Flask, render_template, redirect, url_for, request
import pokemon_types

app = Flask(__name__)

@app.route('/')
def hello_world(name = None):
    return redirect(url_for('choose_poke_type'))

@app.route('/choose_poke_type')
def choose_poke_type():
    poke_types = pokemon_types.get_poke_types()
    return render_template('choose_poke_type.html', poke_types=poke_types)

@app.route('/choose_poke_types')
def choose_poke_types():
    poke_types = pokemon_types.get_poke_types()
    return render_template('choose_poke_types.html', poke_types=poke_types)

@app.route('/show_poke_types', methods=['GET', 'POST'])
def show_poke_types():
    print(request.form['ptype-select'])
    poke_type = request.form['ptype-select']
    return render_template('show_poke_types.html', poke_type=poke_type)


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
