# -*- coding: utf-8 -*-

from odoo import models, fields

class GestionZooFamilia(models.Model):
    _name = "gestion.zoo.familia"
    _description = "Gestión Zoo Familia"

    nombre = fields.Char(required=True)
    
    _sql_constraints = [
          ('nombre_family_unique', 'unique(nombre)', 'El nombre debe ser único'),
    ]
        
   # Relacions proposades:
        #(1-M) Especies (1-M)SubFamilia