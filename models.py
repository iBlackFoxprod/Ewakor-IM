from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

db = SQLAlchemy()

# Update the product categories and types to match the main types shown in the images
PRODUCT_CATEGORIES = [
    ('drum', 'Fût'),
    ('jug', 'Bidon'),
    ('can', 'Jerrican'),
    ('bottle', 'Bouteille'),
    ('other', 'Autre'),
]

PRODUCT_TYPES = [
    ('oil', 'Huile'),
    ('grease', 'Graisse'),
    ('fluid', 'Fluide'),
    ('additive', 'Additif'),
    ('other', 'Autre'),
]

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(20), default='user')
    active = db.Column(db.Boolean, default=True)
    language = db.Column(db.String(2), default='en')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @property
    def is_active(self):
        return self.active

    @is_active.setter
    def is_active(self, value):
        self.active = value

class Product(db.Model):
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)  # e.g., "Lubrifiants", "Produits chimiques", "Outils"
    product_type = db.Column(db.String(50), nullable=False)  # e.g., "Spray", "Jerrican", "Carton"
    container_type = db.Column(db.String(50))  # Jerrican 20L, Jerrican 5L, Seau métallique 20L, Carton (4x5L), Spray
    packaging = db.Column(db.String(20), default='Unité')  # 'Unité' or 'En carton'
    quantity = db.Column(db.Integer, default=0)
    image_path = db.Column(db.String(200))
    min_stock_level = db.Column(db.Integer, default=10)
    unit = db.Column(db.String(20), default='pcs')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    stock_movements = db.relationship('StockMovement', backref='product', lazy=True)
    incoming_stock = db.relationship('IncomingStock', backref='product', lazy=True)

    @property
    def current_stock(self):
        return self.quantity

class Settings(db.Model):
    __tablename__ = 'settings'
    
    id = db.Column(db.Integer, primary_key=True)
    language = db.Column(db.String(2), default='en')
    logo_path = db.Column(db.String(200))

class StockMovement(db.Model):
    __tablename__ = 'stock_movement'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    movement_type = db.Column(db.String(20), nullable=False)  # 'in' or 'out'
    reference = db.Column(db.String(100))  # PO number, invoice number, etc.
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', backref='stock_movements')

class IncomingStock(db.Model):
    __tablename__ = 'incoming_stock'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    supplier = db.Column(db.String(100), nullable=False)
    expected_quantity = db.Column(db.Integer, nullable=False)
    expected_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(20), default='pending')  # pending, received, cancelled
    po_number = db.Column(db.String(50))
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', backref='incoming_stock')

class CompanySettings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    language = db.Column(db.String(10), default='en')  # 'en' or 'fr'
    logo_path = db.Column(db.String(255), default='static/default_logo.png')
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow) 