import json


def create_model(name="知识查询助手",type="abab5.5s-chat", ttg=256, temp=0.01, topp=0.95):
    model = {
        'name' : name,
        'description' : f"{name}是一款由MiniMax自研的，没有调用其他产品的接口的大型语言模型。MiniMax是一家中国科技公司，一直致力于进行大模型相关的研究。",
        'model_type' : type,
        'tokens_to_generate' : int(ttg),
        'temperature' : float(temp),
        'top_p' : float(topp)
    }
    print(model)
    with open(f'{name}.json', 'w+') as file:
        json.dump(model, file, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    name = input("模型名字(文件名\称呼)：")
    type = input("模型类型(abab6-chat, abab5.5-chat, abab5.5s-chat, 以上3选1):")
    ttg = input("模型生成上限:")
    temp = input("temperature(0~1,越高创造性越强，越低准确性越强):")
    topp = input("top_p(越大越随机):")
    create_model(name, type, ttg, temp, topp)
