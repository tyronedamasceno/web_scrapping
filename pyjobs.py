from bs4 import BeautifulSoup as bs
from requests import get

base_url = 'http://pyjobs.com.br'


pyjobs = get(base_url)
home_page = bs(pyjobs.text, 'html.parser')

number_of_pages = len(home_page.find_all('li', {'class':'page-item'}))

vagas = []

for i in range(number_of_pages):
    which_page = '{}/?page={}'.format(base_url, (i+1))
    pyjobs = get(which_page)
    jobs_page = bs(pyjobs.text, 'html.parser')

    boxes = jobs_page.find_all('div', {'class':'card-body'})
    
    urls = [box.find('a').get('href') for box in boxes if box.find('a')]
    
    for url in urls:
        job_url = '{}{}'.format(base_url, url)
        job = get(job_url)
        job_page = bs(job.text, 'html.parser')
        title = job_page.find('h1', {'class':'text-info'}).text
        ps = job_page.find_all('p')
        local = ps[0].text
        empresa = ps[1].text
        #print('\n{}\n{}\n{}'.format(title, local, empresa))
        vagas.append('\n{}\n{}\n{}'.format(title, local, empresa))

print(set(vagas))


