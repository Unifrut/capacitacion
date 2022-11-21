# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Libro(models.Model):
    
    _name = 'biblioteca.libro'
    _description = 'Informacion de Libro'
    
    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    autor = fields.Text(string='Author')
    genero = fields.Text(string='Genere')
    editor = fields.Text(string='Editor')
    editorial = fields.Text(string='Editorial')
    año = fields.Integer(string='Año')
    isbn = fields.Integer(string='ISBN')
    active = fields.Boolean(string='Active', default=True)
    
    ubicacion = fields.Selection(string='Ubicacion',
                            selection=[('bA', 'Bloque A'),
                                       ('bB', 'Bloque B'),
                                       ('bC', 'Bloque C'),
                                       ('bD', 'Bloque D'),
                                       ('bE', 'Bloque E')],
                            copy=False)
    precio = fields.Float(string='Precio', default=0.00)
    paginas = fields.Integer(string='No Paginas', default=0)
    
    """alquiler_ids = fields.One2many(comodel_name='biblioteca.alquiler',
                                  inverse_name='libro_id', 
                                  string='Alquiler')
  
    @api.onchange('precio')
    def _onchange_precio(self):
        if self < 0.00:
            raise UserError(_('El precio no puede ser negativo.'))
      """      
    @api.onchange('isbn')
    def _onchange_isbn(self): 
         if (len(self) >10):
            raise exceptions.ValidationError("El isbn no debe de pasar los 10 caracteres")
   
   

       