# Projeto VAR

Este projeto é um sistema de gestão de punições e acompanhamento, desenvolvido em **Django**.

## Estrutura do Projeto

O projeto principal (`VAR`) contém as configurações gerais, e a lógica principal da aplicação está no app chamado `denuncias`.

### Principais Modelos da Aplicação `denuncias`:
* `Motivo`: Gerencia os motivos das punições.
* `Vares`: Representa os usuários que aplicam as punições/VARs.
* `Punições`: Armazena os registros de punições aplicadas.
* `Acoes`: Lista as ações (usado para o formulário de solicitação de tela).

## Pré-requisitos

Para rodar este projeto, você precisará ter instalado em sua máquina:

* **Python** (versão 3.x)
* **pip** (gerenciador de pacotes do Python)

## Configuração do Ambiente

Siga os passos abaixo para configurar e rodar o projeto localmente.

### 1. Clonar o Repositório

Primeiro, clone o repositório para sua máquina local e navegue até a pasta do projeto.

```bash
git clone <URL_DO_SEU_REPOSITORIO>
cd <nome_da_pasta_do_projeto> # Exemplo: cd var

2. Criar e Ativar o Ambiente Virtual
É uma boa prática utilizar um ambiente virtual (venv) para isolar as dependências do projeto.

No Linux/macOS:

python3 -m venv venv
source venv/bin/activate

No Windows:
python -m venv venv
.\venv\Scripts\activate

3. Instalar as Dependências
Você precisará instalar o Django no ambiente virtual ativo.

pip install django
# Se você criar um arquivo requirements.txt (o que é recomendado), use:
# pip install -r requirements.txt

4. Configurar o Banco de Dados
O projeto está configurado para usar o SQLite por padrão. Aplique as migrações existentes para criar as tabelas necessárias no banco de dados (db.sqlite3):

python manage.py migrate

5. Criar um Superusuário (Opcional)
Para acessar a interface administrativa do Django (/admin/) e gerenciar os modelos (Motivo, Vares, Punições, Acoes):

python manage.py createsuperuser
Siga as instruções no console para definir as credenciais de acesso.

6. Executar o Servidor de Desenvolvimento
Inicie o servidor local:

python manage.py runserver
O projeto estará acessível em: http://127.0.0.1:8000/
