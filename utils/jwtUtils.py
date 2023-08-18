import jwt
import datetime

class TokenUtils:
    
    # 密钥
    secret_key = "your_secret_key"
    expiration_minutes=60*24*30 #30天过期

    @classmethod
    def create_token(cls, payload):
        # 设置token的有效期
        expiration = datetime.datetime.utcnow() + datetime.timedelta(minutes=TokenUtils.expiration_minutes)
        # 添加过期时间到payload中
        payload['exp'] = expiration
        # 生成token
        token = jwt.encode(payload, cls.secret_key, algorithm='HS256')
        return token

    @classmethod
    def verify_token(cls, token):
        try:
            # 验证token
            payload = jwt.decode(token, cls.secret_key, algorithms=['HS256'])
            return payload
        except jwt.ExpiredSignatureError:
            # token过期
            return None
        except jwt.InvalidTokenError:
            # token无效
            return None

    @classmethod
    def set_expiration(cls, payload, expiration_minutes):
        # 设置token的有效期
        expiration = datetime.datetime.utcnow() + datetime.timedelta(minutes=expiration_minutes)
        # 更新payload中的过期时间
        payload['exp'] = expiration

    @classmethod
    def parse_token(cls, token):
        try:
            # 解析token，不验证有效性
            payload = jwt.decode(token, cls.secret_key, algorithms=['HS256'], options={'verify_exp': False})
            return payload
        except jwt.InvalidTokenError:
            # token无效
            return None
        


##示例
# 创建token，有效期为60分钟
# token = TokenUtils.create_token({'user_id': 123}, expiration_minutes=60)
# print("Token:", token)

# 校验token
# verified_payload = TokenUtils.verify_token(token)
# if verified_payload:
#     print("校验成功")
#     print("Payload:", verified_payload)
# else:
#     print("校验失败")

# 设置token的有效期为30分钟
# TokenUtils.set_expiration(payload, expiration_minutes=30)
# new_token = TokenUtils.create_token(payload)
# print("New Token:", new_token)

# # 解析token
# parsed_payload = TokenUtils.parse_token(token)
# if parsed_payload:
#     print("解析成功")
#     print("Payload:", parsed_payload)
# else:
#     print("解析失败")