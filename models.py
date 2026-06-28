from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class HQ(db.Model):
    __tablename__ = "hq"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    autor = db.Column(db.String(100), nullable=False)
    editora = db.Column(db.String(100), nullable=False)
    genero = db.Column(db.String(50), nullable=False)
    volume = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(30), nullable=False)
    nota = db.Column(db.Float)
    imagem = db.Column(db.String(255))

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "autor": self.autor,
            "editora": self.editora,
            "genero": self.genero,
            "volume": self.volume,
            "status": self.status,
            "nota": self.nota,
            "imagem": self.imagem
        }