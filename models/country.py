from app import db

class Country(db.Model):
    __tablename__ = "countries"

    id = db.Column(db.Integer, primary_key=True)
    country_name = db.Column(db.String(64))
    cities = db.relationship('City', backref ='country')
    def __repr__(self):
        return f"<Country {self.id}: {self.country_name}>"