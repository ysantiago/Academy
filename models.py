# -*- coding: utf-8 -*-
from openerp import models, fields, api

class Teachers(models.Model):
	_name = 'academy.teachers'

	name = fields.Char()
	biography = fields.Html()

	# course_ids = fields.One2many('academy.courses', 'teacher_id', string="Courses")
	# Esto es una prueba
	course_ids = fields.One2many('product.template', 'teacher_id', string="Courses")

class Courses(models.Model):
	# _name = 'academy.courses'
	# _inherit = 'mail.thread'
	_inherit = 'product.template'

	name = fields.Char()
	teacher_id = fields.Many2one('academy.teachers', string="Teacher")

