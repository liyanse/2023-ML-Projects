from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://www.indeed.com/jobs?q=data+scientist&l=United+States&vjk=5da2f81acefb9c8c"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

lists = soup.find_all('div', class_="cardOutline tapItem fs-unmask result job_5da2f81acefb9c8c saved resultWithShelf sponTapItem desktop vjs-highlight css-kyg8or eu4oa1w0")

with open('requirements.csv','w',encoding='utf8',newline='')as f:
    thewriter = writer(f)
    header = ['Title', 'Company', 'Location', 'Salary', 'Requirements']
    thewriter.writerow(header)

    for list in lists:
        title = list.find('a', class_="jcs-JobTitle css-jspxzf eu4oa1w0").text.replace('\n', "")
        company = list.find('span', class_="companyName").text.replace('\n', "")
        location = list.find('div', class_="companyLocation").text.replace('\n', "")
        salary = list.find('span', class_="estimated-salary").text.replace('\n', "")
        requirements = list.find('tr', class_="underShelfFooter").text
        info = [title, company, location, salary, requirements]
        thewriter.writerow(info)

conda activate C:\Users\Lian.s\Anaconda3\envs\JobRequirementAnalysis
C:\Users\Lian.s\Anaconda3\Scripts\conda.exe install -p C:/Users/Lian.s/Anaconda3/envs/JobRequirementAnalysis BeautifulSoup -y
