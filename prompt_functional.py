import json

def get_prompt_functions(prompts_path = r'./prompts.json', language = "cn"):
    ###################### 加载prompt ###########################
    function_plugins = {}
    with open(prompts_path, errors='ignore') as f:
        prompts = json.load(f)[language]
    for i in prompts:
        function_plugins[i[0]] = {
            "Prefix":  i[1],
            "Suffix":   r"",
            "Color":    r"secondary",    # 按钮颜色
            "Visible": False, # 不在固定按钮区域
        }
    
    return function_plugins
