from odoo import models,fields

class Employee(models.Model):
    _name = "employee.task"
    _description = "Employee Task"

    name = fields.Char(string="name")
    department = fields.Many2one('department.task',related_to="task.department",string="department_id")
    email = fields.Char(string="email")
    User_Access = fields.Selection([('admin','Admin'),('manager','Manager')],string='User Access',default="manager")