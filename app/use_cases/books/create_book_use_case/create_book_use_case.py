from repositories.book_repository import BookRepository
from dtos.book_dto import BookResponse
from models.book_model import BookModel
from typing import Optional

class CreateBookUseCase:
    """Caso de uso para criação de um novo livro."""

    def __init__(self, book_repository: BookRepository):
        """
        Args:
            book_repository (BookRepository): Repositório de livros.
        """
        self.book_repository = book_repository

    def execute(self, title: str, isbn: str) -> BookResponse:
        """Cria e persiste um novo livro no banco de dados.

        Args:
            title (str): Título do livro.
            isbn (str): ISBN do livro.

        Returns:
            BookResponse: O livro criado com os dados atualizados do banco.
        """
        book_model = BookModel(title=title, isbn=isbn)
        created_book = self.book_repository.add(book_model)
        return BookResponse.model_validate(created_book)
