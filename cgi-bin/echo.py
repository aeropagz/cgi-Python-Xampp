#!C:/Users/cutie/AppData/Local/Microsoft/WindowsApps/python3.exe <-------------- Path to python.exe
import sys,os
from urllib.parse import unquote


#function converts queryString to Dic
def formatParams(query):
    params = {}
    #use unquote() to convert URL-encoding back to normal
    queryString = unquote(query).split('&')
    for param in queryString:
        key, value = param.split('=')
        params[key] = value
    return params


#print resHeader and newline for resBody
print("Content-Type: text/html")
print()

#get HttpMethod
method = os.environ["REQUEST_METHOD"]

print("<h3>Method:</h3>")
print(method, "</br>")


#for GET QueryString is enviroment variable "QUERY_STRING"
if method == "GET":
    params = formatParams(os.environ["QUERY_STRING"])
#for POST QueryString is in STDIN passed by APACHE/XAMPP...
elif method == "POST":
    post = sys.stdin.read()
    params = formatParams(post)

#print Enviroment Variables
#for i in os.environ:
#    print(i+ "   " + os.environ[i] + "</br>")
print("<h3> Params: </h3>")

#print each key -> value in Params
for key in params:
    print(key +" -->  "+ params[key] + "<br>")

print("</br>")

#print params as dict
print(params)





