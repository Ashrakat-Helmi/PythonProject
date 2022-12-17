import requests
from bs4 import BeautifulSoup
pageNum=1
while True:
    if(pageNum >75):
        break;
    else:
        urlConnect= requests.get(f'https://www.flexjobs.com/search?location=&page={pageNum}&search=Web+Development')

        webpage = urlConnect.content
        soup = BeautifulSoup(webpage,"html.parser")
        result = soup.find(id="job-list")

        jobElements =result.find_all("div",class_="col-md-12 col-12")

        for jobElement in jobElements:
            jobTitle= jobElement.find("a",class_="job-title job-link")
            jobLocation = jobElement.find("div", class_="col pe-0 job-locations text-truncate")
            jobTime = jobElement.find("span",class_="job-tag d-inline-block me-2 mb-1")
            jobPostesTime = jobElement.find("div",class_="job-age")
            jobDescription = jobElement.find("div",class_="job-description")
            print(jobTitle.text.strip()," , ",jobLocation.text.strip()," , ",jobTime.text.strip()," , ",jobPostesTime.text.strip()," , ",jobDescription.text.strip())
        pageNum+=1
