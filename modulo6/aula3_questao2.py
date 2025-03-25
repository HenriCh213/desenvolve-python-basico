URLs = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]
dominio = []

for n in URLs:
    domain = n[4:-4]
    dominio.append(domain)

print(dominio)