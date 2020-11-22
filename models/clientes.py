# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Clientes(models.Model):
     _name = 'upoelectro.clientes'
     _description = 'Upoelectro clientes'

     name = fields.Char('Usuario',required=True,help="Usuario Cuenta")
     password = fields.Char("Password",required=True,help="Password Cuenta")
     foto=fields.Binary('Foto')
     nombre = fields.Char(string="Nombre", size=60, required=True, help="Nombre Cliente")
     apellidos = fields.Char(string="Apellidos", size=60, required=True, help="Apellidos Cliente")
     dni = fields.Char(string='DNI', size=9, required=True ,help="DNI Cliente")
     direccion = fields.Char(string='Direccion', size=60 ,required=True, help="Direccion Cliente")
     telefono= fields.Char (string='Telefono',size=9,required=True, help='Telefono cliente')
     correo = fields.Char(string="Correo", size=60, required=True, help="Correo Cliente")

     pedidos_ids = fields.One2many('upoelectro.pedidos','cliente_id',string="Pedidos asociados")