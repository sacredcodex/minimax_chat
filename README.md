# minimax_chat
调用minimax的api的问答应用
链接：https://www.minimaxi.com/platform

## 功能
解决了minimax网页无法保存对话内容的问题。
并制作了一个消费记录文档。

## 使用
**新**：
可以从下面链接下载zip文件，解压运行，不再需要安装python

https://github.com/sacredcodex/minimax_chat/releases/tag/minimax_chat

<del> 需要安装python，用到的包应该都是内置的，如果运行缺少包报错，可以尝试：
```
pip install json
pip install requests
pip install time
pip install datetime
```

</del>
首次使用
1. 创建user信息
   运行user.py,按照提示输入信息，运行结束会生成一个user.json文件，文件包括个人账户信息，请注意妥善保管，避免泄露给他人
2. 创建模型参数信息
  运行model.py,按照提示输入信息

后续使用

3. 运行core.py, 开始对话。

使用建议：

为core.py创建快捷方式，因为多有对话内容会保存在core所在文件夹，长期使用会导致文件夹内有大量json文件

文件说明：

以d开头的txt文件是对话文件，以长串数字命名的json文件是每次minimax回复的内容，其余json文件为用户和模型设置文件

