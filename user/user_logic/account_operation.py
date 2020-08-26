from __init2__ import db
from user.models import Account


class AccountCls:
    def __init__(self,account_name,password=None):
        self.account_name=account_name
        self.password=password
    def account_register(self):
        account=Account()
        account.account_name=self.account_name
        account.password=self.password
        db.session.add(account)
        db.session.commit()
    def check_account_name(self):
        account=Account.query.filter_by(account_name=self.account_name).one()
        return account
    def detect_account_status(self):
        pass
