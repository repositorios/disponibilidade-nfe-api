# -*- coding: utf-8 -*-

import bs4
import json
import requests

api = {"status": []}
temp = []

page = requests.get("http://www.nfe.fazenda.gov.br/Portal/disponibilidade.aspx")
soup = bs4.BeautifulSoup(page.content, "html.parser")

table = soup.find("table", class_="tabelaListagemDados", id="ctl00_ContentPlaceHolder1_gdvDisponibilidade2")

for row in table.findAll("tr"):
    cells = row.findAll('td')

    temp = []  # Reset temp

    if len(cells) > 0:

        if cells[0] is not None:
            temp.append(cells[0].text)

        if cells[1].img is not None:
            if cells[1].img["src"] == "imagens/bola_verde_P.png":
                temp.append("ON")
            elif cells[1].img["src"] == "imagens/bola_vermelho_P.png":
                temp.append("OFF")
            elif cells[1].img["src"] == "imagens/bola_amarela_P.png":
                temp.append("UNSTABLE")
        else:
            temp.append("-")

        if cells[2].img is not None:
            if cells[2].img["src"] == "imagens/bola_verde_P.png":
                temp.append("ON")
            elif cells[2].img["src"] == "imagens/bola_vermelho_P.png":
                temp.append("OFF")
            elif cells[2].img["src"] == "imagens/bola_amarela_P.png":
                temp.append("UNSTABLE")
        else:
            temp.append("-")

        if cells[3].img is not None:
            if cells[3].img["src"] == "imagens/bola_verde_P.png":
                temp.append("ON")
            elif cells[3].img["src"] == "imagens/bola_vermelho_P.png":
                temp.append("OFF")
            elif cells[3].img["src"] == "imagens/bola_amarela_P.png":
                temp.append("UNSTABLE")
        else:
            temp.append("-")

        if cells[4].img is not None:
            if cells[4].img["src"] == "imagens/bola_verde_P.png":
                temp.append("ON")
            elif cells[4].img["src"] == "imagens/bola_vermelho_P.png":
                temp.append("OFF")
            elif cells[4].img["src"] == "imagens/bola_amarela_P.png":
                temp.append("UNSTABLE")
        else:
            temp.append("-")

        if cells[5].img is not None:
            if cells[5].img["src"] == "imagens/bola_verde_P.png":
                temp.append("ON")
            elif cells[5].img["src"] == "imagens/bola_vermelho_P.png":
                temp.append("OFF")
            elif cells[5].img["src"] == "imagens/bola_amarela_P.png":
                temp.append("UNSTABLE")
        else:
            temp.append("-")

        if cells[6].img is not None:
            if cells[6].img["src"] == "imagens/bola_verde_P.png":
                temp.append("ON")
            elif cells[6].img["src"] == "imagens/bola_vermelho_P.png":
                temp.append("OFF")
            elif cells[6].img["src"] == "imagens/bola_amarela_P.png":
                temp.append("UNSTABLE")
        else:
            temp.append("-")

        if cells[7].img is not None:
            if cells[7].img["src"] == "imagens/bola_verde_P.png":
                temp.append("ON")
            elif cells[7].img["src"] == "imagens/bola_vermelho_P.png":
                temp.append("OFF")
            elif cells[7].img["src"] == "imagens/bola_amarela_P.png":
                temp.append("UNSTABLE")
        else:
            temp.append("-")

        if cells[8].img is not None:
            if cells[8].img["src"] == "imagens/bola_verde_P.png":
                temp.append("ON")
            elif cells[8].img["src"] == "imagens/bola_vermelho_P.png":
                temp.append("OFF")
            elif cells[8].img["src"] == "imagens/bola_amarela_P.png":
                temp.append("UNSTABLE")
        else:
            temp.append("-")

        api["status"].append(temp)

file = open("/var/www/html/disponibilidade-nfe.json", "w")
file.write(json.dumps(api, ensure_ascii=False, indent=2))
file.close()
