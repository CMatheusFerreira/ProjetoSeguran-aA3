# 🏚️ Sistema de Registro de Áreas Danificadas — A3 Segurança em Sistemas Computacionais

Este projeto foi desenvolvido para a atividade A3 da matéria **Segurança em Sistemas Computacionais**.  
O objetivo é fornecer um sistema simples, funcional e que demonstre **boas práticas de segurança**, seguindo 5 tópicos do **OWASP Top 10**.

---

## 🎯 Objetivo do Sistema
Auxiliar a cidade de Rio Bonito do Iguaçu na reconstrução após o tornado, permitindo:

- Registrar áreas danificadas
- Descrever os danos
- Classificar a prioridade (Baixa, Média ou Alta)
- Listar todos os registros
- Controlar o acesso via login

O sistema foi desenvolvido com **Python + Flask**, utilizando estrutura simples para facilitar explicação e apresentação.

---

## ✔️ Funcionalidades

- Tela de login com usuário e senha
- Dashboard protegido por sessão
- Cadastro de áreas danificadas
- Lista dinâmica dos registros
- Logout seguro

---

## 🛡️ Segurança Aplicada (OWASP Top 10)

Este projeto implementa **5 tópicos** exigidos pela atividade:

**1. A01 — Controle de Acesso Quebrado**
- Dashboard protegido
- Usuário precisa estar logado para acessar rotas
- Rota `/dashboard` não abre sem sessão válida

**2. A02 — Falhas Criptográficas**
- Senha armazenada com **hash seguro** usando `generate_password_hash`
- Verificação com `check_password_hash`

##3. A03 — Injeção (XSS)**
- Sanitização da descrição usando `replace("<", "&lt;")`

**4. A05 — Validação de Entrada**
- Impede cadastro com campos vazios
- Evita dados inválidos

**5. A07 — Gerenciamento de Sessão**
- `secret_key` configurada
- Sessões protegidas
- Logout remove dados da sessão

---

## 📁 Estrutura do Projeto

ATIVIDADESEGURANÇA
│ app.py
│
└───templates
login.html
dashboard.html


---

## ▶️ Como Rodar o Projeto

**Pré-requisitos**
- Python instalado
- Flask e Werkzeug

**Instalar dependências**
pip install flask werkzeug

### **Executar**
python app.py


Abra no navegador:

http://127.0.0.1:5000

**Login padrão**

Usuário: admin
Senha: 1234


---

## 👨‍💻 Tecnologias Utilizadas
- Python
- Flask
- HTML (Jinja2)
- Werkzerg Hashing

---

## 📌 Integrantes da Equipe
- Matheus Cândido Ferreira
---

## 🔗 Repositório no GitHub
https://github.com/seu-usuario/projeto-a3


---

## 📜 Licença
Projeto simples desenvolvido para fins educacionais.







