# -*- coding: utf-8 -*-

from odoo import models, fields

class GestionZooSubFamilia(models.Model):
    _name = "gestion.zoo.subfamilia"
    _description = "Gestión Zoo SubFamilia"

    nombre = fields.Char()

    _sql_constraints = [
          ('nombre_subfamily_unique', 'unique(nombre)', 'El nombre debe ser único'),
    ]

    # Relacions proposades:
        #(1-M) Especies (M-1)Familia
