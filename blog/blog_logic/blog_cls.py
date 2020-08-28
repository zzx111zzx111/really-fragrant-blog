from blog.models import Blog


class BlogCls:
    def __init__(self, sentence=None, account=None, blog_id=None):
        self.account = account
        self.sentence = sentence
        self.blog_id = blog_id

    def add_blog(self):
        blog = Blog()
        blog.sentence = self.sentence
        from datetime import datetime
        blog.publication_date = datetime.now()
        blog.account_id = self.account.id
        return blog

    def query_blog_by_id(self):
        blog = Blog.query.get(self.blog_id)
        return blog
