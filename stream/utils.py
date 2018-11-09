import re


def fix_and_beautify_youtube(search_page):
    out_html = str(search_page.content) \
        .replace('href="/watch?v=', 'href="play?myhref=http://www.youtube.com/watch?v=') \
        .replace('\\n', '')
    searches = re.search('<ol [^>]+ class="item-section">.+</ol>', str(out_html)).group()
    searches = re.sub('<ol', '<li', searches)
    searches = re.sub('/ol>', '/li>', searches)
    searches = re.sub('<span class="thumb-menu dark-overflow-action-menu video-actions">[^/]+</span>', '', searches)
    searches = re.sub(
        '<ul class="watch-queue-thumb-menu yt-uix-button-menu yt-uix-button-menu-dark-overflow-action-menu hid">((?!/ul.).)+/ul>',
        '', searches)
    searches = re.sub('<div class="yt-lockup-dismissable yt-uix-tile">',
                      '<div class="yt-lockup-dismissable yt-uix-tile" style="display: flex;font-size: 15px">', searches)
    searches = re.sub('<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">',
                      '<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" style="height: 20px; overflow: hidden;">',
                      searches)
    searches = re.sub('src[^>]+data-thumb', 'src', searches)
    searches = re.sub('data-thumb="', 'src="', searches)
    searches = re.sub('<img', '<img style="height: 220px;width: 365px;margin-right: 10px;"', searches)
    searches = re.sub('<span class="video-time" aria-hidden="true">[^<]+</span>', '', searches)
    searches = re.sub('<li><div class="search-refinements((?!</div></li>.).)+</div></li>', '', searches)
    searches = re.sub('<li><div class="pyv-afc-ads-container"((?!</div></li>.).)+</div></li>', '', searches)
    searches = re.sub('<h3 class="yt-lockup-title\s*">',
                      '<h3 class="yt-lockup-title\s*" style="font-size:30px; height:100px; width: 100%; margin:0px 10px 10px 0px; overflow: hidden">',
                      searches)
    searches = re.sub('class="yt-lockup-thumbnail yt-pl-thumb"', 'class="yt-lockup-thumbnail yt-pl-thumb" style="width: 365px;"', searches)
    searches = re.sub('<li class="yt-lockup-playlist-item clearfix"((?!</li>.).)+</li>', '', searches)
    searches = re.sub('<li', '<li style="list-style-type: none;"', searches)
    searches = re.sub('class="yt-lockup-content"','class="yt-lockup-content" style="width: 60%"', searches)
    print(searches)
    searches = get_nav_bar() + searches
    return searches


def get_nav_bar():
    with open('templates/nav_bar.html') as htmlFile:
        html = htmlFile.read()

    return html
