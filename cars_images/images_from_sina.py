'''

by xlc time:2018-05-05 22:47:33
'''
import sys
sys.path.append(r'D:\mypyfunc')
import os
main_path = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
main_path = '/'.join(main_path.split('/')[:-1])
from data_trsfm import txt2lst
import urllib.request
import json
from bs4 import BeautifulSoup as bf
import time
import random

def get_images(path_name, url): # 给定url 爬取图片

    url_request = urllib.request.urlopen('http:'+url)
    data = url_request.read().decode('utf-8')
    soup = bf(data, 'lxml')
    need_data = soup.find('div', {'class':'y-tuku235 seek-list'}).find_all('li')
    count = 0
    for dt in need_data:
        img_data = dt.find('img')
        img_name = img_data['alt']
        img_site = img_data['src']
        img_rq = urllib.request.urlopen(img_site)
        img_dt = img_rq.read()
        f = open(path_name + '_' + str(count) + '.jpg', 'wb')
        f.write(img_dt)
        f.close()
        count += 1

if __name__ != '__main__':#爬源代码 txt.txt
    url = 'http://db.auto.sina.com.cn/photo/b76.html'
    url_request = urllib.request.urlopen(url)
    data = url_request.read().decode('utf-8')

if __name__ != '__main__': # 爬取车名字 cars_sites.txt
    data = open('txt.txt', 'r', encoding='utf-8').read()
    soup = bf(data, 'lxml')
    need_data = soup.find('div', {'id':'J_scrollLeter'}).find_all('li')
    big_dct = {}
    for i in need_data:
        first_alpha = i.h5.text
        dl = i.find_all('dl')
        print(first_alpha)
        medi_dct = {}
        for j in dl:
            name_medi = j.a.text
            all_a = j.find_all('a')
            dct = {}
            for k in all_a:
                name = k.text
                web_site = k['href']
                dct[name] = web_site
            medi_dct[name_medi] = dct
        big_dct[first_alpha] = medi_dct
    f = open('cars_sites.txt', 'w', encoding='utf-8')
    for i in big_dct.items(): 
        f.write(json.dumps(i, ensure_ascii=False))
        f.write('\n')
    f.close()
    
if __name__ == '__main__': # 爬取车的图片
    source_data = txt2lst('cars_sites.txt')
    source = [i[0] for i in source_data]
    source = [json.loads(i) for i in source]
    has_p = open('has_parsed.txt', 'a+', encoding='utf-8')
    has_p_url = has_p.readlines()
    has_p_url = [i.strip() for i in has_p_url]
    for i in source:
        first_name = i[0]
        if os.path.exists(main_path + '/cars_images/' + first_name):
            pass
        else:
            os.mkdir(main_path + '/cars_images/' + first_name)
        data = i[1]
        cars_xi = list(data.keys())
        for xi in cars_xi:
            if os.path.exists(main_path + '/cars_images/' + first_name + '/' + xi):
                pass
            else:
                os.mkdir(main_path + '/cars_images/' + first_name + '/' + xi)
            img_path = main_path + '/cars_images/' + first_name + '/' + xi
            real_data = list(data[xi].items()) # 有网址的数据
            for item in real_data:
                car_type = item[0]
                rq_url = item[1]
                #print(img_path + '/' + car_type, rq_url)
                try:
                    if rq_url not in has_p_url:
                        get_images(img_path + '/' + car_type, rq_url)
                        #time_lazy = random.randint(5, 50)
                        #time.sleep(time_lazy)
                        has_p_url.append(rq_url)
                        has_p.write(rq_url + '\n')
                except Exception as e:
                    print(str(e))
                    has_p.close()
    has_p.close()

