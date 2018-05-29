import requests
import re
from threading import Timer
from PyQt5 import QtCore, QtGui, QtWidgets
from ui import Ui_MainWindow
from tool import Ui_Dialog
import sys,threading,time
import csv
import time
import configparser
from PyQt5.QtWidgets import QMessageBox

class Stock(object):
    all_stocks=[]
    def __init__(self):
        config=configparser.ConfigParser()
        config.read("config.ini")
        self.save_path=config.get("path","save_path")
        self.select_path=config.get("path","select_path")

    def GetStockInfo(self,code):
        r=requests.get("http://hq.sinajs.cn/list="+code)
        a=re.findall(r'.*"(.*?)"', r.text)
        data=a[0].split(',')
        info={"name":data[0],
              "open":data[1],
              "close":data[2],
              "price":data[3],
              "high":data[4],
              "low":data[5],
              "date":data[30],
              "time":data[31]
              }
        return info


    def load_config_code(self):
        config=configparser.ConfigParser()
        config.read("config.ini")
        return [config.get("stock","code").split(","),config.get("stock","cost").split(",")]

    def download_stock(self):
        self.count = 1

        self.para_val = '[["hq","hs_a","",0,' + str(self.count) + ',500]]'  # count 页码 500 条目
        self.r_params = {'__s': self.para_val}
        self.all_quotes_url = 'http://money.finance.sina.com.cn/d/api/openapi_proxy.php/'
        self.r = requests.get(self.all_quotes_url, params=self.r_params)
        # self.all_stocks.append(self.r.json()[0]['fields'])
        field=self.r.json()[0]['fields']
        try:
            while (True):
                self.para_val = '[["hq","hs_a","",0,' + str(self.count) + ',500]]'  # count 页码 500 条目
                self.r_params = {'__s': self.para_val}
                self.all_quotes_url = 'http://money.finance.sina.com.cn/d/api/openapi_proxy.php/'
                self.r = requests.get(self.all_quotes_url, params=self.r_params)  # 根据网址下载所有的股票编号，这里使用的是新浪网址，有很多网址可以下载股票编号
                if len(self.r.json()[0]["items"]) == 0:
                    break
                for item in self.r.json()[0]["items"]:
                    temp=dict(zip(field,item))
                    if float(temp["open"])!=0:
                        self.all_stocks.append(temp)

                self.count += 1
        except:
            print("error")
    def save_all_stock(self):
        filename = self.save_path +'/'+ time.strftime("%Y%m%d", time.localtime()) + '.csv'
        if len(self.all_stocks)==0:
            self.download_stock()
            print('None')
        with open(filename, 'w') as f:
            writer = csv.DictWriter(f,fieldnames=self.all_stocks[0].keys())
            writer.writeheader()
            for row in self.all_stocks:
                writer.writerow(row)




    def select_changepercent(self,percent):
        self.download_stock()
        data = []
        for stock in self.all_stocks:
            if float(stock['changepercent'])>percent:
                data.append(stock['symbol'])

        filename = self.select_path + '/' + 'change'+time.strftime("%Y%m%d", time.localtime()) + '-' + str(percent) + '.txt'
        with open(filename, 'w')as f:
            for item in data:
                f.write('%s\n' % item)

    def select_T(self,percent):
        self.download_stock()
        self.data=[]
        for stock in self.all_stocks:
            self.price_open=(float(stock['trade']) - float(stock['open']))/float(stock['open'])*100

            if (float(stock['trade'])>float(stock['low'])*(1+(percent/100))) \
                and (float(stock['open'])>float(stock['low'])*(1+(percent/100))) \
                and float(stock['changepercent'])<9.9 \
                and float(stock['trade'])<100:
                # and float(stock['trade']) >= float(stock['open'])\
                if self.price_open>=-2.50:
                    self.data.append([stock['symbol'],'%.3f'%self.price_open])
        #save
        filename=self.select_path+'/'+time.strftime("%Y%m%d", time.localtime())+'-'+str(percent)+'.txt'
        with open(filename,'w')as f:
            for item in self.data:
                f.write('%s\t%s\n'%(item[0],item[1]))


class mainwindow(Ui_MainWindow,QtWidgets.QMainWindow):
    stock=Stock()
    top=False
    def __init__(self, parent=None):
        super(mainwindow, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.show()
        # self.pushButton.clicked.connect(self.createmonitor)
        self.pushButton_save_all.clicked.connect(self.save_all)
        self.pushButton_save_percent.clicked.connect(lambda:self.save_percent(float(self.lineEdit.text())))
        self.pushButton_select_T.clicked.connect(lambda:self.select(float(self.lineEdit.text())))
        # self.pushButton_top.clicked.connect(self.top)


        self.th=threading.Thread(target=self.realtime)
        self.th.setDaemon('True')
        self.th.start()

    def select(self,percent):
        self.stock.select_T(percent)
        self.msg()
    def save_all(self):
        self.stock.save_all_stock()
        self.msg()
    def save_percent(self,percent):
        self.stock.select_changepercent(percent)
        self.msg()

    def msg(self):
        reply = QMessageBox.information(self,  # 使用infomation信息框
                                        "标题",
                                        "保存成功")

    def top(self):
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.hide()
        # if(self.top==False):
        # self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        #     self.top=True
        # else:
        #     self.setWindowFlags(QtCore.Qt.Widget)
        #     self.top=False
        self.show()
    def realtime(self):
        while(1) :
            str=""
            codes,costs=self.stock.load_config_code()
            for code,cost in zip(codes,costs):
                info=self.stock.GetStockInfo(code)
                #涨幅
                changepercent=(float(info["price"])-float(info["close"]))/float(info["close"])*100
                #收益百分比
                profitpercent=(float(info["price"])-float(cost))/float(cost)*100
                str=str+info["name"][0]+"\t%.2f"%float(info["price"])+"\t%.2f%%\t"%changepercent+"%.2f%%"%profitpercent+'\n'

            self.label_1.setText(str)
            self.label_1.adjustSize()

    def createmonitor(self):
        data=self.textEdit.toPlainText().split(',')

        print(data)
        monitor=monitorwindow(data)
        monitor.exec()

class monitorwindow(Ui_Dialog,QtWidgets.QDialog):
    def __init__(self,parent=None):
        super(monitorwindow,self).__init__()
        self.setupUi(self)

app = QtWidgets.QApplication(sys.argv)
ui = mainwindow()
sys.exit(app.exec_())

a=Stock()
# a.save_all_stock()
# a.select_T(4.5)

# current_time=time.strftime('%H:%M:%S',time.localtime(time.time()))
# print('9:30:00'<current_time<'11:30:00' or '13:00:00'<current_time<'15:00:00' )
# count=1

# para_val = '[["hq","hs_a","",0,' + str(300) + ',20]]'
# r_params = {'__s': para_val}
# # all_quotes_url = 'http://money.finance.sina.com.cn/d/api/openapi_proxy.php/?__s=[["hq","hs_a","",0,88,40]]'
# all_quotes_url = 'http://money.finance.sina.com.cn/d/api/openapi_proxy.php/'
# r = requests.get(all_quotes_url,params=r_params)  #根据网址下载所有的股票编号，这里使用的是新浪网址，有很多网址可以下载股票编号
# print(len(r.json()[0]["items"]))

# Config=configparser.ConfigParser()
# Config.read("config.ini")
# data=Config.get("config","platformname")
# print(data.split(','))

