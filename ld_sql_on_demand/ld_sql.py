# -*- coding: utf-8 -*-
from odoo import fields, models, api
from odoo.tools.safe_eval import safe_eval, test_python_expr
from odoo.exceptions import MissingError, ValidationError, AccessError
DEFAULT_PYTHON_CODE = """env.cr.execute()"""


class LdSql(models.Model):
    _name = "ld.on.demand.sql"
    _rec_name = "create_date"

    code = fields.Text(string='Python Code', groups='base.group_system',
                       default=DEFAULT_PYTHON_CODE,
                       help="Write Python code that the action will execute. Some variables are "
                            "available for use; help about python expression is given in the help tab.")

    @api.constrains('code')
    def _check_python_code(self):
        for action in self.sudo().filtered('code'):
            msg = test_python_expr(expr=action.code.strip(), mode="exec")
            if msg:
                raise ValidationError(msg)

    def run_py_code(self):
        cxt = dict(env=self.env)
        safe_eval(self.code.strip(), cxt, mode="exec", nocopy=True)
