
# A very simple Flask Hello World app for you to get started with...
# https://flask.palletsprojects.com/en/1.1.x/quickstart/#quickstart

from flask import Flask, render_template
import pokemon_types

app = Flask(__name__)

@app.route('/')
def hello_world(name = None):
    return render_template('hello.html', name=name)

@app.route('/choose_poke_type')
def choose_poke_type():
    poke_types = "Normal Fire Water Electric Grass Ice Fighting Poison Ground Flying Psychic Bug Rock Ghost Dragon Dark Steel Fairy".split()
#    poke_types = poke_hack.get_poke_types()
    return render_template('choose_poke_type.html', poke_types=poke_types)

@app.route('/poke_type_deets/<poke_type>')
def poke_type_deets(poke_type):
    #TODO - get the strengths and weaknesses of this poke types
    poke_deets = {
        'super_effective':['poop'], #poke_hack.get_super_effective(poke_type)
        'not_effective':['pee', 'snot'],
        'resistant_to':['soda', 'fries'],
        'vulnerable_to':['ketchup']
    }

    return render_template('poke_type_deets.html', poke_type=poke_type, poke_deets=poke_deets)#, poke_deets=poke_deets)

@app.route('/fun_with_data')
def fun_with_data():
    return "<h1>Coming soon!! </h1>" + pokemon_types.say_hello()
