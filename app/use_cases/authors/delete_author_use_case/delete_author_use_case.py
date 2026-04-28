from repositories.author_repository import AuthorRepository
from dtos.author_dto import AuthorResponse

class DeleteAuthorUseCase:
    """Caso de uso para remoção de um autor do banco de dados."""

    def __init__(self, author_repository: AuthorRepository):
        """
        Args:
            author_repository (AuthorRepository): Repositório de autores.
        """
        self.author_repository = author_repository

    def execute(self, author_id: int) -> AuthorResponse | None:
        """Remove um autor pelo ID.

        Args:
            author_id (int): ID do autor a ser removido.

        Returns:
            AuthorResponse | None: Os dados do autor removido ou None se não encontrado.
        """
        author = self.author_repository.get_by_id(author_id)
        if not author:
            return None
        response = self.author_repository.delete(author_id)
        return AuthorResponse.model_validate(response)
