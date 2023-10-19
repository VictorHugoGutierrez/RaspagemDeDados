import os
import requests
from bs4 import BeautifulSoup

def menu():
  headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
  while True:
    os.system("cls")
    print("(1) Cotação do Dolar")
    print("(2) Cotação do Bitcoin")
    print("(3) Cotação do Libra")
    print("(4) Cotação do Peso Argentino")
    print("(5) Cotação do Ethereum")
    print("(0) Sair")
    op = int(input("Digite a opção desejada: "))

    if op == 1:
      dolar(headers)
    elif op == 2:
      bitcoin(headers)
    elif op == 3:
      libra(headers)
    elif op == 4:
      peso(headers)
    elif op == 5:
      ethereum(headers)
    else:
      os.abort()


def dolar(headers):
  link = "https://www.google.com/search?q=dolar&rlz=1C1ONGR_pt-PTBR1076BR1076&oq=dolar&gs_lcrp=EgZjaHJvbWUyCwgAEEUYJxg5GIoFMgkIARAjGCcYigUyEwgCEC4YgwEYxwEYsQMY0QMYgAQyCggDEAAYsQMYgAQyDQgEEAAYgwEYsQMYgAQyBwgFEAAYgAQyDQgGEAAYgwEYsQMYigUyDQgHEAAYgwEYsQMYgAQyDQgIEAAYgwEYsQMYgAQyDQgJEAAYgwEYsQMYgATSAQc0MzlqMGo5qAIAsAIA&sourceid=chrome&ie=UTF-8"
  request = requests.get(link, headers=headers)

  site = BeautifulSoup(request.text, "html.parser")

  dolar = site.find("span", class_="DFlfde SwHCTb")
  os.system("cls")
  print("R$ "+ dolar.get_text())
  again()


def bitcoin(headers):
  link = "https://www.google.com/search?q=bitcoin&rlz=1C1ONGR_pt-PTBR1076BR1076&oq=bitcoin&gs_lcrp=EgZjaHJvbWUyDwgAEEUYORiDARixAxiABDINCAEQABiDARixAxiABDINCAIQABiDARixAxiABDINCAMQABiDARixAxiABDINCAQQABiDARixAxiABDIQCAUQLhjHARixAxjRAxiABDIGCAYQABgDMg0IBxAAGIMBGLEDGIAEMg0ICBAAGIMBGLEDGIAEMgoICRAAGLEDGIAE0gEIMTMwM2owajmoAgCwAgA&sourceid=chrome&ie=UTF-8"
  request = requests.get(link, headers=headers)

  site = BeautifulSoup(request.text, "html.parser")

  bitcoin = site.find("span", class_="pclqee")
  os.system("cls")
  print("R$ "+ bitcoin.get_text())
  again()

def libra(headers):
  link = "https://www.google.com/search?q=libra+cota%C3%A7%C3%A3o&sca_esv=574621129&rlz=1C1ONGR_pt-PTBR1076BR1076&sxsrf=AM9HkKnqk6L17C1FllJKwhxOw4caxjgOcw%3A1697678724809&ei=hIUwZeT3MOnW1sQP-v2u8Ak&oq=libra+cota&gs_lp=Egxnd3Mtd2l6LXNlcnAiCmxpYnJhIGNvdGEqAggAMggQABiABBixAzIFEAAYgAQyBRAAGIAEMgUQABiABDIIEAAYywEYgAQyCBAAGMsBGIAEMggQABjLARiABDIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHkjKG1DrDliJE3ABeAGQAQCYAX-gAcEEqgEDMC41uAEDyAEA-AEBwgIKEAAYRxjWBBiwA8ICChAAGIoFGLADGEPCAg4QABjkAhjWBBiwA9gBAcICEBAuGIoFGMgDGLADGEPYAQLCAhYQLhiKBRjHARjRAxjIAxiwAxhD2AECwgILEAAYgAQYsQMYgwHCAgsQABiKBRixAxiDAeIDBBgAIEGIBgGQBhG6BgYIARABGAm6BgYIAhABGAg&sclient=gws-wiz-serp"
  request = requests.get(link, headers=headers)

  site = BeautifulSoup(request.text, "html.parser")

  libra = site.find("span", class_="DFlfde SwHCTb")
  os.system("cls")
  print("R$ "+ libra.get_text())
  again()

def peso(headers):
  link = "https://www.google.com/search?q=peso+cota%C3%A7%C3%A3o&sca_esv=574621129&rlz=1C1ONGR_pt-PTBR1076BR1076&sxsrf=AM9HkKnIfn5W_XMkgoAo3ZtAcEDzFrNSnQ%3A1697679251071&ei=k4cwZZTzA-DN1sQPh7m_oAI&oq=peso+cota&gs_lp=Egxnd3Mtd2l6LXNlcnAiCXBlc28gY290YSoCCAAyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIIEAAYywEYgAQyBhAAGBYYHjIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHkiSFVCRBFjSD3ABeAGQAQCYAYABoAHRBKoBAzAuNbgBA8gBAPgBAcICChAAGEcY1gQYsAPCAgoQABiKBRiwAxhDwgIHEAAYigUYQ8ICChAAGIoFGLEDGEPCAgoQLhiKBRixAxhDwgINEAAYigUYsQMYgwEYQ8ICCBAAGIAEGLEDwgILEAAYgAQYsQMYgwHiAwQYACBBiAYBkAYK&sclient=gws-wiz-serp"
  request = requests.get(link, headers=headers)

  site = BeautifulSoup(request.text, "html.parser")

  peso = site.find("span", class_="DFlfde SwHCTb")
  os.system("cls")
  print("R$ "+ peso.get_text())
  again()

def ethereum(headers):
  link = "https://www.google.com/search?q=Ethereum&rlz=1C1ONGR_pt-PTBR1076BR1076&oq=Ethereum&gs_lcrp=EgZjaHJvbWUyEQgAEEUYORhDGIMBGLEDGIoFMg8IARAAGEMYgwEYsQMYigUyDQgCEAAYgwEYsQMYgAQyBggDEAAYAzIKCAQQABixAxiABDIPCAUQABhDGIMBGLEDGIoFMg0IBhAAGIMBGLEDGIAEMg0IBxAAGIMBGLEDGIAEMgoICBAAGLEDGIAEMgkICRAAGEMYigXSAQcyNDdqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8"
  request = requests.get(link, headers=headers)

  site = BeautifulSoup(request.text, "html.parser")

  ethereum = site.find("span", class_="pclqee")
  os.system("cls")
  print("R$ "+ ethereum.get_text())
  again()

def again():
  op = input("Deseja fazer outra cotação? (S/N)\n").upper()
  if op == "S":
    os.system("cls")
    menu()
  else:
    os.abort()

menu()