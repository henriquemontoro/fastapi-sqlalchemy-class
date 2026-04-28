from repositories.author_repository import AuthorRepository
from dtos.author_dto import AuthorResponse

class GetAllAuthorsUseCase:
    """Caso de uso para listagem de todos os autores."""

    def __init__(self, author_repository: AuthorRepository):
        """
        Args:
            author_repository (AuthorRepository): Repositório de autores.
        """
        self.author_repository = author_repository

    def execute(self) -> list[AuthorResponse]:
        """Busca todos os autores cadastrados.

        Returns:
            list[AuthorResponse]: Lista com todos os autores.
        """
        authors = self.author_repository.get_all()
        return [AuthorResponse.model_validate(author) for author in authors]
