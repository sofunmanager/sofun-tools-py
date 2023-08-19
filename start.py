import ctypes
import json
import logging
import os
import sys
import time
from flask import Flask, request, jsonify
from logging.handlers import RotatingFileHandler
from utils import svnUtils
from utils.jsonResult import JsonResult
from utils.jwtUtils import TokenUtils
from utils.file_w_r_Utils import INI_Tools
from service.user import user_routes

app = Flask(__name__)

# 注册路由(新增接口文件在此处注册)
app.register_blueprint(user_routes)

server_name="SOFUN工具盒子"



ctypes.windll.kernel32.SetConsoleTitleW(server_name)
# 配置日志处理器
formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
# formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s')

# 控制台日志处理器
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

# 文件日志处理器
_time=time.strftime("%Y%m%d_%H",time.localtime())
log_path = f"logs/{_time}"
os.makedirs(log_path, exist_ok=True)
file_handler = RotatingFileHandler(f'{log_path}/_flask_.log', maxBytes=1024 * 1024, backupCount=10,encoding='utf-8')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

# 添加日志处理器到根logger
root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)
root_logger.addHandler(console_handler)
root_logger.addHandler(file_handler)



#默认启动
host="0.0.0.0"
port=5228
is_debug=False

#加载配置文件
logging.info("加载配置文件...")
c_host=INI_Tools.get("SERVER_CONFIG","host")
if(c_host):
    host=c_host

c_port=INI_Tools.get("SERVER_CONFIG","port")
if(c_port):
    port=c_port

c_is_debug=INI_Tools.get("SERVER_CONFIG","is_debug")
if(c_is_debug):
    if(c_is_debug=="True"):
        is_debug=True
    else:
        is_debug=False


#启动参数处理
logging.info("加载启动参数...")
for i in range(1, len(sys.argv)):
    arg=sys.argv[i]
    a=arg.split("=")
    if(a[0]=="host"):
        logging.info(f"设置启动地址：{a[1]}")
        host=a[1]
        
    if(a[0]=="port"):
        logging.info(f"设置启动端口：{a[1]}")
        port=a[1]

if(host!="127.0.0.1" and host!="localhost" and host!="0.0.0.0"):
    logging.warning(f"当前启动地址为[{host}],该地址可能会导致服务无法访问！建议设置为[127.0.0.1]|[0.0.0.0]|[localhost]")













@app.before_request
def before_request():

     # 接口白名单
    excluded_endpoints = ['user.login']
    endpoint=request.endpoint
    if endpoint not in excluded_endpoints:
        token=request.headers.get("token")
        if(token):
            logging.info(f"header获取到token:{token}")
            jwt_str=TokenUtils.verify_token(token)
            if(jwt_str):
                logging.info(f"登录用户:{jwt_str['username']}")
                app.config['CURR_USER'] = {'username':jwt_str['username'],'password':jwt_str['password']}


            else:
                logging.info("身份校验未通过")
                return JsonResult.fail(message="身份校验未通过!",code=401)

        else:
            logging.info("没有获取到token")
            return JsonResult.fail(message="没有获取到token!",code=401)
    
    

@app.after_request
def after_request(response):
    response.headers["Content-Type"] = "application/json;charset=UTF-8"
    return response
    

if __name__ == '__main__':
    logging.info(f"启动{server_name}服务[DEBUG:{is_debug}]>>>")
    app.run(host,port,is_debug)
    