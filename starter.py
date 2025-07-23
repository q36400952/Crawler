from wsgiref import headers
import os
import requests
from bs4 import BeautifulSoup


def download_image(url, save_path):
    response = requests.get(url)
    with open(save_path, "wb") as file:
        file.write(response.content)

def main():
    url = "https://www.ptt.cc/bbs/Beauty/M.1686997472.A.FDA.html"
    # 設定Cookie以確認年齡
    headers = {"Cookie": "over18=1"}
    response = requests.get(url, headers = headers)
    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup.prettify())
    spans = soup.find_all("span", class_="article-meta-value")
    title = spans[2].text

    #建立圖片資料夾
    dir_name = f"images/{title}"
    if not os.path .exists(dir_name):
        os.makedirs(dir_name)

    # 找到網頁中所有圖片
    links = soup.find_all("a")
    allow_file_name = ["jpg", "png", "gif", "jpeg"]
    for link in links:
        href = link.get("href")
        if not href:
            continue
        file_name = href.split("/")[-1]
        extension = href.split(".")[-1].lower()
        if extension in allow_file_name:
            print(f"file name:{extension}")
            print(f"url: {href}")
            download_image(href, f"{dir_name}/{file_name}")

        # print(href)


if __name__ == "__main__":
    main()