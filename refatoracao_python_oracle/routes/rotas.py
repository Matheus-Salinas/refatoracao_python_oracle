from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from controllers.user_controller import (
    mostrar_usuarios,
    mostrar_edicao,
    cadastrar_usuario,
    excluir_usuario,
    atualizar_usuario
)

router = APIRouter()

# Rotas de usuários
@router.get("/", response_class=HTMLResponse)
async def listar_usuarios(request: Request):
    return await mostrar_usuarios(request)

@router.post("/usuarios", response_class=HTMLResponse)
async def criar_usuario(request: Request):
    form_data = await request.form()
    return await cadastrar_usuario(
        request,
        nome=form_data["nome"],
        email=form_data["email"]
    )

@router.get("/usuarios/editar/{user_id}", response_class=HTMLResponse)
async def editar_usuario(request: Request, user_id: int):
    return await mostrar_edicao(request, user_id)

@router.post("/usuarios/atualizar/{user_id}", response_class=HTMLResponse)
async def update_usuario(request: Request, user_id: int):
    form_data = await request.form()
    return await atualizar_usuario(
        request,
        user_id,
        nome=form_data["nome"],
        email=form_data["email"]
    )

@router.get("/usuarios/excluir/{user_id}", response_class=HTMLResponse)
async def deletar_usuario(user_id: int):
    return await excluir_usuario(user_id)