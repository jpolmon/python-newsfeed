from flask import Blueprint, render_template, session, redirect
from app.models import Post
from app.db import get_db
from app.utils.auth import login_required

bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@bp.route('/')
@login_required
def dash():
  db = get_db()
  # getting all posts by the logged in user
  posts = (
    db.query(Post)
    .filter(Post.user_id == session.get('user_id'))
    .order_by(Post.created_at.desc())
    .all()
  )

  return render_template(
    'dashboard.html',
    posts = posts,
    loggedIn=session.get('loggedIn')
  )

@bp.route('/edit/<id>')
@login_required
def edit(id):
  db = get_db()
  # getting the single post to edit
  post = db.query(Post).filter(Post.id == id).one()

  return render_template(
    'edit-post.html',
    post = post,
    loggedIn=session.get('loggedIn')
  )