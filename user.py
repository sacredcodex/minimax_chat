import json
import os

# 补充用户信息
if __name__ == '__main__':
    name = input("姓名(称呼，可以随意设置）：")
    group_id = input("group id(账户管理-账户信息-基本信息-groupID)：")
    api_key = input("api key(账户管理-接口密钥-创建新的密钥-复制)：")
    user = {
        'name': name,
        'group_id': group_id,
        'api_key': api_key}

    if not os.path.exists("user"):
       os.makedirs("user")

    with open('user\\user.json', 'w+') as file:
        json.dump(user, file, ensure_ascii=False, indent=4)
