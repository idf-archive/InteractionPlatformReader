__author__ = 'Danyang'
from peewee import *
from settings import DATA_BASE


database = MySQLDatabase(DATA_BASE["db"], port = 3306, user=DATA_BASE["username"], password=DATA_BASE["password"])


class AbstractModel(Model):
    class Meta:
        database = database


class Stock(AbstractModel):
    stock_code = CharField(max_length=63, primary_key=True)
    company_name = CharField(max_length=63, null=True)
    stock_type = CharField(max_length=1, null=True)


    def __unicode__(self):
        return self.stock_code+" "+str(self.company_name)


class Speculator(AbstractModel):
    name = CharField(max_length=255, primary_key=True)
    is_guest = BooleanField(default=False)

    def __unicode__(self):
        return self.name

class Management(AbstractModel):
    office_name = CharField(max_length=255, primary_key=True)
    name = CharField(max_length=255)
    stock_code = ForeignKeyField(Stock)

    def __unicode__(self):
        return self.name

class Question(AbstractModel):
    id = IntegerField(primary_key=True)
    datetime = DateTimeField()
    content = TextField()

    q_is_close_comment = BooleanField(default=True)
    c_is_close_comment = BooleanField(default=True)
    q_is_close_appraise = BooleanField(default=True)
    c_is_close_appraise = BooleanField(default=True)

    is_canceled = BooleanField(default=False)
    score = IntegerField(default=-999)
    stock_code = ForeignKeyField(Stock)
    speculator_name = ForeignKeyField(Speculator)

    def __unicode__(self):
        return self.id


class Reply(AbstractModel):
    id = IntegerField(primary_key=True)
    datetime = DateTimeField()
    content = TextField()

    is_check = BooleanField(default=True)
    question_id = ForeignKeyField(Question)
    management = ForeignKeyField(Management)

    def __unicode__(self):
        return self.id

