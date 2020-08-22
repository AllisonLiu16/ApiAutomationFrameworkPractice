# coding:utf-8


# 中英文字符转换表
translate_table = {ord(ch): ord(en) for ch, en in zip(
     u'” “ ，,。！？【】（）％＃＠＆１２３４５６７８９０',
     u'" " ,,.!?[]()%#@&1234567890')}


def cn_trans_en(value):
    try:
        value.translate(translate_table)
    except Exception:
        print(value)
    else:
        return value
