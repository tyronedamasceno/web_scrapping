from bs4 import BeautifulSoup as bs
from requests import get

base_url = 'http://pyjobs.com.br'
jobs = '{}/?page='.format(base_url)

pyjobs = get(jobs)
pyjobs_page = bs(pyjobs.text, 'html.parser')

boxes = pyjobs_page.find_all('div', {'class':'card-body'})

urls = []
for box in boxes:
    x = box.find('a')
    if x:
        urls.append(x.get('href'))    

for url in urls:
    job_url = '{}{}'.format(base_url, url)
    job = get(job_url)
    job_page = bs(job.text, 'html.parser')
    print(job_page.find('h1', {'class':'text-info'}))

