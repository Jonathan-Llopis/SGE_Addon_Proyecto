# -*- coding: utf-8 -*-

from odoo import models, fields

class GestionZooPeligro(models.Model):
    _name = "gestion.zoo.peligro"
    _description = "Gestión Zoo Peligro"

    grado_peligro = fields.Selection(selection=((1, "Seguro"), (2,"Riesgo Bajo"), (3, "Riesgo Moderado"),
                                                (4, "Peligroso"), (5,"Altamente Peligroso"), (6, "Peligro Crítico/Ecológico")))
     
    # Relacions proposades:
        #(1-M) Especie
