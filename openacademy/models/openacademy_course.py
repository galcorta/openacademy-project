# -*- coding: utf-8 -*-

from openerp import models, fields, api

'''
This module create module of Course
'''

class Course(models.Model):

    '''
    This class create module of course
    '''
    _name = 'openacademy.course'

    name = fields.Char(string="Title", required=True)
    description = fields.Text(string='Description')
