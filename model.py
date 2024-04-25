import json



def create_model(name="知识查询助手",type="abab5.5s-chat", ttg=256, temp=0.01, topp=0.95):
    model = {
        'name' : name,
        'description' : f"{name}是一款由MiniMax自研的，没有调用其他产品的接口的大型语言模型。MiniMax是一家中国科技公司，一直致力于进行大模型相关的研究。",
        'model_type' : type,
        'tokens_to_generate' : ttg,
        'temperature' : temp,
        'top_p' : topp
    }
    print(model)
    with open(f'{name}.json', 'w+') as file:
        json.dump(model, file, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    create_model()