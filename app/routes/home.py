from flask import Blueprint, render_template
from werkzeug.utils import append_slash_redirect
from app.models import Post
from app.db import get_db

bp = Blueprint('home', __name__, url_prefix='/')

@bp.route('/')
def index():
  # getting all posts
  db = get_db()
  posts = db.query(Post).order_by(Post.created_at.desc()).all()

  return render_template(
    'homepage.html',
    posts=posts
  )

@bp.route('/login')
def login():
  return render_template('login.html')

@bp.route('/post/<id>')
def single(id):
  # getting a single post by its id
  db = get_db()
  post = db.query(Post).filter(Post.id == id).one()

  return render_template(
    'single-post.html',
    post=post
  )