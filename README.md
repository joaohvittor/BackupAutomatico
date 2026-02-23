📁 Sistema de Backup Automático com Geração de Logs
📌 Descrição

Este projeto é um script em Python que:

Verifica e cria diretórios automaticamente

Gera logs com timestamp único

Coleta informações do sistema

Salva o log em uma pasta específica

Cria backup automático do arquivo gerado

O objetivo é praticar manipulação de arquivos, diretórios e organização modular em Python.

🚀 Funcionalidades

✅ Criação automática das pastas logs e backup

✅ Geração de nome de arquivo com data e hora

✅ Coleta de informações do sistema:

Usuário

Diretório de execução

Data e hora

Lista de arquivos do diretório

✅ Escrita do log em arquivo .txt

✅ Cópia automática para pasta de backup

✅ Uso de caminhos absolutos (independente de onde o script é executado)

🛠 Tecnologias Utilizadas

Python 3

Módulos padrão:

os

datetime

shutil

📂 Estrutura do Projeto
BackupAutomatico/
│
├── main.py
├── logs/
├── backup/
└── README.md
▶️ Como Executar

Clone o repositório:

git clone https://github.com/seu-usuario/nome-do-repo.git

Acesse a pasta do projeto:

cd BackupAutomatico

Execute:

python main.py
📖 Conceitos Aplicados

Funções e modularização

Manipulação de arquivos

Manipulação de diretórios

Caminhos relativos vs absolutos

Organização de projeto

Automação básica