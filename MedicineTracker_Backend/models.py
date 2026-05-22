class User(UserMixin, db.Model):
    __tablename__ = 'users'
    
class Category(db.Model):
    __tablename__ = 'categories'

class FamilyMember(db.Model):
    __tablename__ = 'familymembers'
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

class Medicine(db.Model):
    __tablename__ = 'medicines'
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    member_id = db.Column(db.Integer, db.ForeignKey('familymembers.member_id'))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.category_id'))

class Alert(db.Model):
    __tablename__ = 'alerts'
    medicine_id = db.Column(db.Integer, db.ForeignKey('medicines.medicine_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))