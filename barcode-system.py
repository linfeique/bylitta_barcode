from barcode import writer
import shortuuid
import csv
from barcode import EAN13
from barcode.writer import ImageWriter
from pathlib import Path
import os

cloth_name = input("Qual o nome do conjunto?\n")

qtd_colors = input("Quantas cores esse produtos tem?\n")
qtd_sizes = input("Quantos tamanhos esse produto tem?\n")

x = 1 * int(qtd_colors) * int(qtd_sizes)

if os.path.exists("/files"):
    file = open("files/file.csv", "w", encoding='UTF8')        
else:
    os.mkdir("files")
    file = open("files/file.csv", "w", encoding='UTF8')

if not os.path.exists("/images"):
    os.mkdir("images")

for x in range(0, x):
    numbers = shortuuid.ShortUUID(alphabet="1234567890").random(length=12)

    writer = csv.writer(file)

    header = ["Nome", "Número Imagem", "Código de barras"]
    data = [cloth_name, x, numbers]

    writer.writerow(data)

    barcode = EAN13(numbers, writer=ImageWriter())
    barcode.save(f"images/{cloth_name}_{x}_codigo")

file.close()