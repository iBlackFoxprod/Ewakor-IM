from app import app, db
from models import User

def init_db():
    with app.app_context():
        # Create all tables
        db.create_all()
        
        # Check if admin user exists
        admin = User.query.filter_by(email='admin@ewakor.com').first()
        if not admin:
            admin = User(
                email='admin@ewakor.com',
                role='admin',
                name='System Administrator'
            )
            admin.set_password('admin123')
            db.session.add(admin)
            db.session.commit()
            print("Default admin user created!")
        else:
            print("Admin user already exists.")

if __name__ == '__main__':
    init_db() 