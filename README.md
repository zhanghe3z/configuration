# myconfig
1. [my_nvim_config](https://github.com/zhanghe3z/nvim-config)
2. [tmux_config](https://github.com/zhanghe3z/config_in_server/blob/master/.tmux.conf)
3. [alacritty](https://github.com/zhanghe3z/-configuration-/blob/master/alacritty.yml)
4. [ranger](https://github.com/zhanghe3z/my-ranger-config)
5. git 代理 git config --global http.proxy socks5://localhost:1080  
6. terminal 代理 export https_proxy=http://127.0.0.1:8889 http_proxy=http://127.0.0.1:8889 all_
proxy=socks5://127.0.0.1:1089
7. Download Google Drive files  
>wget --no-check-certificate -r 'https://docs.google.com/uc?export=download&id=1eDjh-_bxKKnEuz5h-HXS7EDJn59clx6V' -O $(curl -s "https://drive.google.com/file/d/1eDjh-_bxKKnEuz5h-HXS7EDJn59clx6V/view?usp=sharing" | grep -o '<title>.*</title>' | cut -d'>' -f2 | awk -F ' - Goo' '{print $1}')
