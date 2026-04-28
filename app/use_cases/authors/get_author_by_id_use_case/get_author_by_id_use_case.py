from repositories.author_repository import AuthorRepository
from dtos.author_dto import AuthorResponse
from typing import Optional

class GetAuthorByIdUseCase:
    """Caso de uso para busca de um autor pelo ID."""

    def __init__(self, author_repository: AuthorRepository):
        """
        Args:
            author_repository (AuthorRepository): Repositório de autores.
        """
        self.author_repository = author_repository

    def execute(self, author_id: int) -> Optional[AuthorResponse]:
        """Busca um autor pelo ID.

        Args:
            author_id (int): ID do autor a ser buscado.

        Returns:
            Optional[AuthorResponse]: O autor encontrado ou None se não existir.
        """
        author = self.author_repository.get_by_id(author_id)
        return AuthorResponse.model_validate(author)
