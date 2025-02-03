# -*- coding: utf-8 -*-

from odoo import models, fields, api

class GestionZooHabitat(models.Model):
    _name = 'gestion.zoo.habitat'
    _description = 'Gestión Zoo Hábitat'

    name = fields.Char(required=True, string="Nombre")
    temperatura = fields.Float(string='Temperatura')
    unidad_temperatura = fields.Selection([
        ('c', 'Celsius'),
        ('f', 'Fahrenheit')
    ], string='Unidad de Temperatura', default='c')
    humedad = fields.Integer(string= 'Humedad Relativa %')     
    animales_habitat = fields.One2many("gestion.zoo.animal", "habitat_animal")
    especie_habitats = fields.Many2many("gestion.zoo.especie",  compute="_compute_especies")
    tipo_habitat = fields.Selection(selection=[
        ('terrestre', 'Terrestre'), 
        ('acuatico', 'Acuático'), 
        ('marino', 'Marino'), 
        ('escalable', 'Con Objetos Escalables'), 
        ('aereo', 'Aéreo'),
        ('mixto', 'Mixto (Terrestre y Acuático)')
    ], string='Tipo de Hábitat')
    
    temperatura_con_unidad = fields.Char(string="Temperatura con Unidad", compute="_compute_temperatura_con_unidad", store=True)
    _sql_constraints = [
        ('name_habitat_unique', 'unique(name)', 'El Nombre del hábitat debe ser único'),
    ]
    
    @api.onchange('unidad_temperatura')
    def _onchange_unidad_temperatura(self):
        if self.unidad_temperatura == 'c' and self.temperatura is not None:
            self.temperatura = (self.temperatura - 32) * 5.0 / 9.0
        elif self.unidad_temperatura == 'f' and self.temperatura is not None:
            self.temperatura = self.temperatura * 9.0 / 5.0 + 32

    @api.depends('temperatura', 'unidad_temperatura')
    def _compute_temperatura_con_unidad(self):
        for record in self:
            if record.temperatura is not None:
                if record.unidad_temperatura == 'c':
                    record.temperatura_con_unidad = f"{record.temperatura} °C"
                elif record.unidad_temperatura == 'f':
                    record.temperatura_con_unidad = f"{record.temperatura} °F"
            else:
                record.temperatura_con_unidad = "N/A"

    @api.depends('animales_habitat')
    def _compute_especies(self):
        for record in self:
            especies = record.animales_habitat.mapped('especie_animal')
            record.especie_habitats = especies
    
