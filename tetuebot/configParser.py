#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from configparser import ConfigParser
import os

from dotenv import load_dotenv

PATH_TO_CONFIG_FILE = 'login_data.cfg'

def get_configuration(section):
    """
    create a file ".env" and place it into the root folder, containing:

        name=""
        owner=""
        client_id=""
        token=""

    edit the running configuration in Pycharm "EnvFile"-Tabber-> add the environment file ".env"

    :param section: irgnored
    :type section: string
    :return:
    :rtype:
    """
    load_dotenv()
    dict_config={}
    for key in ["name","owner","client_id","token"]:
        dict_config[key]=os.getenv(key)
    return True, dict_config

def get_configuration2(section):
    config = ConfigParser()
    config.read(PATH_TO_CONFIG_FILE)
    dict_config = {}
    if config.has_section(section):
        for element in config.items(section):
            dict_config[element[0]] = element[1]
    else:
        return False, dict_config

    if len(dict_config) != 0:
        return True, dict_config
    else:
        return False, dict_config

