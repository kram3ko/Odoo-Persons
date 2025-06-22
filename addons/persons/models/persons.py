from odoo import models, fields, api
from datetime import date

class Person(models.Model):
    _name = 'my.person'
    _description = 'Person'

    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    full_name = fields.Char(compute='_compute_full_name', store=True)
    birthday = fields.Date()
    age = fields.Integer(compute='_compute_age', store=True)
    sex = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('non_binary', 'Non-binary')
    ])
    company_id = fields.Many2one(
        'res.company',
        required=True,
        default=lambda self: self.env.company
    )

    @api.depends('first_name', 'last_name')
    def _compute_full_name(self):
        for rec in self:
            rec.full_name = f"{rec.first_name} {rec.last_name}"

    @api.depends('birthday')
    def _compute_age(self):
        for rec in self:
            if rec.birthday:
                today = date.today()
                rec.age = today.year - rec.birthday.year - (
                    (today.month, today.day) < (rec.birthday.month, rec.birthday.day)
                )
            else:
                rec.age = 0
