from model.user import User
from model.comments import Comments


class Post:
    def __init__(self,body: str, author: User, comment: Comments):
        self.body = body
        self.author = author
        self.comment = comment
