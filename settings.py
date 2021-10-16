import json
import os
# will create or edit local json file for local machine settings

settings_dict = dict()
# settings overview:
# stores classes in json elements 

def class_to_json(self,list_of_classes: list) -> None:
    for c in list_of_classes:
        # store class data in dict
        # then add dict into json dict with key = name-section : value = all class data
        temp_list = c.dump_info()
        settings_dict[temp_list[0]] = temp_list[1]

def create_settings_file():
    cwd = os.getcwd()
    if not os.path.exists(cwd + "/settings.json"):
        open("settings.json","x")

def update_settings():
    pass

def get_settings() -> dict:
    pass



