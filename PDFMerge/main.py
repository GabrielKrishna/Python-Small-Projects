import PyPDF2
import os

merge = PyPDF2.PdfMerger()

lista_arquivos = os.listdir("arquivos")
lista_arquivos.sort()
print(lista_arquivos)

for arquivo in lista_arquivos:
  if ".pdf" in arquivo:
    merge.append(f"arquivos/{arquivo}")

merge.write("PDFMesclado.pdf")