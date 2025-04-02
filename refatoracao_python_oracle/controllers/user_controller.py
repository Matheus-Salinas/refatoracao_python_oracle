from fastapi import Request, Form, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from models.user_model_oracle import UserModelOracle
import cx_Oracle
from datetime import datetime

templates = Jinja2Templates(directory="templates")
templates.env.globals['now'] = datetime.now()

try:
    UserModelOracle.criar_tabela()
except cx_Oracle.DatabaseError as e:
    print(f"Aviso: {e.args[0].message}")

def base_context(request: Request):
    """Contexto base para todas as páginas"""
    return {
        "request": request,
        "usuarios": [],
        "mensagem": None,
        "erro": None
    }

def mostrar_usuarios(request: Request, mensagem: str = None, erro: str = None):
    context = base_context(request)
    try:
        context["usuarios"] = UserModelOracle.listar_todos()
        if mensagem:
            context["mensagem"] = mensagem
        if erro:
            context["erro"] = erro
    except cx_Oracle.DatabaseError as e:
        context["erro"] = f"Erro ao carregar usuários: {e.args[0].message}"
    
    return templates.TemplateResponse("index.html", context)

def mostrar_edicao(request: Request, user_id: int):
    context = base_context(request)
    try:
        usuario = UserModelOracle.buscar_por_id(user_id)
        if not usuario:
            return RedirectResponse("/?erro=Usuário+não+encontrado", status_code=303)
            
        context.update({
            "usuario": usuario,
            "usuarios": UserModelOracle.listar_todos()
        })
    except cx_Oracle.DatabaseError as e:
        return RedirectResponse(f"/?erro=Erro+ao+editar:+{e.args[0].message}", status_code=303)
    
    return templates.TemplateResponse("index.html", context)

async def cadastrar_usuario(request: Request, nome: str = Form(...), email: str = Form(...)):
    try:
        UserModelOracle.inserir(nome, email)
        return RedirectResponse("/?mensagem=Usuário+cadastrado+com+sucesso", status_code=303)
    except cx_Oracle.DatabaseError as e:
        error = e.args[0]
        if error.code == 1:  
            return RedirectResponse("/?erro=Email+já+registrado", status_code=303)
        return RedirectResponse(f"/?erro=Erro+ao+cadastrar:+{error.message}", status_code=303)

def excluir_usuario(user_id: int):
    try:
        UserModelOracle.excluir(user_id)
        return RedirectResponse("/?mensagem=Usuário+removido+com+sucesso", status_code=303)
    except cx_Oracle.DatabaseError as e:
        return RedirectResponse(f"/?erro=Erro+ao+excluir:+{e.args[0].message}", status_code=303)

async def atualizar_usuario(request: Request, user_id: int, nome: str = Form(...), email: str = Form(...)):
    try:
        UserModelOracle.atualizar(user_id, nome, email)
        return RedirectResponse("/?mensagem=Dados+atualizados+com+sucesso", status_code=303)
    except cx_Oracle.DatabaseError as e:
        error = e.args[0]
        if error.code == 1: 
            return RedirectResponse(f"/usuarios/edit/{user_id}?erro=Email+já+registrado", status_code=303)
        return RedirectResponse(f"/usuarios/edit/{user_id}?erro=Erro+ao+atualizar:+{error.message}", status_code=303)