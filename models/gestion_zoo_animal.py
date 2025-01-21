# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date, datetime
import math

from odoo.exceptions import ValidationError

class GestionZooAnimal(models.Model):
    _name = "gestion.zoo.animal"
    _description = "Gestión Zoo Animal"

    sexo = fields.Selection(selection=[('macho', 'Macho'), ('hembra','Hembra')])
    fecha_nacimiento = fields.Date(required=True)
    edad = fields.Integer(compute='get_age', readonly=True)
    continente=fields.Selection(selection=(("europa", "Europa"),
                                           ("asia", "Asia"),
                                           ("africa" , "África"), 
                                           ("norteamerica", "NorteAmérica"),
                                           ("sudamerica", "SudAmérica"),
                                           ("oceania" , "Oceanía"),
                                           ("antartida", "Antártida")))
    # Relacions proposades:
        #(M-1)Pais, (M-1)Habitat, (M-1)Especie, (M-1)Zoo  (M-1) Raza
    
    @api.depends('fecha_nacimiento')
    def get_age(self):
        for animal in self:
            if animal.fecha_nacimiento:
                today = date.today()
                diffdate = today - animal.fecha_nacimiento
                years = diffdate.days/365
                animal.edad = math.floor(years)
    
    @api.constrains('fecha_nacimiento')
    def _check_fecha_nacimiento(self):
        for record in self:
            if record.fecha_nacimiento > date.today():
                raise ValidationError("La fecha de nacimiento no debe ser mas que la fecha actual")