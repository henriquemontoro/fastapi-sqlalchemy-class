from sqlalchemy.orm import Session
from models.book_model import BookModel
from repositories.base_repository import BaseRepository

class BookRepository(BaseRepository[BookModel]):
    """Repositório de livros com operações específicas além do CRUD básico."""

    def __init__(self, session: Session):
        """
        Args:
            session (Session): Sessão do banco de dados.
        """
        super().__init__(session, BookModel)

    def get_by_isbn(self, isbn: str) -> BookModel | None:
        """Busca um livro pelo ISBN.

        Args:
            isbn (str): O ISBN do livro a ser buscado.

        Returns:
            BookModel | None: O livro encontrado ou None se não existir.
        """
        return self.session.query(BookModel).filter(BookModel.isbn == isbn).first()

    def get_by_title(self, title: str) -> list[BookModel]:
        """Busca livros cujo título contenha o termo informado (busca parcial, case-insensitive).

        Args:
            title (str): Termo a ser buscado no título dos livros.

        Returns:
            list[BookModel]: Lista de livros cujo título contém o termo.
        """
        return self.session.query(BookModel).filter(BookModel.title.ilike(f"%{title}%")).all()

    def get_books_with_authors(self) -> list[BookModel]:
        """Retorna apenas os livros que possuem pelo menos um autor associado.

        Returns:
            list[BookModel]: Lista de livros com autores.
        """
        return self.session.query(BookModel).join(BookModel.authors).distinct().all()
