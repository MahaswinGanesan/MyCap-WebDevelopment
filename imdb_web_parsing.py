import requests
from bs4 import BeautifulSoup
import sqlite3
values=[]
connection=sqlite3.connect("tamil_films.bd")
cursor=connection.cursor()
connection.execute('''CREATE TABLE movies (Rank INT,Movie TEXT,Year INT,IMDB_Rating FLOAT)''')

url="https://www.imdb.com/india/top-rated-tamil-movies/"
req=requests.get(url)
content=req.content
soup=BeautifulSoup(content,"html.parser")

all_movies=soup.find("tbody",class_="lister-list")
all_movies=all_movies.find_all("tr")

    for movies in all_movies:
        
        rank = movies.find("td",class_="titleColumn").get_text(strip=True).split('.')[0]
        movie = movies.find("td",class_="titleColumn").a.text
        year = movies.find("span",class_="secondaryInfo").text.replace('(','')
        year = year.replace(')','')
        rating = movies.find("td",class_="ratingColumn imdbRating").text
        connection=sqlite3.connect("tamil_films.bd")
        cursor=connection.cursor()
        cursor.execute('''INSERT INTO movies VALUES (?,?,?,?)''',(rank,movie,year,rating))
      
connection.commit()
connection.close()

print("Table created and data are inserted successfully")
