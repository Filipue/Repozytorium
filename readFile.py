def read_file(path):
    f = open(path, encoding="utf-8")
    data = f.read()
    f.close()
    return data