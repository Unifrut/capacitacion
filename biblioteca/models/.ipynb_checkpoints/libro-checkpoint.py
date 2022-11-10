# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Libro(models.Model):
    
    _name = 'biblioteca.libro'
    _description = 'Informacion de Libro'
    
    name = fields.Text(string='Title', required=True)
    description = fields.Text(string='Description')
    autor = fields.Text(string='Author')
    genero = fields.Text(string='Genere')
    editor = fields.Text(string='Editor')
    editorial = fields.Text(string='Editorial')
    año = fields.Integer(string='Año')
    isbn = fields.Integer(string='ISBN')
    active = fields.Boolean(string='Active', default=True)