from django.http import HttpResponse
from django.shortcuts import render
from selenium import webdriver
import requests

from .utils import *

driver = webdriver.Chrome('/home/nouman/Downloads/chromedriver')


def show(request):
    return render(request, 'show.html')


def search(request):
    # driver.fullscreen_window()()
    if request.GET.get('action') == "SEARCH":
        search_page = requests.get('http://youtube.com/results?search_query={}'.format(request.GET['query']))
        searches = fix_and_beautify_youtube(search_page)
        return HttpResponse(searches)
    else:
        driver.get(request.GET['query'])
        return HttpResponse(status=204)


def play(request):
    try:
        myhref = request.GET['myhref']
        # driver.fullscreen_window()()
        driver.get(myhref)
        return HttpResponse(status=204)
    except Exception as e:
        return HttpResponse("Error: {}".format(e))


def skip(request):
    try:
        skip_add = driver.find_element_by_class_name("videoAdUiSkipButton")
        skip_add.click()
    except Exception as e:
        print(e)
    try:
        skip_add = driver.find_element_by_class_name("svg-close-button")
        skip_add.click()
    except Exception as e:
        print(e)
    try:
        skip_add = driver.find_element_by_class_name("ytp-ad-overlay-close-button")
        skip_add.click()
    except Exception as e:
        print(e)
    return HttpResponse(status=204)


def fullscreen(request):
    try:
        pause = driver.find_element_by_class_name("video-stream")
        pause.click()
        fullscreen_button = driver.find_element_by_class_name("ytp-fullscreen-button")
        fullscreen_button.click()
        pause = driver.find_element_by_class_name("video-stream")
        pause.click()
    except Exception as e:
        print(e)
    return HttpResponse(status=204)


def mute(request):
    try:
        mute = driver.find_element_by_class_name("ytp-mute-button")
        mute.click()
    except Exception as e:
        print(e)
    return HttpResponse(status=204)


def pause(request):
    try:
        pause = driver.find_element_by_class_name("video-stream")
        pause.click()
    except Exception as e:
        print(e)
    return HttpResponse(status=204)
