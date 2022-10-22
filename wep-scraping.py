#1st step install and import modules
from importlib.resources import as_file
import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest


jop_titles=[]
company_name=[]
location_in=[]
jop_skills=[]

#2nd step use requests to fetch the url in my linkd in or....
result=requests.get("")
#3ed step seva page content.
src=result.content
#print(src)
#4nd  step create soup object to parse content .
soup=BeautifulSoup(src,"lxml")
#print(soup)

#5nd step find the elements content info we need 
#--jop titles , jop skills , company names, location.

jop_titles=soup.find_all()

company_name=soup.find_all()

location_in=soup.find_all()

jop_skills=soup.find_all()


#6nd step loop over returned lists to needed info into other lists.
for i in range(len(company_name)):
    jop_titles.append(jop_titles[i].text)
    company_name.append(company_name[i].text)
    location_in.append(location_in[i].text)
    jop_skills.append(jop_skills[i].text)
#print(company_name,jop_skills,jop_titles,jop_titles)

#7nd step create csv file .
file_list=[jop_titles,company_name,location_in,jop_skills]
exported=zip_longest(*file_list)
while open("path") as myfile:
    wr=csv.writer(myfile)
    wr.writerow(["jop titles","company name","location","(jop skills"])
    wr.writerows(exported)
