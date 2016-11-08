# -*- coding: utf-8 -*-
import flask

from triforce_webgui import manager


app = flask.Flask(__name__)
mgr = manager.RomDataManager()


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/system/<string:sys_name>')
def get_system(sys_name):
    # print(mgr.search(mgr.systems, shortname=sys_name, company='sega'))
    print(mgr.search(mgr.systems, name='atomiswaVe', company='sammy'))
    return flask.render_template('index.html')


@app.route('/game/<string:game_name>')
def get_game(game_name):
    print(mgr.search(mgr.games, shortname=game_name))
    return flask.render_template('index.html', )
