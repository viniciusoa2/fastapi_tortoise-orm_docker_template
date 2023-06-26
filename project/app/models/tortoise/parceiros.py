from tortoise import fields, models


class Example(models.Model):
    created_at = fields.DatetimeField(auto_now_add=True)
