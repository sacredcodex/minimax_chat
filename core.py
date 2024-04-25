import requests
import json
import time
from datetime import datetime

class Core:
    def __init__(self, model_file_name = 'chat1.json'):
        if not model_file_name.endswith('.json'):
            model_file_name += '.json'
        with open('user.json', 'r') as file:
            user = json.load(file)
        self.user_name = user['name']
        self.url = "https://api.minimax.chat/v1/text/chatcompletion_pro?GroupId=" + user['group_id']
        self.headers = {"Content-Type": "application/json", "Authorization": "Bearer " + user['api_key']}

        with open(model_file_name, 'r') as file:
            model = json.load(file)
        self.models = ["abab6-chat", "abab5.5-chat", "abab5.5s-chat"]
        self.model_name = model['name']
        self.description = model['description']
        self.model_type = model["model_type"]
        self.tokens_to_generate = model['tokens_to_generate']
        self.temperature = model['temperature']
        self.top_p = model['top_p']
        if self.model_type not in self.models:
            print("Wrong model name")
            exit()
        self.res = None


    def send(self, message_content, new_conversation = False):
        if new_conversation:
            self.payload = {
                "bot_setting": [
                    {
                        "bot_name": self.model_name,
                        "content": self.description,
                    }
                ],
                "messages": [{"sender_type": "USER", "sender_name": self.user_name, "text": message_content}],
                "reply_constraints": {"sender_type": "BOT", "sender_name": self.model_name},
                "model": self.model_type,
                "tokens_to_generate": self.tokens_to_generate,
                "temperature": self.temperature,
                "top_p": self.top_p,
            }
            created_time = time.time()
            created_time = int(created_time)

            self.dialog_file = f'd{created_time}.txt'

        else:
            self.payload["messages"].append({"sender_type": "USER", "sender_name": self.user_name, "text": message_content})

        self.save(message_content, self.user_name)
        response = requests.request("POST", self.url, headers=self.headers, json=self.payload)
        res = json.loads(response.text)
        self.res = res
        #保存
        created_time = res['created']
        with open(f"{created_time}.json", "w", encoding="utf-8") as fp:
            json.dump(res, fp, ensure_ascii=False, indent=4)

        reply_message = res['choices'][0]['messages'][0]
        self.payload['messages'].append(reply_message)

        reply_content = reply_message['text']
        print(reply_content)
        self.save(reply_content, self.model_name)

    def save(self, message_content, name):
        with open(self.dialog_file, 'a') as f:
            print(name, ":", message_content, file = f)
            print('\n', file = f)

    def record_cost(self):
        if self.res is None:
            return
        cur_price = price(self.model_type)
        tokens = self.res["usage"]["total_tokens"]
        with open('消费记录.txt', 'a') as file:
            print(datetime.fromtimestamp(self.res['created']), cur_price, tokens, cur_price * tokens / 1000, file=file)

def price(model):
    if model == "abab6-chat":
        return 0.1
    elif model == "abab5.5-chat":
        return 0.015
    elif model == "abab5.5s-chat":
        return 0.005

if __name__ == '__main__':
    core = Core('知识查询助手')
    content = 'help'
    new_conversation = True
    while True:
        if content == 'help' or content == 'h':
            print('help/h   查看帮助')
            print('quit/q   退出')
            print('new/n    开始新对话')
            print('请输入对话内容')
        elif content == 'new' or content == 'n':
            core.record_cost()
            new_conversation = True
        elif content == 'quit' or content == 'q':
            core.record_cost()
            exit()
        elif content.isspace():
            continue
        else:
            core.send(content, new_conversation)
            new_conversation = False
        content = input()

