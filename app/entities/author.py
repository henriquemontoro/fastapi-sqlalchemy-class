from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional

class Author(BaseModel):
    """
    Entidade Author usando Pydantic
    Representa um autor no domínio da aplicação
    """
    id: Optional[int] = Field(None, description="ID do autor", example=1)
    name: str = Field(..., min_length=1, max_length=255, description="Nome completo do autor", example="João Silva")
    email: EmailStr = Field(..., description="Email válido do autor", example="joao.silva@example.com")
    books: List['Book'] = Field(default_factory=list, description="Lista de livros escritos pelo autor")

    class Config:
        from_attributes = True

    def __str__(self):
        return f"Author: {self.name} ({self.email})"

# Resolve forward references
from .book import Book
Author.model_rebuild()
