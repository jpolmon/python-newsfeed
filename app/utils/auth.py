from flask import session, redirect
from functools import wraps

def login_required(func):
  @wraps(func)
  def wrapped_function(*args, **kwargs):
    # only calls the original function if the user is logged in
    if session.get('loggedIn') == True:
      return func(*args, **kwargs)
    
    return redirect('/login')
  
  return wrapped_function