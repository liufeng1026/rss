#!/bin/bash
#Author:perez
apt install python-pip
pip install --upgrade pip
pip install APScheduler==3.6.3
pip install PyMySQL==0.9.3
pip install SQLAlchemy==1.3.17
pip install wechatsogou==4.5.4
nohup python -u entry.py > wxarticel.log 2>&1 &
#curl -O https://raw.githubusercontent.com/atrandys/trojan/master/trojan_mult.sh && chmod +x trojan_mult.sh && ./trojan_mult.sh