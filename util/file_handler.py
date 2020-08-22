# coding:utf-8

import csv


def csv_reader(filename):
    try:
        with open(filename, 'r') as f:
            content = csv.DictReader(f)
            data = [row for row in content]
            return data
    except FileNotFoundError:
        print(filename, "File Not Found!")
        return -1


def csv_writer(filename):
    pass


def json_reader(filename):
    pass

