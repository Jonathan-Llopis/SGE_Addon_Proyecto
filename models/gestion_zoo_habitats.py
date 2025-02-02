# -*- coding: utf-8 -*-

from odoo import models, fields, api

class GestionZooHabitat(models.Model):
    _name = 'gestion.zoo.habitat'
    _description = 'Gestión Zoo Hábitat'

    nombre = fields.Char(required=True)
    temperatura = fields.Float(string='Temperatura')
    unidad_temperatura = fields.Selection([
        ('c', 'Celsius'),
        ('f', 'Fahrenheit')
    ], string='Unidad de Temperatura', default='c')
    humedad = fields.Integer(string= 'Humedad Relativa %')     
    animales_habitat = fields.One2many("gestion.zoo.animal", "habitat_animal")
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
        ('nombre_habitat_unique', 'unique(nombre)', 'El nombre del hábitat debe ser único'),
    ]
    
    @api.onchange('unidad_temperatura')
    def _onchange_unidad_temperatura(self):
            if self.unidad_temperatura == 'c':
                self.temperatura = (self.temperatura - 32) * 5.0 / 9.0
            elif self.unidad_temperatura == 'f':
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

    
        # Relacions proposades:
            #(1-M)Animal