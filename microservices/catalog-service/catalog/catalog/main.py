from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI(
    title="Catalog Service",
    description="A simple catalog service to manage products",
)

# Step 4: Define a Product model
class Product(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

# In-memory storage for products
products: List[Product] = []

# Step 5: GET endpoint to retrieve all products
@app.get("/products", response_model=List[Product])
def get_products():
    return products

# Step 6: GET endpoint to retrieve a product by its ID
@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
    return None

# Step 7: POST endpoint to add a new product
@app.post("/products", response_model=Product)
def create_product(product: Product):
    products.append(product)
    return product

# Step 8: PUT endpoint to update an existing product
@app.put("/products/{product_id}", response_model=Product)
def update_product(product_id: int, product: Product):
    for index, existing_product in enumerate(products):
        if existing_product.id == product_id:
            products[index] = product
            return product
    return None

# Step 9: DELETE endpoint to delete a product
@app.delete("/products/{product_id}", response_model=Product)
def delete_product(product_id: int):
    for index, existing_product in enumerate(products):
        if existing_product.id == product_id:
            del products[index]
            return existing_product
    return None
