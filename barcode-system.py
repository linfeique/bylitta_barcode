from barcode import writer
from barcode import EAN13
import shortuuid
import csv
from barcode.writer import ImageWriter
import os

cloth_name = input("Qual o nome da peça?\n")

qtd_colors = input("Quantas cores essa peça tem?\n")
qtd_sizes = input("Quantos tamanhos essa peça tem?\n")

x = 1 * int(qtd_colors) * int(qtd_sizes)

file = NotImplemented

if os.path.isdir("files"):
	file = open("files/file.csv", "w", encoding='UTF8')
else:
	os.mkdir("files")
	file = open("files/file.csv", "w", encoding='UTF8')

if not os.path.isdir("images"):
	os.mkdir("images")
else:
  pass

for x in range(0, x):
	numbers = shortuuid.ShortUUID(alphabet="1234567890").random(length=12)

	writer = csv.writer(file)

	data = [cloth_name, x, numbers]

	writer.writerow(data)

	if not os.path.isdir(f"images/{cloth_name}"):
		os.mkdir(f"images/{cloth_name}")
	else:
			pass

	with open(f"images/{cloth_name}/{cloth_name}_{x}_codigo.jpeg", "wb") as f:
		EAN13(numbers, writer=ImageWriter()).write(f)

	# teste = barcode.get('ean13', numbers, writer=ImageWriter())
	# teste.save(f"images/{cloth_name}/{cloth_name}_{x}_codigo")

file.close()
