with open("paginaweb2.html", "w") as arq:
    arq.write("<html>")
    arq.write("<head><title>HTML em Python</title></head>")
    arq.write("<body>")

    lista = ["Dom","Seg","Ter","Qua"]
    arq.write("<ul>")
    for e in lista:
        arq.write(f"<li>{e}</li>")
    arq.write("</ul>")

    arq.write("</body")
    arq.write("</html>")