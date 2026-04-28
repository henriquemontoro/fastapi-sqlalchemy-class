from repositories.author_repository import AuthorRepository
from entities.author import Author
from models.author_model import AuthorModel

class CreateAuthorUseCase:
    """Caso de uso para criação de um novo autor."""

    def __init__(self, author_repository: AuthorRepository):
        """
        Args:
            author_repository (AuthorRepository): Repositório de autores.
        """
        self.author_repository = author_repository

    def execute(self, name: str, email: str) -> Author:
        """Cria e persiste um novo autor no banco de dados.

        Args:
            name (str): Nome do autor.
            email (str): Email do autor.

        Returns:
            Author: O autor criado com os dados atualizados do banco.
        """
        author_model = AuthorModel(name=name, email=email)
        created_author = self.author_repository.add(author_model)
        return created_author
