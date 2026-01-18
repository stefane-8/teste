# 🧪 Teste — Projeto Django

Repositório criado para **testar funcionalidades do GitHub** e trabalhar com **múltiplas branches** usando um projeto Django como base.

---

## ❓ Sobre o Projeto

Este projeto foi desenvolvido com o objetivo de:

- testar fluxos de trabalho no GitHub
- trabalhar com branches e commits
- experimentar funcionalidades de desenvolvimento
- servir como base de estudos com Django

---

## 🧰 Tecnologias

O projeto utiliza:

- Python 🐍
- Django 📦
- SQLite (banco local)
- HTML / CSS (templates)

### 📦 Pré-requisitos

Antes de rodar o projeto localmente, instale:

- Python 3.x

pip

(opcional) Git

🚀 Instalação passo a passo
1. Clone o repositório

git clone https://github.com/stefane-8/teste.git

### 2. Vá para a pasta do projeto

cd teste

### 3. Crie e ative um ambiente virtual

- Windows

python -m venv venv
venv\Scripts\activate


- Linux / macOS

python -m venv venv
source venv/bin/activate

### 4. Instale as dependências

pip install -r requiriments.txt

### ▶️ Como rodar o projeto

- Execute as migrações:

python manage.py migrate


### Inicie o servidor:

python manage.py runserver


### Acesse no navegador:

http://localhost:8000/

## 📁 Estrutura geral
```md
accounts/ → app de autenticação (login e cadastro)
companie/ → app relacionado à empresas
config/ → configurações do projeto Django
core/ → código principal
projects/ → app de projetos
public/ → arquivos públicos
static/ → arquivos estáticos (CSS, etc.)
surveys/ → app de pesquisas
templates/ → templates HTML
manage.py → arquivo principal do Django

### 🧠 Organização de Branches

Padrões comuns para organização de branches:

- main → versão estável principal

- dev → desenvolvimento

- feature/* → novas funcionalidades


### 📜 Licença

Este projeto está sob a licença MIT.


---

## 💡 Dicas opcionais que você pode adicionar

### 🎨 Badges (opcionais)

```md
![GitHub repo size](https://img.shields.io/github/repo-size/stefane-8/teste)
![GitHub stars](https://img.shields.io/github/stars/stefane-8/teste)
![GitHub license](https://img.shields.io/github/license/stefane-8/teste)

