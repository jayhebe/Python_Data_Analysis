import requests
import csv
# import openpyxl
from bs4 import BeautifulSoup


def get_page_info(html_code):
    page_bs = BeautifulSoup(html_code, "html.parser")
    page_movies_info = page_bs.find_all("div", class_="item")
    page_next = page_bs.find("span", class_="next").find("a")
    if page_next is not None:
        page_next = page_next["href"]
    else:
        page_next = ""

    return page_movies_info, page_next


# wb = openpyxl.Workbook()
# sheet = wb.active
# sheet.title = "Movie top 250"
#
# sheet["A1"] = "Movie Number"
# sheet["B1"] = "Movie Link"
# sheet["C1"] = "Movie Name"
# sheet["D1"] = "Movie Rate"
# sheet["E1"] = "Movie Quote"

base_url = "https://movie.douban.com/top250"
next_page = "?start=0&filter="
url = base_url + next_page

with open("doubantop250.csv", "a+", encoding="utf8") as f_csv:
    csv_writer = csv.writer(f_csv)
    while next_page:
        # print("Processing: {}".format(url))
        page_html = requests.get(url)
        page_html.encoding = "utf8"
        movies_info, next_page = get_page_info(page_html.text)

        for movie_info in movies_info:
            # Write to Excel
            # row = list()
            # row.append(movie_info.find("em").text)
            # row.append(movie_info.find("a")["href"])
            # row.append(movie_info.find("span", class_="title").text)
            # row.append(movie_info.find("span", class_="rating_num").text)

            # Print out to console
            # print("Movie number: {}".format(movie_info.find("em").text))
            # print("Movie link: {}".format(movie_info.find("a")["href"]))
            # print("Movie name: {}".format(movie_info.find("span", class_="title").text))
            # print("Movie rate: {}".format(movie_info.find("span", class_="rating_num").text))

            # Write to csv
            row = list()
            row.append(movie_info.find("em").text)
            row.append(movie_info.find("a")["href"])
            row.append(movie_info.find("span", class_="title").text)
            row.append(movie_info.find("span", class_="rating_num").text)

            quote_tag = movie_info.find("span", class_="inq")
            if quote_tag is not None:
                row.append(movie_info.find("span", class_="inq").text)
                # print("Movie quote: {}".format(movie_info.find("span", class_="inq").text))
            # print("-" * 20)
            # sheet.append(row)
            csv_writer.writerow(row)

        url = base_url + next_page

# wb.save("doubantop250.xlsx")
