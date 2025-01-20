# -*- coding: utf-8 -*-

from odoo import models, fields

class GestionZooFamilia(models.Model):
    _name = "gestion.zoo.familia"
    _description = "Gestión Zoo Familia"

    nombre = fields.Char(required=True)
        
   # Relacions proposades:
        #(1-M) Especies (1-M)SubFamilia