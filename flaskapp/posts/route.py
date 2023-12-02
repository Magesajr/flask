from  flaskapp.models import Post
from flaskapp import db
from flask import (render_template,
redirect,
flash,
url_for,
request,
abort,Blueprint)
from .forms import PostForm
from flask_login import (login_user,current_user,
login_required)

posts=Blueprint('posts',__name__)


@posts.route('/post/new',methods=['GET','POST'])
@login_required
def new_post(): 
  form = PostForm()
  if form.validate_on_submit():
    post=Post(title=form.title.data,content=form.content.data,Author=current_user)
    db.session.add(post)
    db.session.commit()
    flash(f' You have successfully Posted{current_user.name}😊🤗','success')
    return redirect(url_for('main.HOME'))
  return render_template('posts.html',title='Posts',form=form,legend='New Post')


@posts.route('/post/<int:post_id>')
def post(post_id):
  post=Post.query.get_or_404(post_id)
  return render_template('post.html',title=post.title,post=post)

@login_required  
@posts.route('/post/<int:post_id>/update',methods=['GET','POST'])
def post_update(post_id):
  post=Post.query.get_or_404(post_id)
  if post.Author != current_user:
    abort(403)
  form=PostForm()
  if form.validate_on_submit():
    post.title = form.title.data
    post.content = form.content.data
    db.session.commit()
    flash(f'Your Post have been Updated{current_user.name}🤗😊','success')
    return redirect(url_for('posts.post',post_id=post.id))
  elif request.method =='GET':
    form.title.data = post.title
    form.content.data = post.content
  return render_template('posts.html',title='Post_update',form=form,legend='Update Post')
  

@posts.route('/post/<int:post_id>/delete',methods=['POST'])
def delete_post(post_id):
  post=Post.query.get_or_404(post_id)
  if post.Author != current_user:
    abort(403)
  db.session.delete(post)
  db.session.commit()
  
  flash(f'Your Post has been deleted successfully{current_user.name}😇😇!','sucess')
  return redirect(url_for('main.HOME'))