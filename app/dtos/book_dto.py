from pydantic import BaseModel, Field
from typing import List

class CreateBookRequest(BaseModel):
    """
    DTO para requisição de criação de livro
    Contém os dados necessários para criar um novo livro
    """
    title: str = Field(..., min_length=1, max_length=255, description="Título do livro", example="Clean Code")
    isbn: str = Field(..., min_length=10, max_length=17, description="ISBN do livro no formato ISBN-10 ou ISBN-13", example="978-0132350884")

class UpdateBookRequest(BaseModel):
    """
    DTO para requisição de atualização de livro
    Contém os dados que podem ser atualizados de um livro
    """
    title: str = Field(..., min_length=1, max_length=255, description="Título do livro", example="Clean Code")
    isbn: str = Field(..., min_length=10, max_length=17, description="ISBN do livro no formato ISBN-10 ou ISBN-13", example="978-0132350884")

class AuthorSummary(BaseModel):
    """
    DTO com resumo das informações de um autor
    Usado para evitar referências circulares na resposta de livros
    """
    id: int = Field(..., description="ID único do autor", example=1)
    name: str = Field(..., description="Nome completo do autor", example="João Silva")
    email: str = Field(..., description="Email do autor", example="joao.silva@example.com")

    class Config:
        from_attributes = True

class BookResponse(BaseModel):
    """
    DTO de resposta para operações com livros
    Contém todas as informações do livro incluindo seus autores
    """
    id: int = Field(..., description="ID único do livro", example=1)
    title: str = Field(..., description="Título do livro", example="Clean Code")
    isbn: str = Field(..., description="ISBN do livro", example="978-0132350884")
    authors: List[AuthorSummary] = Field(default_factory=list, description="Lista de autores do livro")

    class Config:
        from_attributes = True
