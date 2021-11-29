from flask import Blueprint, render_template
from werkzeug.utils import append_slash_redirect

bp = Blueprint('home', __name__, url_prefix='/')

@bp.route('/')
def index():
  return render_template('homepage.html')

@bp.route('/login')
def login():
  return render_template('login.html')

@bp.route('/posts/<id>')
def single(id):
  return render_template('single-post.html')