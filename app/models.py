from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None
    address: Optional[str] = None


class ProductCreate(BaseModel):
    sku: str
    name: str
    price: float
    stock: int
    description: Optional[str] = None