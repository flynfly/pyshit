# -*- coding: utf-8 -*-
#by：谢天哲
# Created by: PyQt5 UI code generator 5.15.4


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1237, 860)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.biglay=QtWidgets.QHBoxLayout(mainWindow)
        self.centralwidget.setLayout(self.biglay)


        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setObjectName("widget1")
        self.lay1=QtWidgets.QVBoxLayout(self.widget1)
        self.widget1.setLayout(self.lay1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.setReadOnly(True)
        self.lay1.addWidget(self.label)
        self.lay1.addWidget(self.listWidget,6)
        self.lay1.addWidget(self.plainTextEdit,4)
        self.biglay.addWidget(self.widget1,5)



        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setObjectName("widget2")
        self.lay2 = QtWidgets.QVBoxLayout(self.widget2)
        self.widget2.setLayout(self.lay2)
        self.biglay.addWidget(self.widget2, 24)

        self.widget21 = QtWidgets.QWidget(self.widget2)
        self.widget21.setObjectName("widget21")

        self.lay2.addWidget(self.widget21)
        self.lay2.setSpacing(1)
        self.biglay.addStretch(1)

        self.widget22 = QtWidgets.QWidget(self.widget2)
        self.widget22.setObjectName("widget22")
        self.lay22 = QtWidgets.QHBoxLayout(self.widget22)
        self.widget22.setLayout(self.lay22)
        self.lay2.addWidget(self.widget22)

        self.widget221 = QtWidgets.QWidget(self.widget22)
        self.lay221 = QtWidgets.QHBoxLayout(self.widget221)
        self.widget22.setLayout(self.lay221)
        self.widget222 = QtWidgets.QWidget(self.widget22)
        self.lay222 = QtWidgets.QHBoxLayout(self.widget222)
        self.widget222.setLayout(self.lay222)
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalSlider.setStyleSheet("QSlider::handle:horizontal {min-width: 20px;}")
        self.horizontalSlider_2.setStyleSheet("QSlider::handle:horizontal {min-width: 20px;}")

        self.horizontalSlider.setMaximumHeight(30)  # 将滑块的最大高度设置为20像素
        self.horizontalSlider_2.setMaximumHeight(30)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.lay221.addWidget(self.horizontalSlider)
        self.lay222.addWidget(self.horizontalSlider_2)
        self.widget220 = QtWidgets.QWidget(self.widget22)
        self.lay220 = QtWidgets.QGridLayout(self.widget22)
        self.widget220.setLayout(self.lay220)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setFixedWidth(90)
        self.lay220.addWidget(self.widget221,0,0)
        self.lay220.addWidget(self.label_2,1,0)
        self.lay220.addWidget(self.widget222,2,0)
        self.lay220.addWidget(self.pushButton,3,0)
        self.lay220.setSpacing(1)
        self.widget220.setMaximumHeight(110)

        self.lay22.addStretch(2)
        self.lay22.addWidget(self.widget220,34)
        self.lay22.addStretch(1)
        self.widget22.setMaximumHeight(150)  # 将widget22的最大高度设置为50像素
        mainWindow.setCentralWidget(self.centralwidget)


        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1237, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        self.menu_5 = QtWidgets.QMenu(self.menubar)
        self.menu_5.setObjectName("menu_5")
        self.menu_6 = QtWidgets.QMenu(self.menubar)
        self.menu_6.setObjectName("menu_6")
        mainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.menu_openfile = QtWidgets.QAction(mainWindow)
        self.menu_openfile.setObjectName("menu_openfile")
        self.menu_savefile = QtWidgets.QAction(mainWindow)
        self.menu_savefile.setObjectName("menu_savefile")
        self.actionFFT = QtWidgets.QAction(mainWindow)
        self.actionFFT.setObjectName("actionFFT")
        self.actionbandfilt = QtWidgets.QAction(mainWindow)
        self.actionbandfilt.setObjectName("actionbandfilt")
        self.action_2 = QtWidgets.QAction(mainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(mainWindow)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(mainWindow)
        self.action = QtWidgets.QAction(mainWindow)
        self.action.setObjectName("action")
        self.action_5 = QtWidgets.QAction(mainWindow)
        self.action_6 = QtWidgets.QAction(mainWindow)


        self.menu.addAction(self.menu_openfile)
        self.menu.addAction(self.menu_savefile)
        self.menu_4.addSeparator()
        self.menu_4.addSeparator()
        self.menu_4.addSeparator()
        self.menu_4.addAction(self.action_4)
        self.menu_5.addAction(self.actionFFT)
        self.menu_5.addAction(self.actionbandfilt)
        self.menu_5.addAction(self.action_2)
        self.menu_5.addAction(self.action_3)
        self.menu_5.addAction(self.action)
        self.menu_5.addAction(self.action_5)
        self.menu_5.addAction(self.action_6)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())
        self.action_del = self.menubar.addAction('采集')
        self.action_h = self.menubar.addAction('帮助')


        self.retranslateUi(mainWindow)
        self.menu_openfile.triggered.connect(mainWindow.openfile)
        self.menu_savefile.triggered.connect(mainWindow.savedata)
        self.actionFFT.triggered.connect(mainWindow.fft_data)
        self.actionbandfilt.triggered.connect(mainWindow.bandpassfiltAndShow)
        self.action_2.triggered.connect(mainWindow.dirrect_power)
        self.action_3.triggered.connect(mainWindow.cor_power)
        self.action.triggered.connect(mainWindow.multifilt)
        self.action_5.triggered.connect(mainWindow.amp)
        self.action_6.triggered.connect(mainWindow.tech2)
        self.pushButton.clicked.connect(mainWindow.cut_data)
        self.listWidget.itemDoubleClicked.connect(mainWindow.on_listWidgetItemDoubleClicked)
        self.action_4.triggered.connect(mainWindow.selectChannel)
        self.action_del.triggered.connect(mainWindow.delsys)
        self.action_h.triggered.connect(mainWindow.helper)

        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "信号处理系统"))
        self.label.setText(_translate("mainWindow", "数据文件:"))
        self.label_2.setText(_translate("mainWindow", "上下限"))
        self.pushButton.setText(_translate("mainWindow", "裁剪"))
        self.menu.setTitle(_translate("mainWindow", "文件"))
        self.menu_2.setTitle(_translate("mainWindow", "编辑"))
        self.menu_3.setTitle(_translate("mainWindow", "视图"))
        self.menu_4.setTitle(_translate("mainWindow", "作图"))
        self.menu_5.setTitle(_translate("mainWindow", "信号处理"))
        self.menu_6.setTitle(_translate("mainWindow", "帮助"))
        self.menu_openfile.setText(_translate("mainWindow", "打开"))
        self.menu_openfile.setToolTip(_translate("mainWindow", "打开一个数据文件"))
        self.menu_savefile.setText(_translate("mainWindow", "保存"))
        self.actionFFT.setText(_translate("mainWindow", "傅里叶变换"))
        self.actionbandfilt.setText(_translate("mainWindow", "快速滤波"))
        self.action_2.setText(_translate("mainWindow", "直接功率谱"))
        self.action_3.setText(_translate("mainWindow", "相关功率谱"))
        self.action.setText(_translate("mainWindow", "滤波高级选项"))
        self.action_4.setText(_translate("mainWindow", "通道显示"))
        self.action_5.setText(_translate("mainWindow", "时域特征计算"))
        self.action_6.setText(_translate("mainWindow", "其它选项"))
