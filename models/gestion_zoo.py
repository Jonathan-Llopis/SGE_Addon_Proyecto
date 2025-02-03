# -*- coding: utf-8 -*-

from odoo import models, fields, api

class GestionZoo(models.Model):
    _name = 'gestion.zoo'
    _description = 'Gestión Zoo'

    name = fields.Char(required=True, string="Nombre")
    logo_zoo = fields.Binary(string="Logo")
    ciudad = fields.Char()
    provincia = fields.Many2one("res.country.state")
    pais = fields.Many2one("res.country", string="País", compute='_compute_pais', readonly=True)
    zoo_animales = fields.One2many("gestion.zoo.animal", "animales_zoo", string="Animales en el Zoo")
    computo_animales = fields.Integer(compute='_compute_numero_animales')
    habitats_zoo = fields.Many2many("gestion.zoo.habitat", compute="_compute_habitats", string="Habitats")
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
    extension_calculada = fields.Char(string="Extensión", compute='_compute_extension_calculada')
    sequence = fields.Integer('Sequence', default=1)
    habitats_zoo_count = fields.Integer(compute='_compute_habitats_zoo_count')



    _sql_constraints = [
        ('name_zoo_unique', 'unique(name)', 'El Nombre debe ser único'),
    ]
    
    @api.onchange('unidad_extension')
    def _onchange_extension(self):
            if self.unidad_extension == 'm':
                self.extension = self.extension * 10000
            elif self.unidad_extension == 'h':
                self.extension = self.extension / 10000


    @api.depends('extension', 'unidad_extension')
    def _compute_extension_calculada(self):
        for record in self:
            if record.unidad_extension == 'm':
                record.extension_calculada = f"{record.extension} m²"
            elif record.unidad_extension == 'h':
                record.extension_calculada = f"{record.extension} ha"
            else:
                record.extension_calculada = str(record.extension)
                
    @api.depends('provincia')
    def _compute_pais(self):
        for record in self:
            record.pais = record.provincia.country_id if record.provincia else False
            
    @api.depends('zoo_animales')
    def _compute_numero_animales(self):
        for record in self:
            if record.zoo_animales:
                record.computo_animales = len(record.zoo_animales)
            else:
                record.computo_animales = 0
    @api.depends('zoo_animales')
    def _compute_habitats(self):
        for record in self:
            habitats = record.zoo_animales.mapped('habitat_animal')
            record.habitats_zoo = habitats
        
    @api.depends('habitats_zoo')    
    def _compute_habitats_zoo_count(self):
        for record in self:
            record.habitats_zoo_count = len(record.habitats_zoo)

    
    def action_view_habitats(self):
        res = self.env.ref("gestion_zoo.gestion_zoo_habitats_action_zoo").read()[0]
        res["domain"] = [("id", "in", self.habitats_zoo.ids)]
        return res