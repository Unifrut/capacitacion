# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Alquiler(models.Model):
    
    _name = 'biblioteca.alquiler'
    _description = 'Informacion de alquiler de libros'
    
    libro_id = fields.Many2one(comodel_name='biblioteca.libro',
                               string='Libro',ondelete='cascade',
                               required=True)
    
    name = fields.Char(string='Titulo',related='libro_id.name')
    
    #date
    
    clientes_ids = fields.Many2many(comodel_name='res.partner',string='Usuarios')
    