# TinyServer Installation

## 安装必须软件

```shell
sudo apt update
sudo apt install nginx
sudo apt install python3-pip

pip3 install flask
```

此部分中各种疑难杂症请自行解决

## 配置反向代理

对所有location进行反向代理

```shell
sudo gedit /etc/nginx/sites-available/default
```
如果你没有图形界面，请把`gedit`换用你会使用的文本编辑工具

```
location / {
    try_files $uri @proxy;
}

location @proxy {
    proxy_pass http://localhost:5000;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
}
```

```shell
sudo service nginx restart
```

## 启动服务

假定你在项目根目录下

```shell
python3 app.py
```

## 测试服务

* 本地 `http://localhost/`

* remote `http://<你的ip>/`
