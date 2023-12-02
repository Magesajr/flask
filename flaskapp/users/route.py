from flaskapp import db,mail
from flask import current_app
from  flaskapp.models import User,Post
from flask import (
render_template,
redirect,flash,
url_for,request,
abort,Blueprint)
from .forms import (RegistrationForm
,LoginForm,
UpdateForm,
RequestPass,
ResetPass)
from flask_login import (login_user,
current_user
,logout_user,
login_required)
from flask_mail import Message
from flaskapp.users.utils import save_picture,send_reset_email


users=Blueprint('users',__name__)

@users.route('/register',methods=["GET","POST"])
def register():
  if current_user.is_authenticated:
    return redirect(url_for('main.HOME'))
  form=RegistrationForm()
  if form.validate_on_submit():
    name=form.name.data
    email=form.email.data
    password=form.password.data
    user=User(name=name,email=email,password=password)
    db.session.add(user)
    db.session.commit()
    #with app.app_context():
    flash(f'You have successfully Create an account for { form.name.data}!🥰🤗','success')
    return redirect(url_for('users.login'))
  return render_template('register.html',title='register',form=form)
  
@users.route('/login',methods='GET POST'.split())
def login():
  if current_user.is_authenticated:
    return redirect(url_for('main.HOME'))
  form=LoginForm()
  if form.validate_on_submit():
    email=form.email.data
    password=form.password.data
    user=User.query.filter_by(email=email).first()
    paskey=user.password
    if user and paskey==password:
      login_user(user,remember=form.remember_Me.data)
      next_page=request.args.get('next')
      return redirect(next_page) if next_page else redirect(url_for('main.HOME'))
    else:
      flash(f'Login unsuccessfull Please check email and password!😔','danger')
  return render_template('login.html',title='login',form=form)
  
  #payments=payments)


@users.route('/logout')
def logout():
  logout_user()
  return redirect(url_for('main.HOME'))
  
@users.route('/account',methods=['GET','POST'])
@login_required
def account():
  form = UpdateForm()
  if form.validate_on_submit():
    if form.picture.data:
      picture_file=save_picture(form.picture.data)
      current_user.image_file=picture_file
    current_user.name=form.name.data
    current_user.email=form.email.data
    db.session.commit()
    flash(f'You account have been Updated {form.name.data}!😇😊','success')
    return redirect(url_for('users.account'))
  elif request.method== 'GET':
    form.name.data=current_user.name
    form.email.data=current_user.email
  image_file=url_for('static',filename='profile_pics/' + current_user.image_file)
  return render_template('account.html',title='Account',image_file=image_file,form=form)
  
@users.route('/user/<string:name>')
def user_posts(name):
  page=request.args.get('page',1,type=int)
  user=User.query.filter_by(name=name).first_or_404()
  posts=Post.query.filter_by(Author=user)\
  .order_by(Post.date.desc())\
  .paginate(page=page,per_page=2)
  return render_template('user.html',posts=posts,user=user)
  

@users.route('/requestPass',methods=['GET','POST'])
def request_pass():
  if current_user.is_authenticated:
    return redirect(url_for('users.login'))
  form=RequestPass()
  if form.validate_on_submit():
    user=User.query.filter_by(email=form.email.data).first()
    send_reset_email(user)
    flash(f'an email has been sent with an instruction to reset your password','info')
    return redirect(url_for('users.login'))
  return render_template('request.html',title='request',form=form)
  

@users.route('/resetPass/<token>',methods=['GET','POST'])
def reset_pass(token):
  if current_user.is_authenticated:
    return redirect(url_for('users.login'))
  user=User.verify_reset_token(token)
  if user is None:
    flash('User doesnot exist or token is expired','warning')
    return redirect(url_for('users.request_pass'))
  form=ResetPass()
  if form.validate_on_submit():
    password=form.password.data
    new_pass=User(password=password)
    db.session.add(new_pass)
    db.session.commit()
    flash(f'Your password has been reset🤗🤗','success')
    return redirect(url_for('users.login'))
  return render_template('reset.html',title='reset',form=form)