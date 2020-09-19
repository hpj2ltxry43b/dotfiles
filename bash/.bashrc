# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# User specific environment
if ! [[ "$PATH" =~ "$HOME/.local/bin:$HOME/bin:" ]]
then
    PATH="$HOME/.local/bin:$HOME/bin:$PATH"
fi
export PATH

# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=

# User specific aliases and functions

export TERMINAL="alacritty"

eval $(dircolors -b ~/.dir_colors)

alias ls='ls --color'
alias ll='ls -l --color'
alias la='ls -a --color'
alias lla='ls -la --color'
alias md='mkdir'
alias rd='rmdir'

alias gsta='git status'
alias gcom='git commit'
alias gcoma='git commit -a'
alias gcomam='git commit -am'
alias gcomm='git commit -m'
alias gadd='git add'
alias gdif='git diff'
alias gdifs='git diff --staged'
alias gswi='git switch'
alias gps='git push'
alias gpl='git pull'
alias gf='git fetch'
alias gfp='git fetch && git pull'
alias gfpa='git fetch --all && git pull --all'

alias clmake='clear && cmake --build .'
alias tsmake='tsc' # much less awkward key combination
alias mypys='mypy --disallow-any-expr --disallow-any-explicit --disallow-any-decorated --disallow-untyped-calls --strict-optional --warn-no-return --warn-return-any --disallow-redefinition --disallow-untyped-globals --show-error-context --show-column-numbers --show-error-codes --pretty --error-summary --strict --show-error-context'

export CC=/usr/bin/clang
export CXX=/usr/bin/clang++
