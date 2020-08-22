# coding:utf-8

from optparse import OptionParser
import pytest
import os

root_path = os.path.abspath(".")


def parse_option():
    """
    添加命令行参数，并解析
    :return:
    """
    option_parser = OptionParser()
    option_parser.add_option("-e", "--environment",
                             dest="env",
                             action="store",
                             help="Please choose an environment for this application: test, prod")
    option_parser.add_option("-p", "--project",
                             dest="project",
                             action="store",
                             help="Please choose an project: server,client")
    opts, args = option_parser.parse_args()
    return opts, args


def main():
    """
    读取命令行参数，并以pytest运行
    :return:
    """

    (options, args) = parse_option()
    env = str(options.env).split("=")[1]
    project = str(options.project).split("=")[1]
    environment_file = root_path + "/environment.txt"

    case_path = root_path + "/testcases/" + project
    report_path = root_path + "/reports/allure/xml/"

    try:
        with open(environment_file, 'w') as f:
            f.write(env)
            f.write("\n")
            f.write(project)
    except FileNotFoundError:
        print(environment_file, "File Not Found!")

    pytest.main(["-v", "-s", "--alluredir", report_path, case_path])


if __name__ == "__main__":
    main()
