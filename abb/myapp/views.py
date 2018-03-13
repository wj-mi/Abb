# -*-coding:utf-8 -*-
# @autor: wangjuan
# @time: 2018-03-11:10:00

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def say_hello(request):
    """say　hello"""
    return HttpResponse('hello')
