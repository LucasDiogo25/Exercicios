from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Classe modelo para representar um usuário
class User(BaseModel):
    id: int
    name: str
    email: str
    
@app.get("/")
def root():
    return {"message": "API em execução"}
# Lista para armazenar os usuários
users = []

# Rota para criar um novo usuário
@app.post("/users/")
def create_user(user: User):
    users.append(user)
    return {"message": "Usuário criado com sucesso"}

# Rota para obter todos os usuários
@app.get("/users/")
def get_users():
    return users

# Rota para obter um usuário específico
@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    return {"error": "Usuário não encontrado"}

# Rota para atualizar um usuário
@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    for index, existing_user in enumerate(users):
        if existing_user.id == user_id:
            users[index] = user
            return {"message": "Usuário atualizado com sucesso"}
    return {"error": "Usuário não encontrado"}

# Rota para excluir um usuário
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for index, user in enumerate(users):
        if user.id == user_id:
            users.pop(index)
            return {"message": "Usuário excluído com sucesso"}
    return {"error": "Usuário não encontrado"}

##Para criar um novo usuário, faça uma solicitação POST para http://localhost:8000/users/ com os dados do usuário no corpo da solicitação.
##Para obter todos os usuários, faça uma solicitação GET para http://localhost:8000/users/.
##Para obter um usuário específico, faça uma solicitação GET para http://localhost:8000/users/{user_id}, onde {user_id} é o ID do usuário.
##Para atualizar um usuário, faça uma solicitação PUT para http://localhost:8000/users/{user_id}, onde {user_id} é o ID do usuário, e inclua os dados atualizados do usuário no corpo da solicitação.
##Para excluir um usuário, faça uma solicitação DELETE para http://localhost:8000/users/{user_id}, onde {user_id} é o ID do usuário.