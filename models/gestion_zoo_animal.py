# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date, datetime

from odoo.exceptions import ValidationError

class GestionZooAnimal(models.Model):
    _name = "gestion.zoo.animal"
    _description = "Gestión Zoo Animal"

    sexo = fields.Selection(selection=[('macho', 'Macho'), ('hembra','Hembra')])
    fecha_nacimiento = fields.Date(required=True)
    edad = fields.Integer(compute='get_age', readonly=True)
    continente=fields.Selection(selection=(("europa", "Europa"), ("asia", "Asia"), ("africa" , "África"), 
                                           ("norteamerica", "NorteAmérica"), ("sudamerica", "SudAmérica"),("oceania" , "Oceanía"), ("antartida", "Antártida")))
    # Relacions proposades:
        #(M-1)Pais, (M-1)Habitat, (M-1)Especie, (M-1)Zoo  (M-1) Raza
    
    @api.depends('fecha_nacimiento')
    def _get_age(self):
        for r in self:
            if r.birthday:
                bdate = datetime.strptime(r.fecha_nacimiento, "%Y-%m-%d").date()
                today = date.today()
                diffdate = today - bdate
                years = diffdate.days/365
                r.age = years.as_integer_ratio
    
    @api.constrains('fecha_nacimiento')
    def _check_fecha_nacimiento(self):
        for record in self:
            if record.fecha_nacimiento > fields.Date.today():
                raise ValidationError("La fecha de nacimiento no debe ser mas que la fecha actual")