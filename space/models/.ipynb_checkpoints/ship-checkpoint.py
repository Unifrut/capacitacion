# -*- coding:utf-8 -*-

from odoo import models, fields, api

class nave(models.Model):
    
    _name = 'space.course'
    _description = 'Mission Espacial'
    
    name = fields.Char(string='Title', required=True)
    
    nave_dimension = fields.Selection(string='Dimension de la nave',
                                    selection=[('10', '10m'),
                                               ('20', '20m'),
                                               ('30', '30m')])
    
    nave_combustible = fields.Selection(string='Tipo de combustible',
                                    selection=[('Magnum', 'Magnum'),
                                               ('Premium', 'Premium'),
                                               ('Disel', 'Disel')])
    
    nave_tipo = fields.Selection(string='Tipo de nave',
                                    selection=[('Sobrevuelo', 'Sobrevuelo'),
                                               ('Atmosferica', 'Atmosferica'),
                                               ('Penetradora', 'Penetradora')])
    
    nave_pasajeros = fields.Selection(string='Numero de pasajeros',
                                    selection=[('2', '2'),
                                               ('4', '4'),
                                               ('10', '10')])
    
    active = fields.Boolean(string='Active', default=True)