import requests
import ssl

nMethod = 1
 
print("================================================")

api_url = "https://127.0.0.1:8804/api/Director/GetTotal"
api_url1 = "https://192.168.0.165:8804/api/Director/GetTotal"
api_url3 = "https://localhost:8804/api/Director/GetTotal"
response = requests.get(api_url,verify=False)

if response.status_code == 200:
   print('Success')
elif response.status_code == 404:
   print('Not Found')
print('Result: '+str(response.status_code))   
print('-- content: '+str(response.content))   
