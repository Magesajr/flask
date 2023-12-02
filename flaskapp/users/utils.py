import secrets,os
from PIL import Image
from flask import url_for,current_app
from flask_mail import Message
from flaskapp import mail



def save_picture(form_picture):
  random_hex=secrets.token_hex(8)
  _,f_ext=os.path.splitext(form_picture.filename)
  picture_fn=random_hex + f_ext
  picture_path=os.path.join(current_app.root_path,'static/profile_pics',picture_fn)
  
  image_size=(125,135)
  i=Image.open(form_picture)
  i.thumbnail(image_size)
  i.save(picture_path)
  #form_picture.save(picture_path)
  return picture_fn

def send_reset_email(user):
  token=user.get_reset_token()
  msg=Message('Passsword Reset Request',sender='sam263708@gmail.com',
     recipients=[user.email])
  msg.body=f'''To reset your password tap following link:{url_for('users.reset_pass',token=token,_external=True)}
  
  if you did not request please ignore this email and no change will be made
  '''
  mail.send(msg)
  return 'sent'