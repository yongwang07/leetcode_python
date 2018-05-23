from bs4 import BeautifulSoup
import requests
import json
import re
import csv
from urllib.request import urlretrieve
from functools import partial
from urllib.parse import urlparse, urljoin
import codecs
import pymongo

class UrlManager:
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def has_new_url(self):
        return self.new_url_size() != 0

    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def new_url_size(self):
        return len(self.new_urls)

    def old_url_size(self):
        return len(self.old_urls)


class HtmlDownloader:
    @staticmethod
    def download(url):
        if url is None:
            return None
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = {'User-Agent': user_agent}
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            r.encoding = 'utf-8'
            return r.text
        return None


class HtmlParser:
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    @staticmethod
    def _get_new_urls(page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r'/view/\d+\.htm'))
        for link in links:
            new_url = link['href']
            new_full_url = urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    @staticmethod
    def _get_new_data(page_url, soup):
        data = {'url': page_url}
        title = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        data['title'] = title.get_text()
        summary = soup.find('div', class_='lemma-summary')
        data['summary'] = summary.get_text()
        return data


class DataOutput:
    def __init__(self):
        self.datas = []

    def store_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = codecs.open('baike.html', 'w')
        fout.write('<html>')
        fout.write('<body>')
        fout.write('<table>')
        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>' % data['url'])
            fout.write('<td>%s</td>' % data['title'])
            fout.write('<td>%s</td>' % data['summary'])
            fout.write('</tr>')
            self.datas.remove(data)
        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')
        fout.close()

class SpiderMan:
    def __init__(self):
        self.manager = UrlManager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = DataOutput()

    def crawl(self, root_url):
        self.manager.add_new_url(root_url)
        while self.manager.has_new_url() and self.manager.old_url_size() < 100:
            try:
                new_url = self.manager.get_new_url()
                html = self.downloader.download(new_url)
                new_urls, data = self.parser.parse(new_url, html)
                self.manager.add_new_urls(new_urls)
                self.output.store_data(data)
                print('already catch %s links' % self.manager.old_url_size())
            except Exception as e:
                print('crawl failed')
        self.output.output_html()


def Schedule(filename, block_num, block_size, total_size):
    per = 100.00 * block_num * block_size / total_size
    if per > 100:
        per = 100
    print('{0} => current download: {1:.2f}%'.format(filename, per))


if __name__ == '__main__':
    client = pymongo.MongoClient('localhost', 27017)
    import datetime
    db_book = client.book.books
    db_book.find_one()
    '''
    spider_man = SpiderMan()
    spider_man.crawl('http://baike.baidu.com/view/284853.htm')
    
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}
    r = requests.get('http://www.ivsky.com/tupian/ziranfengguang', headers=headers)
    html = BeautifulSoup(r.text, 'html.parser')
    imgs = html.find_all('img')
    i = 0
    for img in imgs:
        filename = 'img' + str(i) + '.jpg'
        urlretrieve(img['src'], filename, partial(Schedule, filename))
        i += 1

    headers = ['ID', 'UserName', 'Password', 'Age', 'Country']
    rows = [(1001, 'qiye', 'qiye_pass', 24, 'China'),
            (1002, 'Mary', 'Mary_pass', 20, 'USA'),
            (1003, 'Jack', 'Jack_pass', 20, 'USA')]
    with open('qiye.csv', 'w', newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rows)
    with open('qiye.csv') as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        Row = namedtuple('Row', headers)
        print('header=', headers)
        for r in f_csv:
            row = Row(*r)
            print(row.UserName, row.Password)
    
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}
    r = requests.get('http://seputu.com/', headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    rows = []
    pattern = re.compile(r'\s*\[(.*)\]\s+(.*)')
    for mulu in soup.find_all(class_='mulu'):
        h2 = mulu.find('h2')
        if h2 is not None:
            h2_title = h2.string
            for a in mulu.find(class_='box').find_all('a'):
                href = a.get('href')
                box_title = a.get('title')
                match = pattern.match(box_title)
                if match is not None:
                    date = match.group(1)
                    title = match.group(2)
                    print(h2_title, title, href, date)
                    rows.append((h2_title, title, href, date))
    headers = ['title', 'title', 'href', 'date']
    with open('qiye.csv', 'w', newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rows)
    with open('qiye.csv', 'r') as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        for r in f_csv:
            print('r>>', r)
        
    with open('qiye.json', 'w') as fp:
        json.dump(content, fp=fp, indent=4)
    
    with open('qiye.json', 'r') as fp:
        s = json.load(fp=fp)
        print(s)
    '''
#