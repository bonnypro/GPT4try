# GPT4try
一个基于gradio 的简易对话webui 界面，目前只支持 https://github.com/ymcui/Chinese-LLaMA-Alpaca 项目的中文Alpaca大模型。

安装方式：
```
pip install -r requirements.txt
```

pip下载慢的同学可以换成清华源
```
python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip
```
```
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

模型下载到model文件夹内，文件夹内容应如下所示
```
-a----         2023/4/24     18:53            610 config.json
-a----         2023/4/24     18:53            139 generation_config.json
-a----         2023/4/24     18:53     9943340890 pytorch_model-00001-of-00002.bin
-a----         2023/4/24     18:53     3827767515 pytorch_model-00002-of-00002.bin
-a----         2023/4/24     18:53          27118 pytorch_model.bin.index.json
-a----         2023/4/24     18:52            102 special_tokens_map.json
-a----         2023/4/24     18:52         757972 tokenizer.model
-a----         2023/4/24     18:52            760 tokenizer_config.json
```


启动方式
```
python main.py
```
然后复制地址 “http://127.0.0.1:7860/” 到浏览器访问

需要模型的同学，或者不知道如何转换模型的可以在discuss区留言。
