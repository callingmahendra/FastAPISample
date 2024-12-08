from fastapi import FastAPI
from app.routes.users import router as users_router
from app.routes.customers import router as customers_router
from app.routes.employees import router as employees_router

app = FastAPI()

app.include_router(users_router, prefix="/users", tags=["users"])
app.include_router(customers_router, prefix="/customers", tags=["customers"])
app.include_router(employees_router, prefix="/employees", tags=["employees"])
