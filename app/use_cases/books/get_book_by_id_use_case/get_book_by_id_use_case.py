from repositories.book_repository import BookRepository
from dtos.book_dto import BookResponse
from typing import Optional

class GetBookByIdUseCase:
    """Caso de uso para busca de um livro pelo ID."""

    def __init__(self, book_repository: BookRepository):
        """
        Args:
            book_repository (BookRepository): Repositório de livros.
        """
        self.book_repository = book_repository

    def execute(self, book_id: int) -> Optional[BookResponse]:
        """Busca um livro pelo ID.

        Args:
            book_id (int): ID do livro a ser buscado.

        Returns:
            Optional[BookResponse]: O livro encontrado ou None se não existir.
        """
        book = self.book_repository.get_by_id(book_id)
        return BookResponse.model_validate(book) if book else None
