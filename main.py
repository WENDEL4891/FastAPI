from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!"}


@app.get("/fake-users")
async def fake_users():
    users = []
    for _ in range(100):
        user = {
            "nome": fake.name(),
            "data_nascimento": fake.date_of_birth(minimum_age=18, maximum_age=90).isoformat(),
            "naturalidade": fake.city(),
            "cpf": fake.cpf(),
            "foto": f"https://via.placeholder.com/150?text={random.randint(1, 1000)}"
        }
        users.append(user)

    return users
