# -*- coding: utf-8 -*-

from odoo import models, fields, api

class GestionZooEspecie(models.Model):
    _name = "gestion.zoo.especie"
    _description = "Gestión Zoo Especie"

    nombre_vulgar = fields.Char(required=True)
    nombre_cientifico = fields.Char(required=True)
    peligro_extincion = fields.Bool(default=False, string="Peligro Extinción")
    dieta = fields.Selection(selection=(("canrivora","Carnívora"),("herbivora", "Herbívora"),("omnivora","Omnívora") ))
        
        # Relacions proposades:
            #(M-1)Familia, (M-1) SubFamilia, (M-1)Peligro 