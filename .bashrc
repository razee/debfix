
if [ -f `which fortune` ] && [ -f `which cowsay` ]; then
  fortune | cowsay
fi

if [ -f /etc/bash_completion ]; then
  . /etc/bash_completion
fi

PATH=$HOME/.local/bin:$PATH

# nicely colored prompt
if [[ ${EUID} == 0 ]] ; then
  PS1="${debian_chroot:+($debian_chroot)}\[\e[01;31;40m\]█▊▋▌▍▎▏\[\e[34m\][\[\e[31m\]\t\[\e[34m\]]\[\e[33m\]:\[\e[0;38;40m\]\w \[\e[01;31m\]#\[\e[00m\] "
else
  PS1="${debian_chroot:+($debian_chroot)}\[\e[01;33;40m\]█▊▋▌▍▎▏\[\e[34m\][\[\e[31m\]\t\[\e[34m\]]\[\e[33m\]:\[\e[0;38;40m\]\w \[\e[01;33m\]\$\[\e[00m\] "
fi

alias whois='whois -H'
alias more='less -R'
alias ls='ls --color=always -F'
alias la='ls -AlF'
alias ll='ls -lF'
alias grep='grep --color=always'
alias b64='base64'
alias b64d='base64 -d'

export PAGER=less
export LESS=-R
