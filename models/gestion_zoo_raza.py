# -*- coding: utf-8 -*-

from odoo import models, fields

class GestionZooRaza(models.Model):
    _name = "gestion.zoo.raza"
    _description = "Gestión Zoo Raza"

    nombre = fields.Char()
    
    # Relacions proposades:
         #(1-M) Animal
