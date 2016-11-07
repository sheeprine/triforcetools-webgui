# -*- coding: utf-8 -*-
import flask

from triforce_webgui import webgui


app = flask.Flask(__name__)
instance = webgui.TriforceWebGUI()


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/system/<string:sys_name>')
def get_system(sys_name):
    # print(instance.search(instance.systems, shortname=sys_name, company='sega'))
    print(instance.search(instance.systems, name='atomiswaVe', company='sammy'))
    return flask.render_template('index.html')


@app.route('/game/<string:game_name>')
def get_game(game_name):
    print(instance.search(instance.games, shortname=game_name))
    return flask.render_template('index.html', )
