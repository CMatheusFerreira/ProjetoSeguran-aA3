from flask import Flask, request, render_template, redirect, session          #Flask para aplicações Web
from werkzeug.security import generate_password_hash, check_password_hash     #permite criptografar as senhas

app = Flask(__name__)
app.secret_key = "chave_super_secreta_123"  # Protege os dados das sessões e os cookies, para evitar falsificação (OWASP A07)

# Banco de dados simples em memória
areas = []

# Usuário padrão do sistema
user_db = {
    "admin": generate_password_hash("1234")
}

# ---------------- LOGIN ----------------
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form["usuario"]
        senha = request.form["senha"]

        # Segurança OWASP: verificar hash da senha (A02 - cryptografia para evitar exposição de dados sensíveis)
        if usuario in user_db and check_password_hash(user_db[usuario], senha):
            session["logado"] = True
            return redirect("/dashboard")
        else:
            return "Login inválido!"

    return render_template("login.html")

# -------------- DASHBOARD ----------------
@app.route("/dashboard")
def dashboard():
    if not session.get("logado"):  # Segurança: proteção de rota e controle de acesso (A01)
        return redirect("/")
    return render_template("dashboard.html", lista=areas)

# -------------- CADASTRAR ÁREA ----------------
@app.route("/adicionar", methods=["POST"])
def adicionar():
    if not session.get("logado"):
        return redirect("/")

    nome = request.form["nome"]
    descricao = request.form["descricao"]
    prioridade = request.form["prioridade"]

    # Segurança OWASP: validação de entradas (Para evitar erro de configuração de segurança - A05)
    if len(nome) == 0 or len(descricao) == 0:
        return "Campos inválidos!"

    nova_area = {
        "nome": nome,
        "descricao": descricao.replace("<", "&lt;"),  # sanitização contra XSS (Evitar injeção de código malicioso - A03)
        "prioridade": prioridade
    }

    areas.append(nova_area)
    return redirect("/dashboard")

# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
@app.route("/excluir/<int:indice>")
def excluir(indice):
    if not session.get("logado"):
        return redirect("/")

    if 0 <= indice < len(areas):
        areas.pop(indice)

    return redirect("/dashboard")

app.run(debug=True)




