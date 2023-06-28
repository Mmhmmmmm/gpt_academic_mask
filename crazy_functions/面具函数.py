from toolbox import CatchException, update_ui
from .crazy_utils import request_gpt_model_in_new_thread_with_ui_alive
import datetime
import json 
import os
@CatchException
def 面具函数(txt, llm_kwargs, plugin_kwargs, chatbot, history, system_prompt, name = None):
    """
    txt             输入栏用户输入的文本，例如需要翻译的一段话，再例如一个包含了待处理文件的路径
    llm_kwargs      gpt模型参数，如温度和top_p等，一般原样传递下去就行
    plugin_kwargs   插件模型的参数，暂时没有用武之地
    chatbot         聊天显示框的句柄，用于显示给用户
    history         聊天历史，前情提要
    system_prompt   给gpt的静默提醒
    web_port        当前软件运行的端口号
    """
    with open(r'./mask.json', 'r') as f:
        masks = json.load(f)
    # print(masks[0].keys())
    for i in masks:
        if i['name'] == name:
            context = i['context']
            break
    history = []    # 清空历史，以免输入溢出
    
    sys_prompt = ""
    idx = 0 
    for i in context:
        if i['role'] == 'system':
            sys_prompt = sys_prompt +  i['content']
        elif i['role'] == 'user':
            if idx %2 == 0:
                history.append(i['content'])
                idx+=1
            else:
                history.append(r"")
                history.append(i['content'])
                idx+=2
        elif i['role'] == 'assistant':
            if idx %2 == 1:
                history.append(i['content'])
                idx+=1
            else:
                history.append(r"")
                history.append(i['content'])
                idx+=2
    print(history)
    if history != []:
        chatbot.append(history)
    print(chatbot)
    yield from update_ui(chatbot=chatbot, history=history) # 刷新界面 # 由于请求gpt需要一段时间，我们先及时地做一次界面更新
    print(history)
    gpt_say = yield from request_gpt_model_in_new_thread_with_ui_alive(
        inputs=txt, inputs_show_user=txt, 
        llm_kwargs=llm_kwargs, chatbot=chatbot, history=history, 
        sys_prompt=sys_prompt,
        retry_times_at_unknown_error = 1
    )
    chatbot[-1] = (txt, gpt_say)
    history.append(txt)
    history.append(gpt_say)
    print(chatbot, history)
    yield from update_ui(chatbot=chatbot, history=history) # 刷新界面 # 界面更新
