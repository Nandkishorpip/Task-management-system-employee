from odoo import models,fields

class Department(models.Model):
    _name = "department.task"
    _description = "Department Task"

    name = fields.Char(string="name",required=True)
    manager= fields.Char(string="manager")
    Description = fields.Text(string="Description")
