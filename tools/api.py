# API接口模块
from flask import Flask, g,request
from tools.db import RedisClient
import requests

__all__ = ['app']
app = Flask(__name__)

# 连接数据库
def get_conn():
    if not hasattr(g, 'redis'):
        g.redis = RedisClient()
    return g.redis

@app.route('/')
def index():
    return '<p>Welcome to User-Agent Proxy Pool System </p>' \
           '<p>/pc    获取PC类user agent    </p>' \
           '<p>/app   获取APP类user agent   </p>' \
           '<p>/all   存有的user-agent总数  </p>'

# 获取代理
@app.route('/pc', methods = ['get'])
def get_pc_proxy():
    conn = get_conn()
    agent = conn.get_pc_agent()
    if agent:
        return agent[0]
    else:
        return None

@app.route('/app', methods=['get'])
def get_app_proxy():
    conn = get_conn()
    agent = conn.get_app_agent()
    if agent:
        return agent[0]
    else:
        return None

# 获取总计
@app.route('/all', methods=['get'])
def get_all_proxy():
    conn = get_conn()
    return str(conn.get_all())