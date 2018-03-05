# -*-coding:utf-8-*-


pos2name = {'1': '1∫≈Œª', '2': '2∫≈Œª', '3': '3∫≈Œª'}

def gbk2utf(in_data, tag):
    if 1 == tag:
        return unicode(in_data, "utf-8").encode('gbk').decode('gbk')
    elif 0 == tag:
        return unicode(in_data, "utf-8").encode('gbk').decode('gbk').encode('utf8')