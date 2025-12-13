
import requests
# 100-199 info
# 200-299 success
# 300-399 redirect
# 400-499 user error
# 500-599 server error
# get put patch delete 
api_url= "https://jsonplaceholder.typicode.com/users"
response = requests.get(api_url)
data = response.json()

data.append({"name": "John Doe", "username": "johndoe", "email":input("Enter email: ")})
print("User List: data")

# https://github.com/Demiade-David/Batistuta.goal