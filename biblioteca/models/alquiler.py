# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta

class Alquiler(models.Model):
    
    _name = 'biblioteca.alquiler'
    _description = 'Informacion de alquiler de libros'
    
    libro_id = fields.Many2one(comodel_name='biblioteca.libro',
                               string='Libro',
                               ondelete='cascade',
                               required=True)
    
    name = fields.Char(string='Titulo',related='libro_id.name')
    
    #date
    
    clientes_ids = fields.Many2many(comodel_name='res.partner',
                                    string='Usuarios')
    
    cliente = fields.Many2one(comodel_name='res.partner',string='Cliente')
    
    libros_ids = fields.Many2many(comodel_name='libro_id.name',
                                  string='Libros')
    
    
    fechaI = fields.Date(string='Fecha Inicio',
                        default=fields.Date.today)
    
    fechaF = fields.Date(string='Fecha Final',
                        compute='_compute_fechaF',
                        inverse='_inverse_fechaF',
                        store=True)
    
    duracion = fields.Integer(string='Duracion',
                             default=1)
    
    
    @api.depends('fechaI','duracion')
    def _compute_fechaF(self):
        for valor in self:
            if not(valor.fechaI and valor.duracion):
                valor.fechaF=valor.fechaI
            else:
                duracion = timedelta(days=valor.duracion)
                valor.fechaF = valor.fechaI+duracion
    
    def _inverse_fechaF(self):
        for valor in self:
            if valor.fechaI and valor.fechaF:
                valor.duracion = (valor.fechaF - valor.fechaI).days + 1
            else:
                continue