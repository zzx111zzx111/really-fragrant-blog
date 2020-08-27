from blog.models import Blog


class BlogCls:
    def __init__(self,sentence,account=None):
        self.account=account
        self.sentence=sentence
    def add_blog(self):
        blog=Blog()
        blog.sentence = self.sentence
        from datetime import datetime
        blog.publication_date = datetime.now()
        blog.account_id=self.account.id
        return blog
    def modify_blog(self):
        pass
    def delete_blog(self):
        pass