import os
from http.cookies import SimpleCookie
from templates import login_page, secret_page, after_login_incorrect
import cgi
import cgitb
import json
cgitb.enable()
import secret

# create login form
s = cgi.FieldStorage()
username = s.getfirst("username")
password = s.getfirst("password")

form = username == secret.username and password == secret.password

c = SimpleCookie(os.environ["HTTP_COOKIE"])
if c.get("username"):
  c_username = c.get("username").value
if c.get("password"):
  c_password = c.get("password").value

cookie = c_username == secret.username and c_password == secret.password

if cookie:
    username = c_username
    password = c_password

if form:
    print(f"Set-Cookie: username={username}")
    print(f"Set-Cookie: password={password}")

if not username and not password:
    print(login_page())
elif username == secret.username and password == secret.password:
    print(secret_page(username, password))
else:
    print(after_login_incorrect())
