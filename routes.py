from flask_restx import Namespace, Resource

api = Namespace("hqs", description="Operações relacionadas às HQs")


@api.route("/")
class HQList(Resource):

    def get(self):
        """Lista todas as HQs"""
        return {"mensagem": "Listando HQs"}

    def post(self):
        """Cadastra uma HQ"""
        return {"mensagem": "HQ cadastrada"}