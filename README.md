---
# **Final Project of Santander Bootcamp Cibersegurança #2**

Este projeto ensina como criar e usar um sistema de criptografia e descriptografia simples com o algoritmo **AES no modo CTR** utilizando Python.

> O **AES (Advanced Encryption Standard)** no modo **CTR (Counter)** é um método de criptografia simétrica que cifra dados em blocos, utilizando um contador único para cada bloco. É eficiente, seguro e permite operações paralelas.
---
## 🚀 **Funcionalidades**

### 🔒 **Criptografar Arquivos**
- Converte um arquivo em uma versão criptografada com a extensão `.ransomwaretroll`.
- Remove automaticamente o arquivo original após a criptografia.

### 🔓 **Descriptografar Arquivos**
- Restaura o arquivo original a partir de um arquivo criptografado.
- Exclui automaticamente o arquivo criptografado após a recuperação.
---
## 🛠️ **Pré-requisitos**

### 🐍 **Instale o Python**
- Certifique-se de ter o **Python 3.8 ou superior** instalado.  
  > Faça o download em: [https://www.python.org/downloads/](https://www.python.org/downloads/)
  
### 📦 **Instale a biblioteca necessária**
1. No terminal, execute:
   ```bash
   pip install pyaes
   ```
2. A biblioteca **pyaes** implementa o algoritmo AES no Python.
---
## 📂 **Estrutura do Projeto**

```plaintext
cibersecurity-desafio-ransomware/
├── encrypter.py         # Script para criptografar arquivos
├── decrypter.py         # Script para descriptografar arquivos
├── teste.txt            # Arquivo de exemplo para criptografia
├── README.md            # Documentação do projeto
```
---

## 🔒 **Como Criptografar Arquivos**

1. Certifique-se de que o arquivo a ser criptografado está na mesma pasta do script `encrypter.py`.
2. No terminal, execute:
   ```bash
   python encrypter.py
   ```
3. **Resultado:**
   - O arquivo será criptografado com a extensão `.ransomwaretroll`.
   - O arquivo original será excluído automaticamente.
   - Arquivo original: `teste.txt`
   - Arquivo criptografado: `teste.txt.ransomwaretroll`

---

## 🔓 **Como Descriptografar Arquivos**

1. Certifique-se de usar a mesma **chave de criptografia** que foi utilizada para criptografar o arquivo.
2. No terminal, execute:
   ```bash
   python decrypter.py
   ```
3. **Resultado:**
   - O arquivo original será restaurado com o mesmo nome.
   - O arquivo criptografado será excluído automaticamente.
   - Arquivo criptografado: `teste.txt.ransomwaretroll`
   - Arquivo restaurado: `teste.txt`
---
 ⚠️ **Este projeto foi desenvolvido **exclusivamente para aprendizado** e demonstração de conceitos de cibersegurança.**
--- 
