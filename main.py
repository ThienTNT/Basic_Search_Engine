import requests
from bs4 import BeautifulSoup
all_link = []       # Suitable link list
all_search = []     # Search in single link


def count_word(string1, string2):
    count = 0
    index_find = -1
    for i in range(len(string1)):
        count += 1
        index_find = string1.lower().find(string2.lower(), index_find+1)
        if index_find == -1:
            count -= 1
            break
    return count


print("Code done!!!")
