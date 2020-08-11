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
    U = CharField(max_length=32)
    MoveTime = CharField(max_length=32)


class MetaState(BaseModel):
    key = CharField(max_length=32, unique=True)
    value = CharField(max_length=32)


def initialize():
    with database:
        database.create_tables([BoardState, MetaState])


def BoardState_data():
    ret = []
    for i in BoardState.select():
        ret.append({"board_state": {"MoveId": i.id, "KW": i.KW, "QW": i.QW, "R1W": i.R1W, "N1W": i.N1W, "B1W": i.B1W, "R2W": i.R2W, "N2W": i.N2W, "B2W": i.B2W, "P1W": i.P1W, "P2W": i.P2W, "P3W": i.P3W, "P4W": i.P4W, "P5W": i.P5W, "P6W": i.P6W, "P7W": i.P7W, "P8W": i.P8W, "KB": i.KB, "QB": i.QB, "R1B": i.R1B, "N1B": i.N1B, "B1B": i.B1B, "R2B": i.R2B, "N2B": i.N2B, "B2B": i.B2B, "P1B": i.P1B, "P2B": i.P2B, "P3B": i.P3B, "P4B": i.P4B, "P5B": i.P5B, "P6B": i.P6B, "P7B": i.P7B, "P8B": i.P8B, "U": i.U, "MoveTime": i.MoveTime}, "meta_state": MetaState_data()})
    return ret


def MetaState_data():
    ms = {}
    for i in MetaState.select():
        ms[i.key] = i.value
    return ms


def get_MetaState_value_by_key(k):
    try:
        ret = MetaState.get(MetaState.key == k)
    except DoesNotExist:
        ret = None
    return ret


def update_or_create_MetaState_kv(k, v):
    if get_MetaState_value_by_key(k) != None:
        MetaState.update(value = v).where(MetaState.key == k)
    else:
        MetaState.create(key = k, value = v)


def BoardState_populate_from_single_dict(d):
    obj = BoardState.create(**d)
    update_or_create_MetaState_kv("turn_number", str(obj.id))


def BoardState_clear():
    a = BoardState.delete()
    a.execute()
