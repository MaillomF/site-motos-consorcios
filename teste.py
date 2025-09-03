import sqlite3

conn = sqlite3.connect('motos.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM motos")
motos = cursor.fetchall()

for moto in motos:
    print(f"ID: {moto[0]}, Modelo: {moto[1]}, Marca: {moto[2]}, Ano: {moto[3]}, Valor: R${moto[4]:.2f}")
    print(f"Descrição: {moto[5]}")
    print(f"Imagem: {moto[6]}")
    print("-" * 40)

conn.close()