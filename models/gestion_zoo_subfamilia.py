# -*- coding: utf-8 -*-

from odoo import models, fields

class GestionZooSubFamilia(models.Model):
    _name = "gestion.zoo.subfamilia"
    _description = "Gestión Zoo SubFamilia"

    nombre = fields.Char()

    # Relacions proposades:
        #(1-M) Especies (M-1)Familia
