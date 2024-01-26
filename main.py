from fastapi import FastAPI
from database.database import engine, Base
from routers import menu, submenu, dish

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(menu.router)
app.include_router(submenu.router)
app.include_router(dish.router)
