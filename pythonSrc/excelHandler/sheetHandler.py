# -*-coding:utf-8-*-
from utils import *


class SheetHandler():
    def show_sheet_names(sheets):
        for item in sheets:
            print(gbk2utf(item, 1))


