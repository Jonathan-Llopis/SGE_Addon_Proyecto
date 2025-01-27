# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date
import math

from odoo.exceptions import ValidationError

class GestionZooAnimal(models.Model):
    _name = 'gestion.zoo.animal'
    _description = 'Gestión Zoo Animal'

    sexo = fields.Selection(selection=[('macho', 'Macho'), ('hembra','Hembra')])
    fecha_nacimiento = fields.Date(required=True)
    edad = fields.Integer(compute='get_age', readonly=True)
    continente = fields.Selection(
        selection=[('europa', 'Europa'),
                   ('asia', 'Asia'),
                   ('africa', 'África'), 
                   ('norteamerica', 'NorteAmérica'),
                   ('sudamerica', 'SudAmérica'),
                   ('oceania', 'Oceanía'),
                   ('antartida', 'Antártida')],
        default='europa'
    )
    
    # Relacions proposadas:
    #(M-1)Pais, (M-1)Habitat, (M-1)Especie, (M-1)Zoo  (M-1) Raza
    
    color_continente = fields.Char(
        string='Color Continente', compute='_compute_color_continente', store=True
    )
    
    @api.depends('fecha_nacimiento')
    def get_age(self):
        for animal in self:
            if animal.fecha_nacimiento:
                today = date.today()
                diffdate = today - animal.fecha_nacimiento
                years = diffdate.days / 365
                animal.edad = math.floor(years)
            else:
                animal.edad = 0 
    
    @api.constrains('fecha_nacimiento')
    def _check_fecha_nacimiento(self):
        for record in self:
            if record.fecha_nacimiento > date.today():
                raise ValidationError('La fecha de nacimiento no debe ser más que la fecha actual')

    @api.depends('continente')
    def _compute_color_continente(self):
        for record in self:
            if record.continente == 'asia':
                record.color_continente = '#FF6347'  
            elif record.continente == 'africa':
                record.color_continente = '#32CD32'  
            elif record.continente == 'europa':
                record.color_continente = '#1E90FF' 
            elif record.continente == 'norteamerica':
                record.color_continente = '#FFD700'  
            elif record.continente == 'sudamerica':
                record.color_continente = '#FFD700' 
            elif record.continente == 'oceania':
                record.color_continente = '#8A2BE2' 
            elif record.continente == 'antartida':
                record.color_continente = '#FFFFFF'  
            else:
                record.color_continente = '#FFFFFF'  