from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class tbl_tv(Base):
    __tablename__ = 'tbl_tv'
    nama_tv: Mapped[str] = mapped_column(primary_key=True)
    reputasi_brand: Mapped[int] = mapped_column()
    resolusi: Mapped[int] = mapped_column()
    daya: Mapped[int] = mapped_column()
    harga: Mapped[int] = mapped_column()
    ukuran_layar: Mapped[int] = mapped_column()
    
    def __repr__(self) -> str:
        return f"tbl_tv(nama_tv={self.nama_tv!r}, reputasi_brand={self.reputasi_brand!r})"