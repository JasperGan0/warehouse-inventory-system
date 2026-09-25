from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "items"

    id: Mapped[int] = mapped_column(primary_key=True)
    sku: Mapped[str] = mapped_column(String(50))
    name: Mapped[str] = mapped_column(String(100))
    quantity: Mapped[int] = mapped_column(Integer, default=1)
    bin_location: Mapped[str] = mapped_column(String(50))
    qr_path: Mapped[str] = mapped_column(String(50))
