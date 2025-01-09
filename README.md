Final Project of Santander Bootcamp Cibersegurança #2

Como criar e usar um sistema de criptografia e descriptografia com o algoritmo AES no modo CTR usando Python.
⚠️ Importante: Este projeto foi criado somente para fins educacionais e não deve ser usado para atividades maliciosas.

🚀 Funcionalidades
🔒 Criptografar Arquivos
Converte um arquivo em uma versão criptografada com a extensão .ransomwaretroll.
Remove automaticamente o arquivo original após a criptografia.

🔓 Descriptografar Arquivos
Restaura o arquivo original a partir de um arquivo criptografado.
Exclui o arquivo criptografado após a recuperação.

🛠️ Pré-requisitos
🐍 Instalação do Python
Certifique-se de ter o Python 3.8 ou superior instalado em seu computador.
Você pode baixá-lo em: https://www.python.org/downloads/.

📦 Instale a biblioteca necessária
No terminal, execute o comando abaixo para instalar o módulo pyaes:
* A biblioteca **pyaes** é um módulo Python que implementa o algoritmo de criptografia AES (Advanced Encryption Standard).

bash
Copiar código
pip install pyaes
📂 Estrutura do Projeto
plaintext
Copiar código

cibersecurity-desafio-ransomware/
├── encrypter.py         # Script para criptografar arquivos
├── decrypter.py         # Script para descriptografar arquivos
├── teste.txt            # Arquivo de exemplo para criptografia
├── README.md            # Documentação do projeto

🔒 Como Criptografar Arquivos
Certifique-se de que o arquivo que deseja criptografar está na mesma pasta que o script encrypter.py.
Abra o terminal e execute o comando:
bash
Copiar código
python encrypter.py

Resultado:
O arquivo original será criptografado e salvo com a extensão .ransomwaretroll.

Arquivo original: teste.txt
Arquivo criptografado: teste.txt.ransomwaretroll
O arquivo original será automaticamente excluído.

🔓 Como Descriptografar Arquivos
Certifique-se de ter a mesma chave de criptografia usada no processo de criptografia.
Abra o terminal e execute o comando:
bash
Copiar código
python decrypter.py

Resultado:
O arquivo original será restaurado com o mesmo nome.

Arquivo criptografado: teste.txt.ransomwaretroll
Arquivo restaurado: teste.txt
O arquivo criptografado será automaticamente excluído.

⚠️ Este projeto foi desenvolvido exclusivamente para aprendizado e para ensinar conceitos de cibersegurança.
O uso inadequado desta aplicação pode violar leis e regulamentos. Nunca utilize para fins ilegais!
