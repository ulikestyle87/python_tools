# -*- coding: utf-8 -*-
# 开发人员   ：黎工
# 开发时间   ：2020/6/24  15:24 
# 文件名称   ：zip_files_test.PY
# 开发工具   ：PyCharm
import os
import zipfile
import datetime


def getYesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    return yesterday


def get_zip_file(input_path,result_lists):
    """
    对目录进行深度优先遍历
    :param input_path:  需要压缩的文件夹路径
    :param result:
    """
    files = os.listdir(input_path)
    # print(files)
    for file in files:
        if os.path.isdir(input_path + '/' + file):
            get_zip_file(input_path + '/' + file, result_lists)

        else:
            result_lists.append(input_path + '/' + file)
    # print(result_lists)
# get_zip_file(r'D:/python_analysis/five-items',[])


def zip_file_path(input_path, output_path, output_name):
    """
    # 压缩文件
    # :param input_path: 压缩的文件夹路径
    # :param output_path: 解压（输出）的路径
    # :param output_name: 压缩包名称
    """

    f = zipfile.ZipFile(output_path + '/' + output_name, 'w',zipfile.ZIP_DEFLATED)
    filelists = []
    get_zip_file(input_path, filelists)
    for file in filelists:
        f.write(file)
    # 调用了close方法才会保证完成压缩
    f.close()
    return output_path + r'/' + output_name


if __name__ == '__main__':
    catelog = str(getYesterday())
    input_path = 'D:/python_analysis/five-items'
    zip_file_path(input_path,'../zip_file','test_'+catelog+'.zip')

