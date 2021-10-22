import json
import os
# will create or edit local json file for local machine settings
class settings:
    self.settings_dict = dict()
    # settings overview:
    # stores classes in json elements 

    def class_to_json(self,list_of_classes: list) -> None:
        for c in list_of_classes:
            # store class data in dict
            # then add dict into json dict with key = name-section : value = all class data
            temp_list = c.dump_info()
            self.settings_dict[temp_list[0]] = temp_list[1]

    def create_settings_file(self):
        if not self.settings_file_exists():
            open("settings.json","x")

    def update_settings(self) -> None:
        if self.settings_file.exists():
            self.settings_file = open("settings.json","w")
            json.dump(self.settings_dict,self.settings_file)

    def get_settings(self) -> dict:
        if self.check_path():
            return json.load(self.settings_file)

    def get_settings_file(self):
        if self.settings_file_exists():
            self.settings_file = open("settings.json","r")
        else:
            self.create_settings_file()
            self.settings_file = open("settings.json","r")

    def settings_file_exists(self) -> bool:
        cwd = os.getcwd()
        return (os.path.exists(cwd + "/settings.json"))

