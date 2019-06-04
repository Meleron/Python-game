import game
import hero
import copter
import knight
from pymongo import MongoClient
from termcolor import colored


class Database:
    client = MongoClient('mongodb://localhost:27017')
    db = client.game_settings_db
    collection = db.game_settings
    force_update = True

    highscore = None
    spawn_rate_on_start = None
    screen_width = None
    screen_height = None
    hero_width = None
    hero_height = None
    start_hero_health = None
    start_hero_speed = None
    copter_width = None
    copter_height = None
    knight_height = None
    knight_width = None
    start_knight_speed = None
    start_knight_reaction = None

    @staticmethod
    def save_data():
        game_settings_data = {"highscore": str(game.Game.highscore),
                              "spawn_rate_on_start": "100",
                              "screen": {
                                  "screen_width": "1280",
                                  "screen_height": "720"},
                              "hero": {
                                  "hero_width": "86",
                                  "hero_height": "88",
                                  "start_hero_health": "5",
                                  "start_hero_speed": "15"},
                              "copter": {
                                  "copter_width": "80",
                                  "copter_height": "60"},
                              "knight": {
                                  "knight_width": "65",
                                  "knight_height": "90",
                                  "start_knight_speed": "8",
                                  "start_knight_reaction": "7"}
                              }
        """
        game_settings_data = {"highscore": "0",
                              "spawn_rate_on_start": "100",
                              "screen": {
                                  "screen_width": "1280",
                                  "screen_height": "720"},
                              "hero": {
                                  "hero_width": "86",
                                  "hero_height": "88",
                                  "start_hero_health": "3",
                                  "start_hero_speed": "15"},
                              "copter": {
                                  "copter_width": "80",
                                  "copter_height": "60"},
                              "knight": {
                                  "knight_width": "65",
                                  "knight_height": "90",
                                  "start_knight_speed": "8",
                                  "start_knight_reaction": "7"}
                              }
        """
        if Database.db.game_settings.count() > 1 or Database.force_update:
            Database.db.game_settings.delete_many({})
        if Database.db.game_settings.count() == 1:
            Database.db.game_settings.update({}, game_settings_data)
        else:
            Database.collection.insert_one(game_settings_data)

    @staticmethod
    def load_data():
        collection_name = "game_settings"
        if collection_name in Database.db.collection_names():

            print("[database] connection to collection '" + str(collection_name) + "' succeed")
            Database.highscore = int(Database.collection.find({}, {"highscore": 1}).next()["highscore"])
            Database.spawn_rate_on_start = int(Database.collection.find({}, {"spawn_rate_on_start": 1}).next()["spawn_rate_on_start"])
            Database.screen_width = int(Database.collection.find({}, {"screen": 1}).next()["screen"]["screen_width"])
            Database.screen_height = int(Database.collection.find({}, {"screen": 1}).next()["screen"]["screen_height"])
            Database.hero_width = int(Database.collection.find({}, {"hero": 1}).next()["hero"]["hero_width"])
            Database.hero_height = int(Database.collection.find({}, {"hero": 1}).next()["hero"]["hero_height"])
            Database.start_hero_health = int(Database.collection.find({}, {"hero": 1}).next()["hero"]["start_hero_health"])
            Database.start_hero_speed = int(Database.collection.find({}, {"hero": 1}).next()["hero"]["start_hero_speed"])
            Database.copter_width = int(Database.collection.find({}, {"copter": 1}).next()["copter"]["copter_width"])
            Database.copter_height = int(Database.collection.find({}, {"copter": 1}).next()["copter"]["copter_height"])
            Database.knight_width = int(Database.collection.find({}, {"knight": 1}).next()["knight"]["knight_width"])
            Database.knight_height = int(Database.collection.find({}, {"knight": 1}).next()["knight"]["knight_height"])
            Database.start_knight_speed = int(Database.collection.find({}, {"knight": 1}).next()["knight"]["start_knight_speed"])
            Database.start_knight_reaction = int(Database.collection.find({}, {"knight": 1}).next()["knight"]["start_knight_reaction"])
            '''
            print(Database.highscore)
            print(Database.spawn_rate_on_start)
            print(Database.screen_width)
            print(Database.hero_width)
            print(Database.hero_height)
            print(Database.start_hero_speed)
            print(Database.copter_width)
            print(Database.copter_height)
            print(Database.knight_width)
            print(Database.knight_height)
            print(Database.start_knight_speed)
            print(Database.start_knight_reaction)
            '''
        else:
            print(colored("[database] error connecting to collection '" + str(collection_name) + "'", "red"))

