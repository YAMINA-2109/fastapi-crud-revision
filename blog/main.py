from fastapi import FastAPI
from routers import blog, user, authentication


app = FastAPI()

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.user_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Blog Application"}