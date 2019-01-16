from app.models import Master
import datetime
from app import db


def get_rel_by_openid(openid):
    items = Master.query.filter_by(openid=openid).all()
    return items


def add_rel(openid, keyword, account='', mode=604):
    item = Master.query.filter_by(openid=openid).filter_by(keyword=keyword). \
        filter_by(account=account).first()
    if item is None:
        item.keyword = keyword
        item.account = account
        item.mode = mode

        item.createtime = datetime.datetime.now()
        item.modifytime = item.createtime

        db.session.add(item)
        db.session.commit()

        return True
    else:
        return False