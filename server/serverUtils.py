from flask import app, request
from utils.jsonResult import JsonResult

class ServerTool:

    @staticmethod
    def onException(e:Exception):
        app.logger.error(e)
        msg=""
        if(len(e.args)>0):
            msg=e.args[0]
        return JsonResult.fail(message=msg)

    @staticmethod
    def get_param(key):
        if request.method == 'GET':
            # 获取GET参数
            param_value = request.args.get(key)
        
        elif request.method == 'POST':
            print(request.form)
            if request.is_json:
                param_value = request.get_json().get(key)  
            else:
                param_value = request.form.get(key)
        
        return param_value






