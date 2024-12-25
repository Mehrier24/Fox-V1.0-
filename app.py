from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
import pyotp
from forms import RegistrationForm
from models import User  # Import your User (or other models) explicitly

app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:semo1234@localhost/library_db'
app.config['SECRET_KEY'] = 'maximum'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Models



from models import User, Book


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.cli.command('init-db')
def init_db():
    with app.app_context():
        print("Attempting database table creation…")
        db.create_all()
        print("Database tables created:", db.engine.table_names())




@app.route("/")
def home():
    return render_template("home.html")


# Registration Route
@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        phone = form.phone.data
        password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        new_user = User(username=username, email=email, phone=phone, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash("Registration successful! Please login.", "success")
        return redirect(url_for("login"))
    return render_template("register.html", form=form)



# Login Route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()

        if user and bcrypt.check_password_hash(user.password, password):
            otp = pyotp.TOTP(user.otp_secret).now()
            print(f"OTP for {user.email}: {otp}")  # Debugging, for production use proper OTP sending
            login_user(user)
            flash(f"An OTP has been sent for validation.", "info")
            return redirect(url_for("verify_otp"))
        else:
            flash("Invalid email or password.", "danger")
    return render_template("login.html")


# OTP Verification Route
@app.route("/verify_otp", methods=["GET", "POST"])
@login_required
def verify_otp():
    if request.method == "POST":
        entered_otp = request.form.get("otp")
        if pyotp.TOTP(current_user.otp_secret).verify(entered_otp):
            flash("Login successful!", "success")
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid OTP, please try again.", "danger")
    return render_template("verify_otp.html")


# User Dashboard
@app.route("/dashboard", methods=["GET"])
@login_required
def dashboard():
    borrowed_books = Book.query.filter_by(borrower_id=current_user.id).all()
    return render_template("dashboard.html", books=borrowed_books)


# Catalog for Books
@app.route("/catalog", methods=["GET", "POST"])
@login_required
def catalog():
    books = Book.query.filter_by(is_available=True).all()
    if request.method == "POST":
        book_id = request.form.get("book_id")
        book = Book.query.get_or_404(book_id)
        book.is_available = False
        book.borrower_id = current_user.id
        book.due_date = "7 days from now"  # Placeholder for due date logic
        book.pickup_location = "Library Front Desk"  # Placeholder for pickup location
        db.session.commit()
        flash("Book successfully checked out!", "success")
        return redirect(url_for("dashboard"))
    return render_template("catalog.html", books=books)


# Admin Login
@app.route("/admin", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        admin_key = request.form.get("admin_key")
        if admin_key == "admin-secret-key":  # Replace this
            flash("Welcome, Admin!", "success")
            return redirect(url_for("admin_dashboard"))
        else:
            flash("Invalid admin key!", "danger")
    return render_template("admin_login.html")


# Admin Dashboard
@app.route("/admin_dashboard", methods=["GET", "POST"])
def admin_dashboard():
    books = Book.query.all()
    return render_template("admin_dashboard.html", books=books)


# Admin - Add Books
@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        title = request.form.get("title")
        author = request.form.get("author")
        new_book = Book(title=title, author=author)
        db.session.add(new_book)
        db.session.commit()
        flash("Book added successfully!", "success")
        return redirect(url_for("admin_dashboard"))
    return render_template("book_entry.html")
