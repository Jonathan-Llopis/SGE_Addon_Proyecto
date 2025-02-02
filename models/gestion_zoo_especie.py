from odoo import models, fields, api

class GestionZooEspecie(models.Model):
    _name = 'gestion.zoo.especie'
    _description = 'Gestión Zoo Especie'

    nombre_vulgar = fields.Char(required=True)
    nombre_cientifico = fields.Char(required=True)
    peligro_extincion = fields.Boolean(default=False, string='Peligro Extinción')
    animales_especie = fields.One2many("gestion.zoo.animal" "raza_especie")
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
    color_dieta = fields.Char(string='Color Dieta', compute='_compute_color_dieta', store=True)
    color_grado_peligro = fields.Char(string='Color Grado Peligro', compute='_compute_color_grado_peligro', store=True)
    color_familia = fields.Char(string='Color Familia', compute='_compute_color_familia', store=True)

    @api.depends('dieta')
    def _compute_color_dieta(self):
        for record in self:
            if record.dieta == 'carnivora':
                record.color_dieta = '#FF0000'
            elif record.dieta == 'herbivora':
                record.color_dieta = '#00FF00'
            elif record.dieta == 'omnivora':
                record.color_dieta = '#FFFF00'
            else:
                record.color_dieta = '#FFFFFF'

    @api.depends('grado_peligro')
    def _compute_color_grado_peligro(self):
        for record in self:
            color_map = {
                '1': '#00FF00',
                '2': '#FFFF00',
                '3': '#FFA500',
                '4': '#FF4500',
                '5': '#FF0000',
                '6': '#8B0000',
            }
            record.color_grado_peligro = color_map.get(record.grado_peligro, '#FFFFFF')

    @api.depends('familia')
    def _compute_color_familia(self):
        for record in self:
            color_map = {
                'mamifero': '#0000FF',
                'ave': '#FF6347',
                'reptil': '#008000',
                'anfibio': '#00FFFF',
                'pez': '#4682B4',
                'insecto': '#FFD700',
                'aracnido': '#800080',
                'crustaceo': '#B22222',
                'molusco': '#00BFFF',
            }
            record.color_familia = color_map.get(record.familia, '#FFFFFF')
