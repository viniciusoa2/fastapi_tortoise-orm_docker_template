from tortoise import fields, models


class Parceiro(models.Model):
    cnpj = fields.CharField(max_length=100, unique=True)
    razao_social = fields.TextField()
    nome_fantasia = fields.TextField()
    telefone = fields.TextField()
    email = fields.TextField()
    cep = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
    cidade_estado = fields.ReverseRelation['ParceirosCidadeEstado']


class ParceiroCidadeEstado(models.Model):
    parceiro = fields.ForeignKeyField('models.Parceiros', related_name='CidadeEstado')
    cidade = fields.TextField()
    estado = fields.TextField()

