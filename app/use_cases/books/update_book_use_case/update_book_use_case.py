from repositories.book_repository import BookRepository
from dtos.book_dto import BookResponse
from typing import Optional

class UpdateBookUseCase:
    """Caso de uso para atualização dos dados de um livro existente."""

    def __init__(self, book_repository: BookRepository):
        """
        Args:
            book_repository (BookRepository): Repositório de livros.
        """
        self.book_repository = book_repository

    def execute(self, book_id: int, title: str, isbn: str) -> Optional[BookResponse]:
        """Atualiza título e ISBN de um livro pelo ID.

        Args:
            book_id (int): ID do livro a ser atualizado.
            title (str): Novo título do livro.
            isbn (str): Novo ISBN do livro.

        Returns:
            Optional[BookResponse]: O livro atualizado ou None se não encontrado.
        """
        book = self.book_repository.get_by_id(book_id)
        if not book:
            return None

        book.title = title
        book.isbn = isbn
        updated_book = self.book_repository.update(book)
        return BookResponse.model_validate(updated_book) if updated_book else None
