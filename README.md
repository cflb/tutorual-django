Tutorial do Tutorial
--------------------

1. Criar Repositório no Github
2. Clonar repositório na sua máquina
3. Criar sua virtualenv
   * virtualenv -p python3 .env
4. Ativar sua Virtualenv
   * source .env/bin/activate
5. Instalar o Django
   * pip install django
6. Criar arquivo de dependências (requeriments.txt)
   * pip freeze > requeriments.txt
7. Criando projeto com django
   * django-admin startproject meuSite
8. Testando django
   * python3 manage.py runserver
   * ou
   * ./manage.py runserver
9. Criando banco de dados
   * ./manage.py migrate
10. Criando usuário admin
   * ./manage.py createsuperuser
11. Criando um aplicativo de Blog
   * ./manage.py startapp blog
12. Adcionando aplicativo ao settings do projeto
   * No arquivo settings.py adcionar o nome do app na lista de INSTALLED_APPS