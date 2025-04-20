from bs4 import BeautifulSoup

with open("index.html","r") as f:
    content = f.read()
    soup = BeautifulSoup(content,"lxml")
    #print(soup.prettify())
    course_cards = soup.find_all('div', class_='card' )
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text
        course_price = course_price.split(" ")[-1]
        print(course_name+" "+course_price)
