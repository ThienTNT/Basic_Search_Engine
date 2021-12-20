import requests
from bs4 import BeautifulSoup
from googlesearch import search


def count_word(string1, string2):
    count = 0
    index_find = -1
    for single in range(len(string1)):
        count += 1
        index_find = string1.lower().find(string2.lower(), index_find+1)
        if index_find == -1:
            count -= 1
            break
    return count


def get_info(search_box, number):
    for url in search(search_box, tld="co.in", num=number, stop=number, pause=2):
        try:
            r = requests.get(url)
            soup = BeautifulSoup(r.text, "lxml")
            title = soup.find('title').text.strip()
            description = soup.get_text()
        except Exception as e:
            # print(e)
            continue
        search_page = count_word(description, search_box)
        More_specific.append([search_page, title, url])


Search_box = "Bill gate"
More_specific = []
get_info(Search_box, 20)
More_specific.sort(reverse=True)
for Result, Title, Link in More_specific:
    print(f"{Title} URL: {Link}")
    if Result == 0:
        print("Found nothing but maybe relevant")
    elif Result == 1:
        print("Found 1 result")
    else:
        print(f"Found {Result} results")
print(f"\n***Total results: {len(More_specific)}")
