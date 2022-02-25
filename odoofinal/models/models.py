# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class odoofinal(models.Model):
#     _name = 'odoofinal.odoofinal'
#     _description = 'odoofinal.odoofinal'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
from odoo import models, fields, api
class restaurante(models.Model):
	_name = 'odoofinal.restaurante'
	_description = 'model restaurante'

	name = fields.Char('Id',required=True)
	nombre = fields.Char(string='Nombre',required=True)
	num_titulos_gastronomicos=fields.Integer(string='Titulos Gastronomicos',required=True)
	num_premios_al_diseno=fields.Integer(string='Titulos al Diseno',required=True)
	total_reconocimientos = fields.Integer("Total de premios", compute="_get_total")
	@api.depends('num_titulos_gastronomicos')
	def _get_total(self):
		for t in self:
			t.total_reconocimientos =  t.num_titulos_gastronomicos + t.num_premios_al_diseno
class encargado(models.Model):
	_name = 'odoofinal.encargado'
	_description = 'model encargado'

	name = fields.Char('Id',required=True)
	nombre = fields.Char(string='Nombre',required=True)
	empleados_ids = fields.One2many('odoofinal.empleado','empleado_id',string='Empleados')
class empleado(models.Model):
	_name = 'odoofinal.empleado'
	_description = 'model empleado'

	name = fields.Char('Id',required=True)
	nombre = fields.Char(string='Nombre',required=True)
	empleado_id=fields.Many2one('odoofinal.encargado',string='Encargado')
	mesas_ids = fields.One2many('odoofinal.mesa','mesa_id',string='Mesas')
class mesa(models.Model):
	_name = 'odoofinal.mesa'
	_description = 'model mesa'

	name = fields.Char('Id',required=True)
	zona = fields.Char(string='Zona',required=True)
	num_mesa=fields.Integer(string='Numero de mesa',required=True)
	mesa_id=fields.Many2one('odoofinal.empleado',string='Empleado')