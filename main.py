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


def crawling(url, depth):
    # Setup variables
    count = -1          # Count total link crawl
    repeat_link = []    # Repeat link list
    nothing_count = 0   # Count KeyError + invalid link
    if len(all_link) == 0:
        all_link.append(url)

    # Startup
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        links = soup.find_all('a')
        title = soup.find('title').text.strip()
        print(f"{title} --Url: {url}, at depth: {depth}")
    except Exception as e:
        print(e)
        return

    description = soup.get_text()
    search_page = count_word(description, Search_box)
    print(f"Found {search_page} results")

    # Check if reach specific depth
    if depth == 0:
        # print("Code completed")
        return
    # print("Loop begin")

    # Check and fix every single link
    for link in links:
        count += 1      # Count total link
        flag = 0        # Flag check have "/" or repeat link

        # Limit link output
        if count == 10:
            break

        try:
            # Get domain name from url
            domain_name = url.split('//')[0] + "//" + url.split('//')[1].split('/')[0]
            # Check if href is link or not
            if 'http' not in link['href']:
                # Check if this link is valid
                if link['href'][0] != '/':
                    flag = 1
                new_url = domain_name + link['href']
                # Check if link is repeated
                for i in range(len(all_link)):
                    if new_url == all_link[i]:
                        flag = 1
                    if flag == 1:
                        break
                # Separate link into two category
                if flag == 0:
                    all_link.append(new_url)
                    # print(f"{new_url} at depth {depth}")
                    crawling(new_url, depth-1)
                else:
                    repeat_link.append(new_url)
                # print(new_url)
            else:
                new_url = link['href']
                # Check if link is repeated
                for i in range(len(all_link)):
                    if new_url == all_link[i]:
                        flag = 1
                    if flag == 1:
                        break
                # Separate link into two category
                if flag == 0:
                    all_link.append(new_url)
                    # print(f"{new_url} at depth {depth}")
                    crawling(new_url, depth-1)
                else:
                    repeat_link.append(new_url)
                # print(new_url)
        except KeyError:
            nothing_count += 1
            pass
        except IndexError:
            print("IndexError appear")
            pass

    # Output count and depth
    print(f"Total invalid: {nothing_count + len(repeat_link)}. Depth: {depth}\n")
    return


start_url = 'https://stardewvalleywiki.com/Stardew_Valley_Wiki'
# start_url = 'https://vi.wikipedia.org/wiki/Wikipedia'
# start_url = 'https://www.timesjobs.com/'
Depth_crawl = 2
Search_box = "Stardew valley"

# Start first crawl
crawling(start_url, Depth_crawl)
print(f"\n***Total link: {len(all_link)}")

print("Code done!!!")
