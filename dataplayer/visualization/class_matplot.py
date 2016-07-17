# coding=UTF-8

# --------------------------------------------------------------
# class_matplot文件
# @class: MatPlot类
# @introduction: MatPlot类用来查询及处理ip
# @dependency: matplotlib包
# @author: plutoese
# @date: 2016.07.02
# --------------------------------------------------------------

import matplotlib.pyplot as plt


class MatPlot:
    def __init__(self,style='ggplot'):
        # 设定样式
        self.style = style
        plt.style.use(self.style)

    def barplot(self,left=None,height=None,orientation='vertical'):
        pass

if __name__ == '__main__':
    mplot = MatPlot()