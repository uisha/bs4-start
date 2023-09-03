from bs4 import BeautifulSoup
import requests
# import lmxl

# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title)
# # print(soup.title.string)
#
# # print(soup.prettify())
#
# # print(soup.p)
#
# all_anchor_tags = soup.findAll(name="a")
# # print(all_anchor_tags)
# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))

response = requests.get("https://news.ycombinator.com/news")
# print(response.text)

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
article_tags = soup.findAll(class_="titleline")
article_titles = []
article_links = []
for article in article_tags:
    title = article.find(name="a").getText()
    article_titles.append(title)
    link = article.find(name="a").get("href")
    article_links.append(link)

article_scores = [int(score.getText().split()[0]) for score in soup.findAll(class_="score")]

highest_score_index = article_scores.index(max(article_scores))
# print(article_scores)
# print(highest_score_index)

print(article_titles[highest_score_index])
print(article_links[highest_score_index])
print(article_scores[highest_score_index])