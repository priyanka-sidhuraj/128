#enter to venv to check the ouput and put the downloaded chromedriver  in vs
from bs4 import BeautifulSoup
import requests,openpyxl
import re

excel=openpyxl.Workbook()
sheet=excel.active
sheet.title="Movies List2"
sheet.append([' Movie Name','Year','IMDB Rating','Story','Director','Gross'])


try:
  response=requests.get("https://www.imdb.com/search/title/?genres=adventure&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=RHKQH1CANBRWH8NNF26M&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_2")
  soup=BeautifulSoup(response.text,'html.parser')
  movies=soup.find("div",class_="lister-list").find_all("div",class_="lister-item")
 
  for movie in movies:
  #  print(movie)
    name=movie.find('h3').a.text
    year=movie.find('h3').find('span',class_='lister-item-year').text
    year=re.sub("\D","",year)
    rate=movie.find('div',class_='ratings-imdb-rating').strong.text
    story=movie.find("p").findNext("p").get_text(strip=True)
    director=movie.find("p").findNext("p").findNext("p").a.text
    gross=movie.find("p",class_="sort-num_votes-visible").find_all("span")[-1].get_text()
   # print(index,name,year,rate,story,director,gross)
sheet.append([name,year,rate,story,director,gross])
 #   break

except Exception as e:
    print(e)

excel.save("scrapper2.xlsx")