from flask import render_template,request,Blueprint,send_from_directory,redirect,flash,url_for,send_file
from flaskapp.models import Post
from .forms import DownloadForm
import os
import pandas as pd

main=Blueprint('main',__name__)

@main.route('/')
def HOME():
  page=request.args.get('page',1,type=int)
  posts=Post.query.order_by(Post.date.desc()) .paginate(page=page,per_page=5)
  return render_template('home.html',posts=posts)

@main.route('/about')
def about():
  return render_template('about.html',title='About')
  
@main.route('/download',methods=['GET','POST'])
def download():
  folder='flaskapp/main'
  form=DownloadForm()
  if form.validate_on_submit():
    file=form.file.data
    try:
      return send_from_directory('main',file,as_attachment=True)
    except FileNotFoundError:
      flash('file not exixts','danger')
      return redirect(url_for('HOME'))
  return render_template('download.html',title='download',form=form)
  
@main.route('/newfiles',methods=['GET','POST'])
def files():
  folder='flaskapp'
  df={'first':'samson','last':'magesa'}
  file=os.path.join(folder,'mamasam.csv')
  df=pd.DataFrame(df,index=[0,1])
  df.to_csv(file,index=True)
  flash('new file  created','info')
  return send_file(file,as_attachment=True)
