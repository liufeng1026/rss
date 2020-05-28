#!/bin/bash
#Author:perez
cd /home/
rm -rf wx_v1.0.zip
wget -c https://github.com/liufeng1026/rss/releases/download/v1.0/wx_v1.0.zip
apt install unzip
unzip -o wx_v1.0.zip -d wxarticle/
apt install python-pip
pip install --upgrade pip
pip install APScheduler==3.6.3
pip install PyMySQL==0.9.3
pip install SQLAlchemy==1.3.17
pip install wechatsogou==4.5.4
cd wxarticle/
nohup python -u entry.py > wxarticel.log 2>&1 &
#curl -O https://raw.githubusercontent.com/liufeng1026/rss/master/wx.sh && chmod +x wx.sh && ./wx.sh