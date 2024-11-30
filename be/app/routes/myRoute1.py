from app import app
import json
from flask import jsonify, request
from app.Controllers import (
    myController1 as Ability,
)


@app.route("/ability/all", methods=["GET"])
def GetAllAbility():
    result = Ability.GetAllAbility()
    return result.jsonify()
