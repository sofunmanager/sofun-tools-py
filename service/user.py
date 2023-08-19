from flask import Blueprint,current_app

from utils.jsonResult import JsonResult
from utils.jwtUtils import TokenUtils
from service.serviceUtils import ServerTool
from utils.file_w_r_Utils import INI_Tools


user_routes = Blueprint('user', __name__)



# svn_url = 'https://www.cdgqinfo.com/svn/cdsjcy_wps'

#登录
@user_routes.route('/user/login', methods=['GET', 'POST'])
def login():
    try:
        username=ServerTool.get_param("username")
        password=ServerTool.get_param("password")
        if(username and password):


            #登录信息验证逻辑...


            
            token=TokenUtils.create_token({'username':username,'password':password})

            return JsonResult.success(token)
        else:
            return JsonResult.fail(message="账号或密码不能为空！")
    except Exception as e:
        return ServerTool.onException(e)


#测试（返回token信息）
@user_routes.route('/user/test')
def test():
    return JsonResult.success(current_app.config["CURR_USER"])