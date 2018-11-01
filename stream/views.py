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
        number = request.GET['number']
    except Exception as e:
        print("ERROR")
        print(e)
        number = 1

    try:
        myhref = request.GET['myhref']
        driver.get(myhref)
        return HttpResponse("Done")
    except:
        pass
    driver.fullscreen_window()

    try:
        titles = driver.find_elements_by_id('video-title')
    except Exception as e:
        return HttpResponse("Error: {}".format(e))

    title = titles[int(number)-1]
    title.click()
    return HttpResponse("Done")
