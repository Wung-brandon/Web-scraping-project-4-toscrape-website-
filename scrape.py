import requests
from bs4 import BeautifulSoup
import pandas as pd


#scraping 50 pages
books = []
for i in range(1, 51):
    url = f"http://books.toscrape.com/catalogue/category/books_{i}/index.html"
    response = requests.get(url)
    book_html = response.text

    soup = BeautifulSoup(book_html, "html.parser")

    #ol = soup.find("ol")
    #print(ol)
    articles = soup.find_all("article", class_="product_pod")
    #print(articles)
    for article in articles:
        image = article.find("img")
        title = image.attrs["alt"]
        star = article.find("p")
        star = star["class"][1]
        #print(star)
        price = article.find("p", class_="price_color").text
        price1 = price[1:]
        #print(price1)
        books.append([title, price1, star])
    #print(books)

column = ["Title", "Price", "Star Rating"] 
df = pd.DataFrame(books, columns=column)
df.to_csv("Books.csv", index=False)