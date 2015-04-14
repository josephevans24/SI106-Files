def cool_machine(x):
     y = x**2 +7
     return y

z = 65.3
print z + cool_machine(8)



import requests

page = requests.get("https://github.com/presnick/runestone")
print page.text[:1000]


