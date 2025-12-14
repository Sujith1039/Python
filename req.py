import requests

response = requests.get("https://api.github.com/repos/COMMCLASROOMOP/COMMCLASSROOMOP/pulls")

print(response.json())

