from toolbox import HotReload  # HotReload 的意思是热更新，修改函数插件后，不需要重启程序，代码直接生效


def get_mask_functions():
    ###################### 第一组插件 ###########################
    from crazy_functions.面具函数 import 面具函数
    all_mask = ['GitHub Copilot', '以文搜图', '文案写手', '机器学习', '后勤工作', '职业顾问', '英专写手', '语言检测器', '小红书写手', '简历写手', '心理医生', '创业点子王', '互联网写手', '心灵导师', '越狱模式 [Jailbreak]', 'Prompt Improvement', 'CAN', 'Expert']
    function_plugins = {}
    for i in all_mask:
        function_plugins[i] = {
            "Color": "stop",    # 按钮颜色
            "Function": HotReload(面具函数)
        }
    return function_plugins
