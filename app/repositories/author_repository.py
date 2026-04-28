from sqlalchemy.orm import Session
from models.author_model import AuthorModel
from repositories.base_repository import BaseRepository

class AuthorRepository(BaseRepository[AuthorModel]):
    """Repositório de autores com operações específicas além do CRUD básico."""

    def __init__(self, session: Session):
        """
        Args:
            session (Session): Sessão do banco de dados.
        """
        super().__init__(session, AuthorModel)

    def get_by_email(self, email: str) -> AuthorModel | None:
        """Busca um autor pelo email.

        Args:
            email (str): O email do autor a ser buscado.

        Returns:
            AuthorModel | None: O autor encontrado ou None se nenhum autor for encontrado.
        """
        return self.session.query(AuthorModel).filter(AuthorModel.email == email).first()

    def get_by_name(self, name: str) -> list[AuthorModel]:
        """Busca autores cujo nome contenha o termo informado (busca parcial, case-insensitive).

        Args:
            name (str): Termo a ser buscado no nome dos autores.

        Returns:
            list[AuthorModel]: Lista de autores cujo nome contém o termo.
        """
        return self.session.query(AuthorModel).filter(AuthorModel.name.ilike(f"%{name}%")).all()

    def get_authors_with_books(self) -> list[AuthorModel]:
        """Retorna apenas os autores que possuem pelo menos um livro associado.

        Returns:
            list[AuthorModel]: Lista de autores com livros.
        """
        return self.session.query(AuthorModel).join(AuthorModel.books).distinct().all()
