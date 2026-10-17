import json 
import httpx
name = '{"Name": "Olena","Age": 20, "Student": True}'
person = json.loads(name)
print(person["name"],type(person))
print(person["Age"], person["Student"])

info = {"city": "Київ", "tags": ["IT", "кава"]}
print(json.dumps(info, ensure_ascii=False, indent=2))

url = "https://jsonplaceholder.typicode.com/todos"
responce = httpx.get(url, params={"userId": 1}, timeout=10)
print("Code: ", responce.status_code)
todos = responce.json()
print("Tasks: ", len(todos))
