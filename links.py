from readFile import read_file
from klasa import Links

def get_links_data():
    data = read_file("data/links.csv")
    links = []
    for link in data.split('\n'):
        if len(link) and "movieId" not in link:
            link = link.split(',')
            links.append(link)
    return links

def get_links():
    print(get_links_data())
    return [Links(link[0], link[1], link[2]).__dict__ for link in get_links_data()]


