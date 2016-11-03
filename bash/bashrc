_set_aliases() {
    alias ll='ls -l'
    alias la='ls -a'
    alias lla='ls -al'
    alias cl='clear'
    alias \:q='exit'
}

_manpage_color() {
  export LESS_TERMCAP_mb=$'\E[01;31m'
  export LESS_TERMCAP_md=$'\E[01;31m'
  export LESS_TERMCAP_me=$'\E[0m'
  export LESS_TERMCAP_se=$'\E[0m'
  export LESS_TERMCAP_so=$'\E[01;44;33m'
  export LESS_TERMCAP_ue=$'\E[0m'
  export LESS_TERMCAP_us=$'\E[01;32m'
}

_set_prompt() {
    # Reset
    local Color_Off='\[\e[0m\]'       # Text Reset

    # Regular Colors
    local Black='\[\e[0;30m\]'        # Black
    local Red='\[\e[0;31m\]'          # Red
    local Green='\[\e[0;32m\]'        # Green
    local Yellow='\[\e[0;33m\]'       # Yellow
    local Blue='\[\e[0;34m\]'         # Blue
    local Purple='\[\e[0;35m\]'       # Purple
    local Cyan='\[\e[0;36m\]'         # Cyan
    local White='\[\e[0;37m\]'        # White

    : ${PROMPT_COLOR:=Yellow}
    : ${PROMPT_COLOR2:=Blue}
    local C1=${!PROMPT_COLOR}
    local C2=${!PROMPT_COLOR2}

    #local NEWLINE="\n"
    local LINE1="\342\224\214${White}(${Cyan}\w${White})"
    local LINE2="\342\224\224\342\224\200(${Yellow}\u${Purple}@${Yellow}\h${White})-> "
    export PS1="${NEWLINE}${LINE1} \$(git_branch)${NEWLINE}${LINE2}${Color_Off}"
}

git_branch() {
    [ -d .git ] || git rev-parse --git-dir 2> /dev/null || return
    local BRANCH=$(git branch --no-color 2>/dev/null | sed -e "/^[^*]/d" -e "s/* //")
    local ALLCHANGED=$(git status --porcelain 2>/dev/null | wc -l | tr -d ' ')
    echo "[${BRANCH}:${ALLCHANGED}]"
}

export VISUAL=vim
export EDITOR="$VISUAL"

_set_aliases
_manpage_color
_set_prompt
