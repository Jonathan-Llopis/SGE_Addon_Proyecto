# -*- coding: utf-8 -*-

from odoo import models, fields, api

class GestionZoo(models.Model):
    _name = 'gestion.zoo'
    _description = 'Gestión Zoo'

    nombre = fields.Char(required=True)
    logo_zoo = fields.Binary(string="Logo")
    ciudad = fields.Char()
    provincia = fields.Many2one("res.country.state")
    pais = fields.Many2one("es.country", string="País", compute='_compute_pais', store=True)
    animalesZoo = fields.One2many("gestion.zoo.animal", "animales_zoo", string="Animales en el Zoo")
    computoAnimales = fields.Integer(compute='_compute_numero_animales')
    extension = fields.Float(string='Extensión')
    unidad_extension = fields.Selection(
        selection=[('m', 'Metros Cuadrados'), ('h', 'Hectárea')],
        string='Unidad de Extensión', default='m'
    )
    tipo = fields.Selection(
        selection=[('tradicional', 'Tradicional'),
                   ('safari', 'Safari'),
                   ('especializado', 'Especializado'),
                   ('bioparque', 'Bioparque'),
                   ('acuario', 'Acuario')],
        required=True
    )
    extension_con_prefijo = fields.Char(string="Extensión con Prefijo", compute='_compute_extension_con_prefijo')
    sequence = fields.Integer('Sequence', default=1)
    

    _sql_constraints = [
        ('nombre_zoo_unique', 'unique(nombre)', 'El nombre debe ser único'),
    ]
    
    @api.onchange('unidad_extension')
    def _onchange_extension(self):
            if self.unidad_extension == 'm':
                self.extension = self.extension * 10000
            elif self.unidad_extension == 'h':
                self.extension = self.extension / 10000


    @api.depends('extension', 'unidad_extension')
    def _compute_extension_con_prefijo(self):
        for record in self:
            if record.unidad_extension == 'm':
                record.extension_con_prefijo = f"{record.extension} m²"
            elif record.unidad_extension == 'h':
                record.extension_con_prefijo = f"{record.extension} ha"
            else:
                record.extension_con_prefijo = str(record.extension)
                
    @api.depends('provincia')
    def _compute_pais(self):
        for record in self:
            record.pais = record.provincia.country_id if record.provincia else False
            
    @api.depends('animalesZoo')
    def _compute_numero_animales(self):
        for record in self:
            record.computoAnimales = len(record.animalesZoo)
    
    # Relaciones propuestas (M-1) Provincia, (M-1) País, (1-M) Animal
