export SECRET_KEY='c5c321bb470b4b11b98346a4f7223005'
export SQLALCHEMY_DATABASE_URI='sqlite:///site.db'
export PAYMENT_KEY='50d634f7ff85cd7ad324d4998dda3151'

export MAIL_USERNAME='sam263708@gmail.com'
export MAIL_PASSWORD='hpyxoozfawqcyjnt'


blue=$(tput setaf 004);
orange=$(tput setaf 166);
white=$(tput setaf 007);
red=$(tput setaf 001);
reset=$(tput setaf sgr0);
green=$(tput setaf 002)
bold=$(tput bold);


PS1="\[${bold}\]\n"
PS1+="\[${blue}\]samsung@";
PS1+="\[${red}\]magesaJR";
PS1+="\[${orange}\]@CODELAB\[${blue}\]";
PS1+="\[${green}\]in/\w";
PS1+="\n";
PS1+="\[${white}\]\$ \[${reset}\]";
export PS1;




export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

. "$HOME/.cargo/env"

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
