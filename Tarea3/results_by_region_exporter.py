class ResultsByLocalExporter:
    def __init__(self,data,filename,local):
        self.data = data
        self.filename = filename
        self.local = local
    


    def export(self):
    
        candidatos = []
        lista_ordenada = []
        for element in self.data:
            if element["candidato"] not in candidatos:
                candidatos.append(element["candidato"])
        for candidato in candidatos:
            contador = 0
            for element in self.data:
                if element["local"] == self.local and element["candidato"] == candidato:
                    contador += element["votos tricel"]
            lista_ordenada.append([candidato,contador])
        with open(self.filename,"w",encoding = "utf-8") as archivo:
            for linea in lista_ordenada:
                archivo.write(linea[0])
                archivo.write(" ")
                archivo.write(str(linea[1]))
                archivo.write("\n")
        