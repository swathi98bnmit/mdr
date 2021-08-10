# from mdr import MDRClassifier
# import pandas as pd
#
# genetic_data = pd.read_csv('https://github.com/EpistasisLab/scikit-mdr/raw/development/data/GAMETES_Epistasis_2-Way_20atts_0.4H_EDM-1_1.tsv.gz', sep='\t', compression='gzip')
#
# features = genetic_data.drop('class', axis=1).values
# labels = genetic_data['class'].values
#
# my_mdr = MDRClassifier()
# my_mdr.fit(features, labels)
# print(my_mdr.score(features, labels))


# from bs4 import BeautifulSoup
# import requests as req
# Web = req.get('https://festive-knuth-1279a2.netlify.app/')
# S = BeautifulSoup(Web.text, 'lxml')
# print(S.prettify())
# for TraverseTags in S.recursiveChildGenerator():
#   # Traversing the names of the tags
#     if TraverseTags.name:
#       # Printing the names of the tags
#         print(TraverseTags.name)
# Attr = S.html
# # Using the Children attribute to get the children of a tag
# # Only contain tag names and not the spaces
# Attr_Tag = [e.name for e in Attr.children if e.name is not None]
# print(Attr_Tag)

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

import requests
from bs4 import BeautifulSoup
url = "https://www.atptour.com/en/rankings/singles"
# url = "https://www.amazon.com/s?k=laptops&ref=nb_sb_noss_1"
response = requests.get(url)
page = response.text
soup = BeautifulSoup(page, 'lxml')
table = soup.find(class_="mega-table")
[row.text.split() for row in table.find_all("tr")]
print(table)
header = [j for j in [i.strip("  ") for i in table.find_all("tr")[0].text.splitlines()] if j != ""]
header.remove("Country")
header.remove("Move")
data = []
for row in table.find_all("tr")[1:]:
    x = row.text.split()
    name = " ".join(i for i in x if i.isalpha() or "-" in i)
    res = [i for i in x if not (i.isalpha() or "-" in i)]
    res.insert(1, name)
    if len(res) == 8:
        res.pop(2)
    data.append(res)
rankings2 = pd.DataFrame(data, columns=header)
print(rankings2)

