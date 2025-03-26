# 💻📱 ERP\_BACKEND\_DJANGO

## 📌 Sobre o Projeto

O **ERP\_BACKEND\_DJANGO** é um Sistema de Gestão Empresarial (ERP) completo, desenvolvido com **Django Rest Framework** no back-end e **ReactJS** no front-end. Ele oferece funcionalidades para gerenciamento de empresas, funcionários, grupos de permissões e tarefas.

## 🚀 Tecnologias Utilizadas

### 🔹 Back-end:

- Django
- Django Rest Framework
- Simple JWT

### 🔹 Front-end:

🚧 **Em Construção** 🚧

## ⛏️ Instalação

### 1️⃣ Clonar o Repositório

```bash
git clone https://github.com/JGabriel02/ERP_BACKEND_DJANGO.git
cd ERP_BACKEND_DJANGO
```

### 2️⃣ Criar e Ativar o Ambiente Virtual

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 3️⃣ Instalar Dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Rodar Migrações do Banco de Dados

```bash
python manage.py migrate
```

### 5️⃣ Iniciar o Servidor

```bash
python manage.py runserver
```

O servidor estará disponível em [**http://127.0.0.1:8000/**](http://127.0.0.1:8000/).

## 📋 Documentação da API

### 🔑 Autenticação

**Criar Conta**

```
POST /api/v1/auth/signup
Parâmetros:
- name (string) - Obrigatório
- email (string) - Obrigatório
- password (string) - Obrigatório
```

**Fazer Login**

```
POST /api/v1/auth/signin
Parâmetros:
- email (string) - Obrigatório
- password (string) - Obrigatório
```

**Obter Usuário Logado**

```
GET /api/v1/auth/user
Cabeçalho:
- Authorization: Bearer <Access Token>
```

### 🏢 Empresas e Funcionários

**Listar Funcionários de uma Empresa**

```
GET /api/v1/companies/employees
```

**Criar um Funcionário**

```
POST /api/v1/companies/employees
Parâmetros:
- name (string) - Obrigatório
- email (string) - Obrigatório
- password (string) - Obrigatório
```

**Obter um Funcionário**

```
GET /api/v1/companies/employees/{id}
```

**Editar um Funcionário**

```
PUT /api/v1/companies/employees/{id}
Parâmetros:
- name (string) - Opcional
- email (string) - Opcional
- groups (string) - Opcional
```

**Deletar um Funcionário**

```
DELETE /api/v1/companies/employees/{id}
```

### 🔐 Grupos e Permissões

**Listar Grupos de uma Empresa**

```
GET /api/v1/companies/groups
```

**Criar um Grupo**

```
POST /api/v1/companies/groups
Parâmetros:
- name (string) - Obrigatório
- permissions (string) - Obrigatório
```

**Obter um Grupo**

```
GET /api/v1/companies/groups/{id}
```

**Editar um Grupo**

```
PUT /api/v1/companies/groups/{id}
Parâmetros:
- name (string) - Opcional
- permissions (string) - Opcional
```

**Deletar um Grupo**

```
DELETE /api/v1/companies/groups/{id}
```

### 📌 Tarefas

**Listar Tarefas de uma Empresa**

```
GET /api/v1/companies/tasks
```

**Criar uma Tarefa**

```
POST /api/v1/companies/tasks
Parâmetros:
- employee_id (number) - Obrigatório
- status_id (number) - Obrigatório
- title (string) - Obrigatório
- description (string) - Opcional
- due_date (date) - Opcional (Formato: d/m/Y H:M)
```

**Obter uma Tarefa**

```
GET /api/v1/companies/tasks/{id}
```

**Editar uma Tarefa**

```
PUT /api/v1/companies/tasks/{id}
Parâmetros:
- employee_id (number) - Opcional
- status_id (number) - Opcional
- title (string) - Opcional
- description (string) - Opcional
- due_date (date) - Opcional
```

**Deletar uma Tarefa**

```
DELETE /api/v1/companies/tasks/{id}
```


💡 *Desenvolvido por ********[JGabriel02](https://github.com/JGabriel02)********.*


