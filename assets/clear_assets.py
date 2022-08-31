# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2022-08-31 14:46:18
# LastEditTime: 2022-08-31 14:56:11
# Description: 清理images文件夹中不必要的文件

from glob import glob
import os

if __name__ == '__main__':

    md_dir = '../_projects'
    mds = glob(f'{md_dir}/*.md')
    mds_str = ''
    for md in mds:
        with open(md,'r') as f:
            md_str = ' '.join(f.readlines())
        mds_str += md_str

    files_dir = 'images'
    files = glob(f'{files_dir}/*/*')
    
    for file_path in files:
        if file_path not in mds_str:
            os.remove(file_path)

        
    


