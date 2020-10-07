# myconfig
1. [my_nvim_config](https://github.com/zhanghe3z/nvim-config)
2. [tmux_config](https://github.com/zhanghe3z/config_in_server/blob/master/.tmux.conf)
3. [alacritty](https://github.com/zhanghe3z/-configuration-/blob/master/alacritty.yml)
4. [ranger](https://github.com/zhanghe3z/my-ranger-config)
5. git 代理 git config --global http.proxy socks5://localhost:1080  
6. terminal 代理 export https_proxy=http://127.0.0.1:8889 http_proxy=http://127.0.0.1:8889 all_
proxy=socks5://127.0.0.1:1089
7. [Download Google Drive files](https://gist.github.com/iamtekeste/3cdfd0366ebfd2c0d805)  
>wget wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1vOfxAMFJUalhZzydzJa1AluRhzG7ZxHS' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1vOfxAMFJUalhZzydzJa1AluRhzG7ZxHS" -O iosxrvk9.qcow2 && rm -rf /tmp/cookies.txt

8. ubuntu 16 中文乱码在zshrc下面加
>LANG=zh_CN.UTF-8
LANGUAGE=zh_CN:en_US:en
LC_CTYPE="zh_CN.UTF-8"
LC_NUMERIC=zh_CN.UTF-8
LC_TIME=zh_CN.UTF-8
LC_COLLATE="zh_CN.UTF-8"
LC_MONETARY=zh_CN.UTF-8
LC_MESSAGES="zh_CN.UTF-8"
LC_PAPER=zh_CN.UTF-8
LC_NAME=zh_CN.UTF-8
LC_ADDRESS=zh_CN.UTF-8
LC_TELEPHONE=zh_CN.UTF-8
LC_MEASUREMENT=zh_CN.UTF-8
LC_IDENTIFICATION=zh_CN.UTF-8
LC_ALL=

9. [i3 config ](https://github.com/zhanghe3z/configuration/blob/master/config)
