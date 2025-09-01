Iniciar aplicativos django, temos que criar o 'django-admin startproject back_var .'
faz com que o aplicativo principal seja criado
" Projetos/
└── back_var/
    ├── back_var/  (pasta de configurações)
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── manage.py  <-- **Agora o arquivo `manage.py` está aqui.**"

    criar isso aqui acima

Logo apos temos que criar o aplicativo

python manage.py startapp denuncias

sempre que criar aplicativos como o de cima, temos que colocalos nos APPS Installed em 'settings.py' no caso criamos o denuncias, os add la.

---Preparar o Banco de Dados
Agora que o Django sabe que seu aplicativo existe, você precisa rodar as migrações iniciais para criar as tabelas padrão do framework no banco de dados.

python manage.py makemigrations
python manage.py migrate


apos temos que mexer no nosso models, ele que vai criar as colunas no banco de dados
no caso seria uma classe com os parametros que seram aceitos

Toda alteraçao no models tem q da um 
python manage.py makemigrations denuncias
python manage.py migrate
python manage.py runserver