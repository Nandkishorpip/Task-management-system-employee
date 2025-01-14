from odoo import models,fields

class Task(models.Model):
    _name = "task.task"
    _description = "Task Management"

    Task_Name = fields.Char(string="Task_Name",required=True)
    Assigned_employee = fields.Many2one('employee.task',related_to="task.task",string="Assigned Employee")
    deadline = fields.Date(string="deadline")
    status = fields.Selection([('draft','Draft'),('in progress','In Progress'),('completed','Completed')],string="status",default='draft')
    Notes = fields.Text(string="Notes")