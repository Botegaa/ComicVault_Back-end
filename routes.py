from flask_restx import Namespace, Resource, fields
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
        return [hq.to_dict() for hq in hqs], 200

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


@api.route("/nome/<string:titulo>")
class HQBuscaPorNome(Resource):
    def get(self, titulo):
        """Busca HQs pelo título"""

        hqs = HQ.query.filter(HQ.titulo.ilike(f"%{titulo}%")).all()

        if not hqs:
            return {"erro": "Nenhuma HQ encontrada com esse título"}, 404

        return [hq.to_dict() for hq in hqs], 200


@api.route("/status/<string:status>")
class HQBuscaPorStatus(Resource):
    def get(self, status):
        """Busca HQs pelo status"""

        hqs = HQ.query.filter(HQ.status.ilike(f"%{status}%")).all()

        if not hqs:
            return {"erro": "Nenhuma HQ encontrada com esse status"}, 404

        return [hq.to_dict() for hq in hqs], 200


@api.route("/<int:id>")
class HQResource(Resource):

    def get(self, id):
        """Busca uma HQ pelo ID"""
        hq = HQ.query.get(id)

        if not hq:
            return {"erro": "HQ não encontrada"}, 404

        return hq.to_dict(), 200

    @api.expect(hq_model)
    def put(self, id):
        """Atualiza uma HQ pelo ID"""
        hq = HQ.query.get(id)

        if not hq:
            return {"erro": "HQ não encontrada"}, 404

        dados = api.payload

        hq.titulo = dados["titulo"]
        hq.autor = dados["autor"]
        hq.editora = dados["editora"]
        hq.genero = dados["genero"]
        hq.volume = dados["volume"]
        hq.status = dados["status"]
        hq.nota = dados["nota"]
        hq.imagem = dados.get("imagem")

        db.session.commit()

        return {
            "mensagem": "HQ atualizada com sucesso!",
            "hq": hq.to_dict()
        }, 200

    def delete(self, id):
        """Exclui uma HQ pelo ID"""
        hq = HQ.query.get(id)

        if not hq:
            return {"erro": "HQ não encontrada"}, 404

        db.session.delete(hq)
        db.session.commit()

        return {"mensagem": "HQ excluída com sucesso!"}, 200