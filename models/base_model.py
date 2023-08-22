#!/usr/bin/python3
"""
This is the model where all modul is definded
"""

import models
import uuid
from datetime import datetime

class BaseModel:
    """
    Representation of all attributes and models of HBNB project
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize new baseModel
        self.id : Lorsqu4une instance est cree nous generons automatiquement un identifiant unique et le convertissons en chqine

        self.created_at = datetime.now(): Enregistre la date et l'heure actuelles au moment de la creation de l'instance

        self.update_at = self.created_at: Initialise avec la meme valeur au moment de la creation
        """

        timestamp_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def save(self):
        """
        Updates the public instance attribute updated_at
        with the current datetime and saves the object to storage.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        return a dictionnary cointaining all keys/values
        """
        result = self.__dict__.copy()
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        result["__class__"] = self.__class__.__name__
        return result

    def __str__(self):
        """
        Return the string representation of the BaseModel instance
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) <{}>".format(class_name, self.id, self.__dict__)
