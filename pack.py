path = "./gabusmod/addoninfo.txt"

f = open(path, "rb")
content = f.read().decode("ISO-8859-1", "ignore")
f.close()

f = open(path, "w", encoding="utf-8")
f.write(content)
f.close()