from bs4 import BeautifulSoup
import requests

def main():
    #url = "https://m.timesjobs.com/mobile/jobs-search-result.html?txtKeywords=Python+developer&cboWorkExp1=-1&txtLocation="
    url = "https://m.timesjobs.com/mobile/jobs-search-result.html?txtKeywords=Devops%2C&cboWorkExp1=-1&txtLocation="
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
    jobs = soup.find_all("ul",class_="ui-content search-result")

    for joblist in jobs:
        job_listing = joblist.find_all("li")
        for index, job in enumerate(job_listing):
            company_name = job.find("div", class_="srp-job-heading") 
            if not company_name:
                continue
            skillslist = job.find("div", class_="srp-keyskills").text
            #skillslist = ",".join(job.find("div", class_="srp-keyskills").text.split(" "))
            company_name = job.find("span", class_="srp-comp-name").text.replace(" ","")
            location = job.find("div", class_="srp-loc").text.replace(" ","")
            experience = job.find("div", class_="srp-exp").text.replace(" ","")
            salary = job.find("div", class_="srp-sal").text.replace(" ","")
            moreinfo = job.find("div").find("div").find_all("div")[2].find("h3").find("a")["href"]

            with open("posts.txt","a") as f:
                f.write(f"company_name: {company_name.strip()}\n")
                f.write(f"skill set: {skillslist.strip()}\n")
                f.write(f"Location: {location.strip()}\n")
                f.write(f"Experience: {experience.strip()}\n")
                f.write(f"Salary:  {salary.strip()}\n")
                f.write(f"MoreInfo: {moreinfo}\n")


            print("company_name:",company_name.strip())
            print("skill set:",skillslist.strip())
            print("Location:", location.strip())
            print("Experience:", experience.strip())
            print("Salary:", salary.strip())
            print("MoreInfo:", moreinfo)
            print("\n")
if __name__=="__main__":
    main()
