from repositories.book_repository import BookRepository
from dtos.book_dto import BookResponse

class DeleteBookUseCase:
    """Caso de uso para remoção de um livro do banco de dados."""

    def __init__(self, book_repository: BookRepository):
        """
        Args:
            book_repository (BookRepository): Repositório de livros.
        """
        self.book_repository = book_repository

    def execute(self, book_id: int) -> BookResponse | None:
        """Remove um livro pelo ID.

        Args:
            book_id (int): ID do livro a ser removido.

        Returns:
            BookResponse | None: Os dados do livro removido ou None se não encontrado.
        """
        book = self.book_repository.get_by_id(book_id)
        if not book:
            return None
        response = self.book_repository.delete(book_id)
        return BookResponse.model_validate(response)
