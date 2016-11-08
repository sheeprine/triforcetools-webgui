# -*- coding: utf-8 -*-
import copy
import os

import yaml


class RomDataManager(object):
    systems_dir = 'systems'
    games_dir = 'games'
    roms_dir = 'roms'

    def __init__(self):
        self.systems = dict()
        self.games = dict()
        self.game_assoc = dict()
        self.base_path = os.path.dirname(os.path.relpath(__file__))
        self.systems_path = os.path.join(self.base_path, self.systems_dir)
        self.games_path = os.path.join(self.base_path, self.games_dir)
        self.roms_path = os.path.join(self.base_path, self.roms_dir)
        self._load_systems(self.systems_path)
        self._load_games(self.games_path)
        self.__associate_games()

    @staticmethod
    def _load_file(sysfile):
        with open(sysfile, 'r') as f:
            content = yaml.load(f)
            return content

    @classmethod
    def _load_data(cls, path, dest, key='name'):
        for f in os.listdir(path):
            data = cls._load_file(os.path.join(path, f))
            dest[data[key].lower()] = data

    def _load_systems(self, path):
        self._load_data(path, self.systems)

    def _load_games(self, path):
        self._load_data(path, self.games, 'shortname')

    def __associate_games(self):
        for game in self.games.values():
            system_name = game['system'].lower()
            if system_name not in self.game_assoc:
                self.game_assoc[system_name] = list()
            self.game_assoc[system_name].append(game)

    def search(self, data, shortname=None, **kwargs):
        if shortname:
            try:
                return data[shortname.lower()]
            except KeyError:
                pass
        elif kwargs:
            result = copy.copy(data.values())
            for search_name, search_value in kwargs.items():
                for item in data.values():
                    # TODO(sheeprine): Compute Levenshtein  distance to ease
                    # search.
                    if item[search_name].lower() != search_value.lower():
                        if item in result:
                            result.remove(item)
            return result
        return []

    def get_system(self, shortname=None, **kwargs):
        return self.search(self.systems, shortname, **kwargs)

    def get_game(self, shortname=None, **kwargs):
        return self.search(self.games, shortname, **kwargs)

    def find_rompath(self, game):
        system_name = game['system'].lower()
        basepath = os.path.join(self.roms_path, system_name)
        for f in game['roms']:
            rompath = os.path.join(basepath, f)
            if os.path.isfile(rompath):
                return rompath
