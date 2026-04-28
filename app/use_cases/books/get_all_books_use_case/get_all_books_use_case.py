from repositories.book_repository import BookRepository
from dtos.book_dto import BookResponse

class GetAllBooksUseCase:
    """Caso de uso para listagem de todos os livros."""

    def __init__(self, book_repository: BookRepository):
        """
        Args:
            book_repository (BookRepository): Repositório de livros.
        """
        self.book_repository = book_repository

    def execute(self) -> list[BookResponse]:
        """Busca todos os livros cadastrados.

        Returns:
            list[BookResponse]: Lista com todos os livros.
        """
        books = self.book_repository.get_all()
        return [BookResponse.model_validate(book) for book in books]
