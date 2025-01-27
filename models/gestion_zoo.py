# -*- coding: utf-8 -*-

from odoo import models, fields, api

class GestionZoo(models.Model):
    _name = 'gestion.zoo'
    _description = 'Gestión Zoo'

    nombre = fields.Char(required=True)
    ciudad = fields.Char()
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
    extension_establecida = fields.Boolean(default=False)

    _sql_constraints = [
        ('nombre_zoo_unique', 'unique(nombre)', 'El nombre debe ser único'),
    ]
    
    @api.onchange('unidad_extension', 'extension')
    def _onchange_extension(self):
        if self.extension and self.extension_establecida:
            if self.unidad_extension == 'm':
                self.extension = self.extension * 10000
            elif self.unidad_extension == 'h':
                self.extension = self.extension / 10000
        self.extension_establecida = True


    @api.depends('extension', 'unidad_extension')
    def _compute_extension_con_prefijo(self):
        for record in self:
            if record.unidad_extension == 'm':
                record.extension_con_prefijo = f"{record.extension} m²"
            elif record.unidad_extension == 'h':
                record.extension_con_prefijo = f"{record.extension} ha"
            else:
                record.extension_con_prefijo = str(record.extension)
    
    # Relaciones propuestas (M-1) Provincia, (M-1) País, (1-M) Animal
