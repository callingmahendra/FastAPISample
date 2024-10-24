from fastapi import FastAPI
from app.routes.users import router as users_router
from app.routes.customers import router as customers_router

app = FastAPI()

app.include_router(users_router, prefix="/users", tags=["users"])
app.include_router(customers_router, prefix="/customers", tags=["customers"])
