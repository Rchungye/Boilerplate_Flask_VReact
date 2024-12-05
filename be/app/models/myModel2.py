from app import db
from datetime import datetime
from app.models.myModel1 import Ability, pokemon_ability


pokemon_type = db.Table('pokemon_type',
    db.Column('pokemon_id', db.Integer, db.ForeignKey('pokemon.id'), primary_key=True),
    db.Column('type_pkm_id', db.Integer, db.ForeignKey('type_pkm.id'), primary_key=True)
)


class TypePkm(db.Model):
    __tablename__ = "type_pkm"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20), nullable=False)
    pokemons = db.relationship('Pokemon', secondary=pokemon_type, back_populates='types')
    
    def as_dict(self):
        return{
            "id": self.id,
            "nombre": self.nombre,
        }


class Pokemon(db.Model):
    __tablename__ = "pokemon"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20), nullable=False)
    sprite  = db.Column(db.String(255), nullable=False)
    abilities = db.relationship('Ability', secondary=pokemon_ability, back_populates='pokemons')
    types = db.relationship('TypePkm', secondary=pokemon_type, back_populates='pokemons')

    def as_dict(self):
        return{
            "id": self.id,
            "nombre": self.nombre,
            "sprite": self.sprite,
            "abilities": [ability.as_dict() for ability in self.abilities],
            "types": [type.as_dict() for type in self.types]
        }