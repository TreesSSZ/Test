"""
堆糖数据网页
爬虫堆糖
进入网页找到想爬去的数据  F12进入到开发者模式找到Network里的XHR
滑动找到Name数据Headers里面的request URL
Request URL: https://www.duitang.com/napi/blog/list/by_search/?kw=%E8%B5%B5%E4%B8%BD%E9%A2%96&type=feed&include_fields=top_comments%2Cis_root%2Csource_link%2Citem%2Cbuyable%2Croot_id%2Cstatus%2Clike_count%2Clike_id%2Csender%2Calbum%2Creply_count%2Cfavorite_blog_id&_type=&start=24&_=1611214640146

ASCII码   -Url编码 -中文转码
Request URL:
https://www.duitang.com/napi/blog/list/by_search/?kw=
%E8%B5%B5%E4%B8%BD%E9%A2%96&type=feed&include_fields=top_comments%2Cis_root%2Csource_link
%2Citem%2Cbuyable%2Croot_id%2Cstatus%2Clike_count%2Clike_id%2Csender%2Calbum%2Creply_count
%2Cfavorite_blog_id&_type=&start=24&_=1611214640146

kw=赵丽颖 以&来分割  kw=%E8%B5%B5%E4%B8%BD%E9%A2%96&
https://www.duitang.com/napi/blog/list/by_search/?kw=%E8%B5%B5%E4%B8%BD%E9%A2%96&start=24&limit=1000

在第24张开始start=24&limit=10001000是设置存1000张  1000张结束
 点来链接里的"total":3600最设置现在最多图片
"""


import  requests
from urllib.request import urlretrieve
picture =[]
url = "https://www.duitang.com/napi/blog/list/by_search/?kw=%E8%B5%B5%E4%B8%BD%E9%A2%96&start=24&limit=1000"
start1 = '"path":"'
end_1 = '"'

#张数
num = 0
#下载地址
local =  'D:\\Codes\\Python\\Foundation\\堆糖数据网页\\'
#同时显示下载的进度函数
def callbackfunc(blocknum, blocksize, totalsize):
    '''回调函数
    @blocknum: 已经下载的数据块
    @blocksize: 数据块的大小
    @totalsize: 远程文件的大小
    '''
    percent = 100.0 * blocknum * blocksize / totalsize
    if percent > 100:
        percent = 100
    print("%.2f%%"% percent)

for i in range(0,3600,100):
    url_2=url.format(i)
    H5 = requests.get(url_2).content.decode("utf-8")
    picture.append(H5)
for j in picture:
    end = 0
    while j.find(start1, end) != -1:
        start = j.find(start1, end)+len(start1)
        end = j.find(end_1, start)
        url_ing = j[start:end]
        num +=1
        #下载第几张后缀
        img_name = str(num) + '.jpg'
        #下载路径拼接
        img2_name =local+img_name
        urlretrieve(url_ing,img2_name,callbackfunc)
        #  函数1是外部或者本地url，函数2是指定了保存到本地的路径，函数3显示当前的下载进度。
        print('打印第', num, '张成功！')

