'''

by xlc time:2018-05-05 22:47:33
'''
import sys
sys.path.append(r'G:\Github_codes\mypyfunc')
import os
main_path = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
main_path = '/'.join(main_path.split('/')[:-1])
from data_trsfm import txt2lst
import urllib.request
import json
from bs4 import BeautifulSoup as bf

def get_images(url): # 给定url 爬取图片
    url_request = urllib.request.urlopen('http:'+url)
    data = url_request.read().decode('utf-8')
    f = open('result.txt', 'w', encoding='utf-8')
    f.write(data)
    f.close()

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
            real_data = list(data[xi].items()) # 有网址的数据
            for item in real_data:
                car_type = item[0]
                rq_url = item[1]
                get_images(rq_url)
            break
        break
