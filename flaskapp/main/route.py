from flask import render_template,request,Blueprint,send_from_directory,redirect
from flaskapp.models import Post
from .forms import DownloadForm

main=Blueprint('main',__name__)

@main.route('/')
def HOME():
  page=request.args.get('page',1,type=int)
  posts=Post.query.order_by(Post.date.desc()) .paginate(page=page,per_page=5)
  return render_template('home.html',posts=posts)

@main.route('/about')
def about():
  return render_template('about.html',title='About')
  
@main.route('/download')
def download():
  folder='flaskapp/main'
  form=DownloadForm()
  file=form.file.data
  if form.validate_on_submit():
    try:
      send_from_directory(folder,file,as_attachment=True)
    except FileNotFounderror:
      flash('file not exixts','danger')
      return redirect(url_for('.HOME'))
  return render_template('download.html',title='download')
  
