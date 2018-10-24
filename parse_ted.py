import pandas as pd
from bs4 import BeautifulSoup
import urllib
import codecs
import os, glob


def enlist_talk_names(path, dict):
    dict_ = {}
    r = urllib.request.urlopen(path).read()
    soup = BeautifulSoup(r, "lxml")
    talks = soup.find_all("a", class_='')
    for i in talks:
        if i.attrs['href'].find('/talks/') == 0 and dict_.get(i.attrs['href']) != 1:
            dict_[i.attrs['href']] = 1

    return dict_


allTalkNames = {}
for i in range(1, 2):
    path = 'https://www.ted.com/talks?page=%d' % (i)
    allTalkNames = enlist_talk_names(path, allTalkNames)
    print(allTalkNames)


def extract_talk(path, talk_name):
    r = urllib.request.urlopen(path).read()
    soup = BeautifulSoup(r, "lxml")
    df = pd.DataFrame()
    print(path)
    findall = soup.find_all('link')
    for i in findall:
        if i.get('href') != None and i.attrs['href'].find('?language') != -1:
            # print i.attrs['href']
            lang = i.attrs['hreflang']
            path = i.attrs['href']
            r1 = urllib.request.urlopen(path).read()
            soup1 = BeautifulSoup(r1, "lxml")
            time_frame = []
            text_talk = []
            for i in soup1.find_all('span', class_='talk-transcript__fragment'):
                time_frame.append(i.attrs['data-time'])
                text_talk.append(i.text.replace('\n', ' '))
            # print len(timeframe), len(textTalk)
            df1 = pd.DataFrame()
            df1[lang] = text_talk
            df[lang + '_time_frame'] = time_frame
            df = pd.concat([df, df1], axis=1)
    df.to_csv(talk_name + '.csv', sep='\t', encoding='utf-8')


for i in allTalkNames:
    extract_talk('https://www.ted.com' + i + '/transcript', i[7:])
    break

