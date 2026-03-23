"""
Starter code for Building REST APIs with FastAPI

This module provides the basic structure for building a REST API using FastAPI.
Complete the implementation following the requirements in README.md
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List


# Initialize FastAPI application
app = FastAPI(
    title="Assignment API",
    description="REST API for learning FastAPI",
    version="1.0.0"
)


# TODO: Define Pydantic models for your data structures
class Item(BaseModel):
    """Model for Item request/response"""
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    price: float


# TODO: Create an in-memory database (dictionary) to store items
# In production, this would be replaced with a real database
items_db = {}


# TODO: Implement the following endpoints:

@app.get("/")
def read_root():
    """Welcome endpoint"""
    return {"message": "Welcome to the FastAPI Assignment"}


@app.get("/items")
def get_items():
    """GET endpoint to retrieve all items"""
    # TODO: Implement this endpoint
    # - Return a list of all items
    # - Consider adding pagination and filtering
    pass


@app.get("/items/{item_id}")
def get_item(item_id: int):
    """GET endpoint to retrieve a specific item by ID"""
    # TODO: Implement this endpoint
    # - Return the item with the specified ID
    # - Raise HTTPException with 404 status if item not found
    pass


@app.post("/items")
def create_item(item: Item):
    """POST endpoint to create a new item"""
    # TODO: Implement this endpoint
    # - Add the item to the database
    # - Return the created item with an ID
    # - Return 201 status code
    pass


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    """PUT endpoint to update an existing item"""
    # TODO: Implement this endpoint
    # - Update the item with the specified ID
    # - Raise HTTPException with 404 status if item not found
    # - Return the updated item
    pass


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    """DELETE endpoint to remove an item"""
    # TODO: Implement this endpoint
    # - Delete the item with the specified ID
    # - Raise HTTPException with 404 status if item not found
    # - Return a success message
    pass


# To run this application, use the command:
# uvicorn starter-code:app --reload
