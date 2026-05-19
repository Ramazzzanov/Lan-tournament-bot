
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Tournament(Base):
    __tablename__ = "tournaments"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    game: Mapped[str] = mapped_column(String(50))
