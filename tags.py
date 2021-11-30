from readFile import read_file
from klasa import Tags

def get_tags_data():
    data = read_file("data/tags.csv")
    tags = []
    for tag in data.split('\n'):
        if len(tag) and "userId" not in tag:
            tag = tag.split(',')
            tags.append(tag)
    return tags

def get_tags():
    print(get_tags_data())
    return [Tags(tag[0], tag[1], tag[2], tag[3]).__dict__ for tag in get_tags_data()]