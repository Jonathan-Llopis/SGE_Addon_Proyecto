# -*- coding: utf-8 -*-

from odoo import models, fields

class GestionZooRaza(models.Model):
    _name = "gestion.zoo.raza"
    _description = "Gestión Zoo Raza"

    nombre = fields.Char( required=True)
    
    _sql_constraints = [
          ('nombre_raza_unique', 'unique(nombre)', 'El nombre debe ser único'),
    ]
    
    # Relacions proposades:
         #(1-M) Animal
