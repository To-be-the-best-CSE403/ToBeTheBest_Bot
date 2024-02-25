import asyncio
from flask import Blueprint, jsonify, request
from src.bot import challenge_player

views = Blueprint("views", __name__)


@views.route("/home")
def api_home():
    return "ToBeTheBest Bot API"


@views.route("/challenge", methods=["GET"])
def api_challenge():
    name = request.args.get("name")
    if not name:
        return jsonify({"error": "No name parameter provided"}), 400
    
    asyncio.get_event_loop().run_until_complete(challenge_player(name))
    return jsonify({"message": "Bot challenged!"})