from fastapi import FastAPI, HTTPException
from models import Produtos
from crud import criar_produto, listar_produtos, atualizar_produto, remover_produto

app = FastAPI()

@app.post("/produtos/")
def create_product(produto: Produtos):
    produto_id = criar_produto(produto)
    return {"id": produto_id}

@app.get("/produtos/")
def list_products():
    return {"produtos": listar_produtos()}

@app.put("/produtos/{id}")
def update_product(id: str, produto: Produtos):
    update = atualizar_produto(id, produto)
    if update == 0:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return {"msg": "Atualizado com sucesso"}

@app.delete("/produtos/{id}")
def delete_product(id: str):
    deleted = remover_produto(id)
    if deleted == 0:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return {"msg": "Produto removido com sucesso"}