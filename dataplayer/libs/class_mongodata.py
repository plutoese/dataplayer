# coding=UTF-8

# --------------------------------------------------------------
# class_mongodata文件
# @class: MongoData类
# @introduction: MongoData类用来导入和到处MongoDB数据
# @dependency: pymongo包
# @author: plutoese
# @date: 2016.01.27
# --------------------------------------------------------------

from libs.class_mongodb import MongoDB
import pandas as pd
from pandas import Index


class MongoData:
    """MongoData类用来导入和到处MongoDB数据

    :param str host: 数据库主机，默认是'localhost'
    :param int port: 数据库端口，默认是27017
    :param str mongo_str: 数据库连接字符串
    :return: 无返回值
    """
    def __init__(self, host='localhost', port=27017,mongo_str=None):
        self.db = MongoDB(host,port,mongo_str)
        self.collection = None

    def connect(self,database=None,collection=None):
        """ 连接数据库

        :param str database: 数据库名
        :param str collection: 集合名
        :return: 无返回值
        """
        self.db.connect(database,collection)
        self.collection = self.db.collection

    def find(self,out_format='standard',groupby=None,on=None,how='outer',sort_by=None,**kwargs):
        """ 查询数据库，并返回结果

        :param out_format:
        :param groupby:
        :param on:
        :param how:
        :param sort_by:
        :param kwargs:
        :return:
        """
        if out_format == 'raw':
            return self.collection.find(**kwargs)
        elif out_format == 'standard':
            return self.tranform(self.collection.find(**kwargs),
                                 out_format=out_format,groupby=groupby,on=on,how=how,sort_by=sort_by)
        else:
            return None

    @staticmethod
    def tranform(rdata,out_format='standard',groupby=None,on=None,how='outer',sort_by=None):
        """ 数据格式转换

        :param rdata:
        :param out_format:
        :param groupby:
        :param on:
        :param how:
        :param sort_by:
        :return:
        """
        if out_format == 'standard':
            mdata = pd.DataFrame(list(rdata))
            grouped = mdata.groupby(groupby)
            first = True
            for name,group in grouped:
                del group[groupby]
                # 更改横轴变量名
                index_list = group.columns.tolist()
                value_location = group.columns.get_loc('value')
                index_list[value_location] = name
                group.columns = Index(index_list)

                if first:
                    result = group
                    first = False
                else:
                    result = pd.merge(result, group, how=how, on=on)
            if sort_by is not None:
                return result.sort_values(sort_by)
            else:
                return result

    def close(self):
        """ 关闭MongoDB连接

        :return: 无返回值
        """
        self.db.close()


if __name__ == '__main__':
    mdata = MongoData()
    mdata.connect('region','ceic')
    print(mdata.find(groupby='variable',on=['region','year'],sort_by=['region','year'],how='inner',
                     filter={'year':2013,'variable':{'$in':['人口数','人均可支配收入']}},
                     projection={'_id':False,'variable':True,'value':True,'region':True,'year':True}))
    mdata.close()

