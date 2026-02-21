from fastapi import FastAPI, HTTPException
from app.models import UserCreate, ProductCreate
from app.database import users_collection, products_collection
from bson import ObjectId
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="E-Commerce API 🚀")

@app.post("/users/", response_model=UserCreate)
async def create_user(user: UserCreate):
    user_dict = user.dict()
    result = await users_collection.insert_one(user_dict)
    user_dict["_id"] = str(result.inserted_id)
    return user_dict

@app.get("/users/{user_email}", response_model=UserCreate)
async def get_user_by_email(user_email: str):
    user = await users_collection.find_one({"email": user_email})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user["_id"] = str(user["_id"])
    return user

@app.post("/products/", response_model=ProductCreate)
async def create_product(product: ProductCreate):
    product_dict = product.dict()
    result = await products_collection.insert_one(product_dict)
    product_dict["_id"] = str(result.inserted_id)
    return product_dict

@app.get("/products/{product_sku}", response_model=ProductCreate)
async def get_product_by_sku(product_sku: str):
    product = await products_collection.find_one({"sku": product_sku})
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    product["_id"] = str(product["_id"])
    return product