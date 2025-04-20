from bs4 import BeautifulSoup
import requests


url = "https://m.timesjobs.com/mobile/jobs-search-result.html?txtKeywords=Python+developer&cboWorkExp1=-1&txtLocation="
cookies = {
    "JSESSIONID": "",
    "MSESSIONID": "",
    "ACEGI_SECURITY_HASHED_REMEMBER_ME_COOKIE": "",
    "FULLY_COOKIE_KEY": "",
    # You can include others if needed
}

headers = {
    "User-Agent": "Mozilla/5.0",
    # "Authorization": "Bearer xyz",  # if required
}
session = requests.Session()
response = session.get(url, cookies=cookies, headers=headers)



html_text = response.text

soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find("div",class_="clearfix srp-heading")

company_name = jobs.find("div", class_="srp-job-heading")
skillslist = soup.find("div", class_="srp-keyskills").text
company_name = company_name.find("span", class_="srp-comp-name").text.replace(" ","")

locationtag = soup.find("div",class_="clearfix exp-loc")
location = locationtag.find("div", class_="srp-loc").text
experience = locationtag.find("div", class_="srp-exp").text
salary = locationtag.find("div", class_="srp-sal").text






print("company_name:",company_name.strip())
print("skill set:",skillslist.strip())
print("Location:", location.strip())
print("Experience:", experience.strip())
print("Salary:", salary.strip())
