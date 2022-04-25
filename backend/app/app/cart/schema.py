from pydantic import BaseModel
import datetime
from typing import List
from app.products.schemas import Product

class CartItemsBase(BaseModel):
    products: Product
    created_date: datetime.datetime

class CartItemsInDBBase(CartItemsBase):
    id: int
    class Config:
        orm_mode = True

class CartItems(CartItemsInDBBase):
    pass



class CarInDBBase(BaseModel):
    id: int
    cart_items: List[CartItems] = []
    class Config:
        orm_mode = True

class Car(CartItemsInDBBase):
    pass

