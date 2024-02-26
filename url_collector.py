import requests
from bs4 import BeautifulSoup

def collect():
    page_counter = 1
    url_list = []

    while True:
        # Create url look at page and get all job cards
        url = "https://www.make-it-in-germany.com/en/working-in-germany/job-listings?tx_solr%5Bfilter%5D%5B0%5D=industry%3A9&tx_solr%5Bfilter%5D%5B1%5D=workingplan%3A1&tx_solr%5Bfilter%5D%5B2%5D=jobtype%3A1&tx_solr%5Bfilter%5D%5B3%5D=qualification%3A14&tx_solr%5Bpage%5D="+str(page_counter)+"#list45536"
        req  = requests.get(url)
        text = req.text
        soup = BeautifulSoup(text, "html.parser")
        jobs_list = soup.find_all(class_ = "card card--job")
        
        # If no job listing on page stop looking further
        if not len(jobs_list):
            break
        
        # Get extract url from every job card
        for j in jobs_list:
            job_str = str(j)
            pos_start = job_str.find("a href=\"https:") + 8
            if pos_start != 7 and (job_str.lower().find("software developer") != -1 or job_str.lower().find("software engineer") != -1 or job_str.lower().find("web developer") != -1):
                pos_end = job_str.find("\"", pos_start)
                url_job = job_str[pos_start:pos_end]
                url_list.append(url_job)
        page_counter += 1
    return url_list
