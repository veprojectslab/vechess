import sys
import os
from peewee import *
from playhouse.db_url import connect

db_url = os.environ["VECHESS_DB_URL"]
database = connect(db_url)

class BaseModel(Model):
    class Meta:
        database = database

class BoardState(BaseModel):
    KW = CharField(max_length=32)
    QW = CharField(max_length=32)
    R1W = CharField(max_length=32)
    N1W = CharField(max_length=32)
    B1W = CharField(max_length=32)
    R2W = CharField(max_length=32)
    N2W = CharField(max_length=32)
    B2W = CharField(max_length=32)
    P1W = CharField(max_length=32)
    P2W = CharField(max_length=32)
    P3W = CharField(max_length=32)
    P4W = CharField(max_length=32)
    P5W = CharField(max_length=32)
    P6W = CharField(max_length=32)
    P7W = CharField(max_length=32)
    P8W = CharField(max_length=32)
    KB = CharField(max_length=32)
    QB = CharField(max_length=32)
    R1B = CharField(max_length=32)
    N1B = CharField(max_length=32)
    B1B = CharField(max_length=32)
    R2B = CharField(max_length=32)
    N2B = CharField(max_length=32)
    B2B = CharField(max_length=32)
    P1B = CharField(max_length=32)
    P2B = CharField(max_length=32)
    P3B = CharField(max_length=32)
    P4B = CharField(max_length=32)
    P5B = CharField(max_length=32)
    P6B = CharField(max_length=32)
    P7B = CharField(max_length=32)
    P8B = CharField(max_length=32)


def initialize():
    with database:
        database.create_tables([BoardState])


def BoardState_data():
    ret = []
    for i in BoardState.select():
        ret.append({"cmd": "", "id": i.id, "KW": i.KW, "QW": i.QW, "R1W": i.R1W, "N1W": i.N1W, "B1W": i.B1W, "R2W": i.R2W, "N2W": i.N2W, "B2W": i.B2W, "P1W": i.P1W, "P2W": i.P2W, "P3W": i.P3W, "P4W": i.P4W, "P5W": i.P5W, "P6W": i.P6W, "P7W": i.P7W, "P8W": i.P8W, "KB": i.KB, "QB": i.QB, "R1B": i.R1B, "N1B": i.N1B, "B1B": i.B1B, "R2B": i.R2B, "N2B": i.N2B, "B2B": i.B2B, "P1B": i.P1B, "P2B": i.P2B, "P3B": i.P3B, "P4B": i.P4B, "P5B": i.P5B, "P6B": i.P6B, "P7B": i.P7B, "P8B": i.P8B, })
    return ret


def BoardState_populate_from_single_dict(d):
    BoardState.create(KW=d["KW"], QW=d["QW"], R1W=d["R1W"], N1W=d["N1W"], B1W=d["B1W"], R2W=d["R2W"], N2W=d["N2W"], B2W=d["B2W"], P1W=d["P1W"], P2W=d["P2W"], P3W=d["P3W"], P4W=d["P4W"], P5W=d["P5W"], P6W=d["P6W"], P7W=d["P7W"], P8W=d["P8W"], KB=d["KB"], QB=d["QB"], R1B=d["R1B"], N1B=d["N1B"], B1B=d["B1B"], R2B=d["R2B"], N2B=d["N2B"], B2B=d["B2B"], P1B=d["P1B"], P2B=d["P2B"], P3B=d["P3B"], P4B=d["P4B"], P5B=d["P5B"], P6B=d["P6B"], P7B=d["P7B"], P8B=d["P8B"])

def BoardState_clear():
    a = BoardState.delete()
    a.execute()
