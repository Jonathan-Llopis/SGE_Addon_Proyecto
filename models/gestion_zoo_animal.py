# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date
import math

from odoo.exceptions import ValidationError

class GestionZooAnimal(models.Model):
    _name = 'gestion.zoo.animal'
    _description = 'Gestión Zoo Animal'

    identificador_animal = fields.Char(compute='_compute_identificador_animal', readonly=True)
    sexo = fields.Selection(selection=[('macho', 'Macho'), ('hembra','Hembra')])
    fecha_nacimiento = fields.Date(required=True)
    edad = fields.Integer(compute='get_age', readonly=True)
    animales_zoo = fields.Many2one("gestion.zoo", string="Pertenece al Zoo", required=True)
    habitat_animal = fields.Many2one("gestion.zoo.habitat", string="Habitat del Animal", required=True)
    especie_animal = fields.Many2one("gestion.zoo.especie", string="Especie", required=True)
    raza_especie = fields.Many2one("gestion.zoo.raza", string="Raza del Animal")
    pais_origen = fields.Many2one("res.country", string="País de Origen", required=True)
    continente = fields.Selection(
        selection=[('europa', 'Europa'),
                   ('asia', 'Asia'),
                   ('africa', 'África'), 
                   ('norteamerica', 'NorteAmérica'),
                   ('sudamerica', 'SudAmérica'),
                   ('oceania', 'Oceanía'),
                   ('antartida', 'Antártida')],
        default='europa', required=True
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
                years = diffdate.days // 365 
                animal.edad = years
            else:
                animal.edad = 0 
    
    @api.constrains('fecha_nacimiento')
    def _check_fecha_nacimiento(self):
        for record in self:
            if record.fecha_nacimiento and record.fecha_nacimiento > date.today():
                raise ValidationError('La fecha de nacimiento no debe ser posterior a la fecha actual.')

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
                
    @api.depends('especie_animal', 'sexo', 'continente', 'fecha_nacimiento')
    def _compute_identificador_animal(self):
        for record in self:
            if record.especie_animal and record.especie_animal.nombre_cientifico and record.sexo and record.continente and record.fecha_nacimiento:
                iniciales_nombre_cientifico = ''.join([word[0].upper() for word in record.especie_animal.nombre_cientifico.split()])
                inicial_sexo = record.sexo[0].upper()
                inicial_continente = record.continente[0].upper()
                fecha_nacimiento = record.fecha_nacimiento.strftime('%Y%m%d')
                record.identificador_animal = f"{iniciales_nombre_cientifico}{inicial_sexo}{inicial_continente}{fecha_nacimiento}"
            else:
                record.identificador_animal = ''