
from . import ControllerObject
from datetime import datetime, date
from app import app, db
from app.models.myModel2 import Pokemon


def GetAllPkm():
    pkms = Pokemon.query.all()
    return ControllerObject(
        payload=[pkm.as_dict() for pkm in pkms], status=200)

