# coding: utf-8

from mako.template import Template
print(Template("hello ${data}!").render(data="world"))