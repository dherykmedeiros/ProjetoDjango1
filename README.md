
# projetoDjango

Este é um projeto básico de cadastro de usuários desenvolvido com o framework Django. O sistema permite o cadastro de usuários com nome, idade e um ID gerado automaticamente como chave primária.

## Funcionalidades

- Cadastro de receitas.
- Registro de usuarios.
- Login
- Logout
- Visualização de receitas


## Tecnologias Utilizadas

- Python
- Django
- SQLite (banco de dados padrão do Django)

## Requisitos

- Python 3.8 ou superior
- Django 3.0 ou superior

## Instalação

1. Clone este repositório:
   
   git clone https://github.com/dherykmedeiros/projetoDjango1.git<br>
   cd projetoDjango1
   

2. Crie e ative um ambiente virtual:
   
   python -m venv venv<br>
   source venv/bin/activate   # Para Linux/Mac<br>
   venv\Scripts\activate      # Para Windows
   

3. Instale as dependências:
   
   pip install -r requirements.txt
   

4. Execute as migrações do banco de dados:
   
   python manage.py migrate
   

5. Inicie o servidor de desenvolvimento:
   
   python manage.py runserver
   

6. Acesse o aplicativo em seu navegador:
   
   http://127.0.0.1:8000/
   

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

