# -*- coding: utf-8 -*-#

# Name:         db_manager.py
# Description:  
# Author:       Mark
# Date:         2019\8\14 0014 16:24
from flask_script import Manager

db_manager = Manager()


@db_manager.command
def init():
    print("迁移仓库创建完毕！")


@db_manager.command
def revision():
    print("迁移脚本生成成功！")


@db_manager.command
def upgrade():
    print("脚本映射到数据库成功！")
