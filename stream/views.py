from django.http import HttpResponse
from django.shortcuts import render
from selenium import webdriver

driver = webdriver.Chrome('/home/nouman/Downloads/chromedriver')


def watch(request):
    url = request.GET['url']
    driver.fullscreen_window()
    driver.get(url)


def show(request):
    return render(request, 'show.html')


def search(request):
    driver.fullscreen_window()
    driver.get('http://youtube.com/results?search_query={}'.format(request.GET['query']))

    try:
        titles = driver.find_elements_by_id('video-title')
    except Exception as e:
        return HttpResponse("Error: {}".format(e))

    titles_dict = {}
    count = 0

    for title in titles:
        titles_dict[title.get_attribute('href')] = title.text
        count += 1

    return render(request, 'play.html', {"titles": titles_dict})


def play(request):
    try:
        myhref = request.GET['myhref']
        driver.fullscreen_window()
        driver.get(myhref)
        return render(request, 'show.html')
    except Exception as e:
        return HttpResponse("Error: {}".format(e))
