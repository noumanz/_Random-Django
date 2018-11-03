from django.http import HttpResponse
from django.shortcuts import render
from selenium import webdriver
import requests

from .utils import *

driver = webdriver.Chrome('/home/nouman/Downloads/chromedriver')


def show(request):
    return render(request, 'show.html')


def search(request):
    driver.fullscreen_window()
    search_page = requests.get('http://youtube.com/results?search_query={}'.format(request.GET['query']))
    searches = fix_and_beautify_youtube(search_page)
    return HttpResponse(searches)


def play(request):
    try:
        myhref = request.GET['myhref']
        driver.fullscreen_window()
        driver.get(myhref)
        return render(request, 'show.html')
    except Exception as e:
        return HttpResponse("Error: {}".format(e))
