# -*- coding: utf-8 -*-

from odoo import models, fields, api


class academia_app(models.Model):
    _name = 'academia_app.course'
    _description = 'academia_app.course'

    name = fields.Char(required=True, string="Name")
    course_code = fields.Char(required=True, string="Course Code")
    description = fields.Text()


