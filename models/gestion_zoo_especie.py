from odoo import models, fields, api
from odoo.exceptions import UserError

class GestionZooEspecie(models.Model):
    _name = 'gestion.zoo.especie'
    _description = 'Gestión Zoo Especie'

    name = fields.Char(required=True, string="Nombre Vulgar")
    name_cientifico = fields.Char(required=True)
    peligro_extincion = fields.Boolean(default=False, string='Peligro Extinción')
    animales_especie = fields.One2many("gestion.zoo.animal", "especie_animal")
    especies_zoo = fields.Many2many("gestion.zoo", compute="_compute_zoo" )
    habitat_especies = fields.Many2one("gestion.zoo.habitat")
    dieta = fields.Selection(selection=[('carnivora','Carnívora'),
                                        ('herbivora', 'Herbívora'),
                                        ('omnivora','Omnívora')], required=True, default = 'carnivora')
    grado_peligro = fields.Selection(selection=[('1', 'Seguro'),
                                                ('2','Riesgo Bajo'),
                                                ('3', 'Riesgo Moderado'),
                                                ('4', 'Peligroso'),
                                                ('5','Altamente Peligroso'),
                                                ('6', 'Peligro Crítico/Ecológico')], required=True)
    
    familia = fields.Selection(selection=[  ('mamifero', 'Mamíferos'),
                                            ('ave', 'Aves'),
                                            ('reptil', 'Reptiles'),
                                            ('anfibio', 'Anfibios'),
                                            ('pez', 'Peces'),
                                            ('insecto', 'Insectos'),
                                            ('aracnido', 'Arácnido'),
                                            ('crustaceo', 'Crustáceo'),
                                            ('molusco', 'Molusco')], default = 'mamifero')


 

    
    @api.depends('animales_especie')
    def _compute_zoo(self):
        for record in self:
            zoos = record.animales_especie.mapped('animales_zoo')
            record.especies_zoo = zoos
    
    @api.ondelete(at_uninstall=False)
    def delete_especie(self):
        for especie in self:
            if especie.animales_especie:
                raise UserError("No se puede borrar un zoológico que tiene animales.")