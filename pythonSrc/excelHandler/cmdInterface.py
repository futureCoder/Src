# -*-coding:utf-8-*-


def select_mode():
    operation = ['1:add', '2:remove', '3:modify', '4:find']
    target = ['1:Hero', '2:Rune']
    for item in operation:
        print(item)
    mode = input()
    for item in target:
        print(item)
    tar = input()
    print(mode, tar)
    # handle_user_input(mode, tar)
