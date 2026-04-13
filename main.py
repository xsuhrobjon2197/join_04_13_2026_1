1-misol
folders = ["home", "user", "documents"]
path = "/".join(folders)
print(path)

#2-misol
words = ["Python", "", "Django", None, "Api"]
result = "".join([w for w in words if w])
print(result)

#3-misol
word = "Python"
result = "-".join(word)
print(result)

#4-misol
words = ["python", "backend", "api"]
result = " | ".join([w.upper() for w in words])
print(result)

#5-misol
data = {"name": "Ali", "age": 20}
result = ", ".join(data.keys())
print(result)

#6-misol
parems = {"page": 1, "limit": 10}
query = "&".join([f"{k}={v}" for k, v in parems.items()])
print(query)

#7-misol
row = ["Ali", "20", "Tashkent"]
csv_line = ",".join(row)
print(csv_line)
