# Ajex透過瀏覽器訪問網頁，網頁會回傳沒有資料的HTML內容。
# 接著瀏覽器的JavaScript會執行，然後再發出AJAX請求，獲取json資料。
#javaScript會將資料渲染到網頁上。

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://api.hahow.in/api/products/search?category=COURSE&limit=8&mixedResults=false&page=0&sort=TRENDING"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    data = response.json()
    # print(data['data']['courseData']['products'])
    products = data['data']['courseData']['products']
    course_list = []
    for product in products:
        course_data = [
        product['title'],
        product['price'],
        product['averageRating'],
        product["numSoldTickets"],
        ]
        course_list.append(course_data)
    df = pd.DataFrame(course_list, columns=["課程名稱", "價格", "評分", "購買人數"])
    df.to_excel("courses.xlsx", index=False, engine="openpyxl")
else:
    print("無法取得網頁")
