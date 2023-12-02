from flask import  Blueprint,render_template,flash,redirect,url_for
from .forms import PaymentForm

pays=Blueprint('pays',__name__)


@pays.route('/payment',methods=['GET','POST'])
def payment():
  form=PaymentForm()
  #if form.validate_on_submit():
    #flash(f'You have successfully paid this!🥰🤗','success')
  return redirect(url_for('pays.azampay'))
  #else:
      #flash(f'hello welcome to our Y4ca  payments,choose your payment method! 🥰😊 💰💸💶💵','success')
  #return render_template('pay/payment.html',title='payment',form=form) 
  
  
@pays.route('/azampay')
def azampay():
  form=PaymentForm()
  #if form.validate_on_submit():
    #flash(f'payment has been  done successful by  azampay','success')
  #else:
    #flash('welcome to azampay portal','success')
  return render_template('test/azampesa.html',title='azampay html',form=form)