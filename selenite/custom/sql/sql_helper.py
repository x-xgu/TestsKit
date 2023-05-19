from sqlalchemy import Engine
from sqlalchemy.orm import sessionmaker


class SQLHelper:
    """
    Helper class for SQL operations
    """

    def __init__(
            self,
            engine: Engine
    ) -> None:
        """
        Initialize SQLHelper

        Args:
            engine (Engine): SQL engine
        """
        self._engine = engine
        self._session = sessionmaker(bind=self._engine)
        self.session = self._session()

    def __del__(self) -> None:
        """
        Close session
        """
        self.session.close()

    def commit(self) -> None:
        """
        Commit changes

        Returns:
            None
        """
        self.session.commit()

    def rollback(self) -> None:
        """
        Rollback changes

        Returns:
            None
        """
        self.session.rollback()
