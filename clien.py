#-*- coding: utf-8 -*-
import sys
import os
reload(sys)
sys.setdefaultencoding("utf8")

import urllib2
from bs4 import BeautifulSoup
import re

import time
import webbrowser

with open('clien.html', 'w') as init_data:
        init_data.write('<meta http-equiv="Content-Type" content="text/html; charset=utf-8">\n')

def BestArticleClien(boardName, replyNumberHope):
    url = 'http://www.clien.net/cs2/bbs/board.php?bo_table=' + boardName
    html = urllib2.urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')

    for tr in soup.find_all('tr', {'class' : 'mytr'}):
        try:
            replyNumber = tr.find('span').string[1:-1]
        except:
            pass

        if replyNumber.isdigit():
            if int(replyNumber) > replyNumberHope:
                articles = tr.find('td', {'class' : 'post_subject'})
                #best_park_number = tr.td.string
                link = articles.a.get('href')
                link = link.replace('..', 'http://www.clien.net/cs2')
                title = articles.a.string
                article = ' <a href=\'' + link + '\'>' + title + '</a> [' + replyNumber + ']'

                with open('clien.html', 'a') as w:
                    if boardName == 'park':
                        w.write('모두의공원')
                    if boardName == 'lecture':
                        w.write('팁과강의')
                    if boardName == 'kin':
                        w.write('아무거나질문')
                    if boardName == 'use':
                        w.write('사용기게시판')
                    if boardName == 'cm_mac':
                        w.write('맥당')

                    w.write(article)
                    w.write('<br>\n')

def main():
    BestArticleClien('park', 10)
    BestArticleClien('lecture', 8)
    BestArticleClien('kin', 2)
    BestArticleClien('use', 10)
    BestArticleClien('cm_mac', 3)

    cwd = os.getcwd()
    clienHtml = 'file://' + cwd + '/clien.html'
    webbrowser.open_new(clienHtml)


if __name__ == '__main__':
    main()
