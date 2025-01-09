import os
import pyaes

# Nome do arquivo criptografado
file_name = "teste.txt.ransomwaretroll"  # Substitua com o nome correto do seu arquivo criptografado

# Abrir o arquivo criptografado
with open(file_name, "rb") as file:
    file_data = file.read()

# A mesma chave usada na criptografia (é IMPORTANTE que seja a mesma)
key = b"testeransomwares"

# Descriptografar o arquivo com a mesma chave
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

# Remover o arquivo criptografado
os.remove(file_name)

# Criar o arquivo descriptografado
new_file_name = "teste.txt"  # O nome do arquivo original
with open(new_file_name, "wb") as new_file:
    new_file.write(decrypt_data)

print(f"Arquivo descriptografado com sucesso: {new_file_name}")
