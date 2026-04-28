from sqlalchemy.orm import Session
from typing import TypeVar, Type, Generic

T = TypeVar('T')

class BaseRepository(Generic[T]):
    """Repositório genérico com operações CRUD básicas para qualquer modelo SQLAlchemy."""

    def __init__(self, session: Session, model: Type[T]):
        """
        Args:
            session (Session): Sessão do banco de dados.
            model (Type[T]): Classe do modelo SQLAlchemy a ser gerenciado.
        """
        self.session = session
        self.model = model

    def get_all(self) -> list[T]:
        """Retorna todos os registros do modelo.

        Returns:
            list[T]: Lista com todos os registros encontrados.
        """
        return self.session.query(self.model).all()

    def get_by_id(self, id: int) -> T | None:
        """Busca um registro pelo ID.

        Args:
            id (int): ID do registro a ser buscado.

        Returns:
            T | None: O registro encontrado ou None se não existir.
        """
        return self.session.query(self.model).filter(self.model.id == id).first()

    def add(self, entity: T) -> T:
        """Persiste um novo registro no banco de dados.

        Args:
            entity (T): Instância do modelo a ser salva.

        Returns:
            T: A entidade salva e atualizada com os dados do banco.
        """
        self.session.add(entity)
        self.session.commit()
        self.session.refresh(entity)
        return entity

    def update(self, entity: T) -> T:
        """Atualiza um registro existente no banco de dados.

        Args:
            entity (T): Instância do modelo com os dados atualizados.

        Returns:
            T: A entidade atualizada e sincronizada com o banco.
        """
        self.session.merge(entity)
        self.session.commit()
        self.session.refresh(entity)
        return entity

    def delete(self, id: int):
        """Remove um registro pelo ID.

        Args:
            id (int): ID do registro a ser removido.

        Returns:
            T | None: A entidade removida ou None se não encontrada.
        """
        entity = self.get_by_id(id)
        if entity:
            self.session.delete(entity)
            self.session.commit()
            return entity
