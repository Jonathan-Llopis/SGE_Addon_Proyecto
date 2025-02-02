# -*- coding: utf-8 -*-

from odoo import models, fields

class GestionZooRaza(models.Model):
    _name = 'gestion.zoo.raza'
    _description = 'Gestión Zoo Raza'

    name = fields.Char( required=True, string="Nombre")
    animales_raza = fields.One2many("gestion.zoo.animal", "raza_animal")
    
    _sql_constraints = [
            ('name_raza_unique', 'unique(name)', 'El name debe ser único'),
    ]
    
    # Relacions proposades:
         #(1-M) Animal
