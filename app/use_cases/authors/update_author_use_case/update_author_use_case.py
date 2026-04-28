from repositories.author_repository import AuthorRepository
from dtos.author_dto import AuthorResponse
from typing import Optional

class UpdateAuthorUseCase:
    """Caso de uso para atualização dos dados de um autor existente."""

    def __init__(self, author_repository: AuthorRepository):
        """
        Args:
            author_repository (AuthorRepository): Repositório de autores.
        """
        self.author_repository = author_repository

    def execute(self, author_id: int, name: str, email: str) -> Optional[AuthorResponse]:
        """Atualiza nome e email de um autor pelo ID.

        Args:
            author_id (int): ID do autor a ser atualizado.
            name (str): Novo nome do autor.
            email (str): Novo email do autor.

        Returns:
            Optional[AuthorResponse]: O autor atualizado ou None se não encontrado.
        """
        author = self.author_repository.get_by_id(author_id)
        if not author:
            return None

        author.name = name
        author.email = email
        updated_author = self.author_repository.update(author)
        return AuthorResponse.model_validate(updated_author)
