from flask_restx import Namespace, Resource
from flask_restx import fields
from models import db, HQ

api = Namespace("hqs", description="Operações relacionadas às HQs")

hq_model = api.model(
    "HQ",
    {
        "titulo": fields.String(required=True, description="Título da HQ"),
        "autor": fields.String(required=True, description="Autor"),
        "editora": fields.String(required=True, description="Editora"),
        "genero": fields.String(required=True, description="Gênero"),
        "volume": fields.Integer(required=True, description="Volume"),
        "status": fields.String(required=True, description="Status da leitura"),
        "nota": fields.Float(required=True, description="Nota"),
        "imagem": fields.String(description="URL da capa")
    }
)


@api.route("/")
class HQList(Resource):
    def get(self):
        """Lista todas as HQs"""

        hqs = HQ.query.all()

        return [hq.to_dict() for hq in hqs]
    @api.expect(hq_model)
    def post(self):
        """Cadastra uma HQ"""

        dados = api.payload

        nova_hq = HQ(
            titulo=dados["titulo"],
            autor=dados["autor"],
            editora=dados["editora"],
            genero=dados["genero"],
            volume=dados["volume"],
            status=dados["status"],
            nota=dados["nota"],
            imagem=dados.get("imagem")
        )

        db.session.add(nova_hq)
        db.session.commit()

        return {
            "mensagem": "HQ cadastrada com sucesso!",
            "id": nova_hq.id
        }, 201