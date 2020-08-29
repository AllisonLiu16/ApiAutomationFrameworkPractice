# coding:utf-8

import configparser
import os
# import logging


# logging.basicConfig(level=logging.INFO, filename="/Users/nan.liu/ApiAutomationProject/ApiPractice/logs/all.log",
#                     filemode="w", format='%(asctime)s -  %(levelname)s: %(message)s')
# logging.info('info 信息')


class GlobalConfig:

    # 获取项目根目录
    root_path = os.path.abspath(".")
    # 获取当前环境参数
    env_file = root_path + "/environment.txt"
    with open(env_file, 'r') as f:
        content = f.read().split("\n")
        env = content[0]
        client_or_server = content[1]

    # 读取配置文件相关配置信息
    # 路径：root_path/env/env.ini
    config_file_path = root_path + "/envs/" + env + ".ini"
    config = configparser.ConfigParser()
    config.read(config_file_path)
    sections = config.sections()
    for section in sections:
        if client_or_server in sections:
            if section == client_or_server:
                for item in config.items(section):
                    if item[0] == "base_url":
                        base_url = item[1]
                    elif item[0] == "cookies":
                        cookies = item[1]
        else:
            print("Please choose Client or Server to continue!")
