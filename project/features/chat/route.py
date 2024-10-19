from .blueprint import chat_bp
from .request_validator import request_validator
from .controller import ChatController



@chat_bp.route("/chat",methods=["POST"])
@request_validator.validate_create_chat()
def create_chat(validated_data):
    controller=ChatController()
    response=controller.create_chat(validated_data)
    return response,201
@chat_bp.route("/chat_archive/<uuid:chat_id>",methods=["GET"])
def get_chat(chat_id):
    controller=ChatController()
    response=controller.get_chat(chat_id)
    return response,201
@chat_bp.route("/mark_read",methods=["POST"])
def marke_it(chat_id):
    controller=ChatController()
    response=controller.get_chat(chat_id)
    return response,201