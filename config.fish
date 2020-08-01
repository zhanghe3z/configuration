
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
eval /home/zhanghe/anaconda3/bin/conda "shell.fish" "hook" $argv | source
if test -f /home/zhanghe/.autojump/share/autojump/autojump.fish; . /home/zhanghe/.autojump/share/autojump/autojump.fish; end
export NVM_DIR="$HOME/.nvm"
if not functions -q fisher
    set -q XDG_CONFIG_HOME; or set XDG_CONFIG_HOME ~/.config
    curl https://git.io/fisher --create-dirs -sLo $XDG_CONFIG_HOME/fish/functions/fisher.fish
    fish -c fisher
end
function nvm
      bass source ~/.nvm/nvm.sh ';' nvm $argv
end

#<<< conda initialize <<<

