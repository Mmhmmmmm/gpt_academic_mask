from toolbox import HotReload  # HotReload 的意思是热更新，修改函数插件后，不需要重启程序，代码直接生效


def get_prompt_functions():
    ###################### 第一组插件 ###########################
    from crazy_functions.prompt函数 import prompt函数
    function_plugins = {
        "prompt_test": {
            "Prefix":   r"Below is a paragraph from an academic paper. Polish the writing to meet the academic style, " +
                        r"improve the spelling, grammar, clarity, concision and overall readability. When necessary, rewrite the whole sentence. " +
                        r"Furthermore, list all modification and explain the reasons to do so in markdown table." + "\n\n",
            # 后语
            "Suffix":   r"",
            "Color":    r"secondary",    # 按钮颜色
        },

    }
    return function_plugins
