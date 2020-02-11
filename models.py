from app import db

### Init class Book ###
class Book(db.Model):
    ### Name table ###
    __tablename__ = 'books'

    ### Define colums in db ###
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String())
    author = db.Column(db.String())
    published = db.Column(db.String())

    ### Initialize variables ###
    def __init__(self, name, author, published):
        self.name = name
        self.author = author
        self.published = published
        
    def __repr__(self):
        return '<id {}'.format(self.id)

    ### Method to help return JSON ###
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'author': self.author,
            'published': self.published
        }
