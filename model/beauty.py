from odoo import models, fields
class Contact(models.Model):
    _name = 'custom.web.form.booking'
    name = fields.Char(string='Name')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    date = fields.Date(string='Date')