
[ `which fortune` ] && [ `which cowsay` ] && fortune | cowsay

# source bash_completion if not already
[ ! $BASH_COMPLETION_COMPAT_DIR ] &&
  ! shopt -oq posix &&
    [ -f /usr/share/bash-completion/bash_completion ] &&
      . /usr/share/bash-completion/bash_completion    ||
    [ -f /etc/bash_completion ] && . /etc/bash_completion

PATH=$HOME/.local/bin:$PATH

# nicely colored prompt
PS1="█▊▋▌▍▎▏\[\e[34m\][\[\e[31m\]\t\[\e[34m\]]\[\e[33m\]:\[\e[0;38;40m\]\w "
[ $EUID = 0 ] &&
  PS1="${debian_chroot:+($debian_chroot)}\[\e[01;31;40m\]${PS1}\[\e[01;31m\]#\[\e[00m\] " ||
  PS1="${debian_chroot:+($debian_chroot)}\[\e[01;33;40m\]${PS1}\[\e[01;33m\]\$\[\e[00m\] "

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
