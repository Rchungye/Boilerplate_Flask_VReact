from app import app
import json
from flask import jsonify, request
from app.Controllers import (
    myController2 as Pokemon,
)


@app.route("/pokemon/all", methods=["GET"])
def GetAllPokemon():
    result = Pokemon.GetAllPkm()
    return result.jsonify()


