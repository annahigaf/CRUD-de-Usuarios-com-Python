TURMA: SI (noturno)

GRUPO:

Anna Julia Higa Farincho 

Evelyn Merces

Geovane Soares

Leticia Macedo

Richard


🧑‍💻 CRUD de Usuários com Python

API desenvolvida em Python para gerenciamento de usuários, implementando as operações básicas de um sistema CRUD (Create, Read, Update e Delete) com armazenamento de dados em memória utilizando uma lista (array). O projeto foi estruturado com boas práticas, aplicando arquitetura MVC + Service para separar responsabilidades e modularizar o código.


🚀 Funcionalidades

✔ Criar um novo usuário

✔ Listar todos os usuários

✔ Consultar usuário específico

✔ Atualizar dados de um usuário

✔ Remover usuário do sistema


Essas operações são realizadas em memória, sem necessidade de banco de dados externo, facilitando testes e demonstração de lógica backend.


📁 Estrutura do Projeto

O projeto está organizado seguindo boas práticas de arquitetura e separação de camadas:

📦controllers     # Responsáveis por receber as requisições

📦models          # Definições de entidades como User

📦repositories    # Abstrai a camada de persistência em memória

📦services        # Lógica de negócios

app.py            # Arquivo principal para iniciar o servidor/API


🧠 Arquitetura

✨ MVC + Service Pattern

Models: Definem as entidades do sistema.

Controllers: Recebem e retornam os dados via API.

Services: Contém a lógica principal do CRUD.

Repositories: Gerenciam a persistência em memória.

Esse padrão facilita manutenção e escalabilidade do código.


🛠️ Tecnologias Utilizadas
Tecnologia	Uso no Projeto
Python	Linguagem principal
Lista (array)	Armazenamento temporário dos dados
MVC	Estrutura arquitetural
REST API	Padrão de comunicação


🧪 Como Rodar o Projeto

Clone o repositório:

git clone https://github.com/annahigaf/CRUD-de-Usuarios-com-Python.git


Navegue até a pasta do projeto:

cd CRUD-de-Usuarios-com-Python


Execute a API com Python:

python app.py


A API ficará disponível localmente e você pode testar os endpoints (ex: com o Postman, Insomnia ou curl).

📌 Endpoints


Método	Caminho	Descrição
GET	/users	Lista todos os usuários
GET	/users/{id}	Retorna um usuário específico
POST	/users	Cria um novo usuário
PUT	/users/{id}	Atualiza um usuário
DELETE	/users/{id}	Remove um usuário


