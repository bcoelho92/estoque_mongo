from banco import collection
from models import Produtos
from bson.objectid import ObjectId

def criar_produto(produto: Produtos):
    result = collection.insert_one(produto.model_dump())
    return str(result.inserted_id)

def listar_produtos():
    produtos = list(collection.find())
    for p in produtos:
        p["_id"] = str(p["_id"])
    return produtos

def atualizar_produto(id: str, produto: Produtos):
    result = collection.update_one(
        {"_id": ObjectId(id)},
        {"$set": produto.model_dump()}
    )
    return result.modified_count

def remover_produto(id: str):
    result = collection.delete_one({"_id": ObjectId(id)})
    return result.deleted_count

