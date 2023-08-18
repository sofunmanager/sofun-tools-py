import json
class JsonResult:
    

    @staticmethod
    def success(
        data:None = None,
        message:str|None = None,
        code:int=200,
        ):
        res={'success':True,'code':200,'message':'操作成功'}
        if(data):
            res['data']=data
        
        if(code):
            res['code']=code

        if(message):
            res['message']=message

        return json.dumps(res, ensure_ascii=False)
    
    @staticmethod
    def fail(
        message:str|None = None,
        data:None = None,
        code:int=0,
        ):
        res={'success':False,'code':0,'message':'操作失败'}
        if(data):
            res['data']=data
        
        if(code):
            res['code']=code

        if(message):
            res['message']=message

        return json.dumps(res, ensure_ascii=False)
