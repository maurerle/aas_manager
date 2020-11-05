# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aas_editor/mainwindow_base.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from aas_editor.settings import APPLICATION_NAME
from aas_editor.views.treeview_pack import PackTreeView
from aas_editor.views.tab import TabWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")

        # Left part
        self.leftLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.leftLayoutWidget.setObjectName("layoutWidget")
        self.leftVerticalLayout = QtWidgets.QVBoxLayout(self.leftLayoutWidget)
        self.leftVerticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.leftVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftVerticalLayout.setObjectName("verticalLayout")

        self.toolBar = QtWidgets.QToolBar(self.leftLayoutWidget)
        self.toolBar.setMaximumHeight(30)
        self.toolBar.setObjectName("toolBar")
        self.leftVerticalLayout.addWidget(self.toolBar)

        self.lineEdit = QtWidgets.QLineEdit(self.leftLayoutWidget)
        self.lineEdit.setBaseSize(QtCore.QSize(256, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.leftVerticalLayout.addWidget(self.lineEdit)

        self.packTreeView = PackTreeView(self.leftLayoutWidget)
        self.packTreeView.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.packTreeView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.packTreeView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.packTreeView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.packTreeView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.packTreeView.setObjectName("packTreeView")
        self.leftVerticalLayout.addWidget(self.packTreeView)

        # Right part
        self.rightLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.rightLayoutWidget.setObjectName("rightLayoutWidget")
        self.rightVerticalLayout = QtWidgets.QVBoxLayout(self.rightLayoutWidget)
        self.rightVerticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.rightVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.rightVerticalLayout.setObjectName("rightVerticalLayout")

        self.splitterTabWidgets = QtWidgets.QSplitter(self.rightLayoutWidget)
        self.splitterTabWidgets.setOrientation(QtCore.Qt.Horizontal)
        self.rightVerticalLayout.addWidget(self.splitterTabWidgets)

        self.tabWidget = TabWidget(self.splitterTabWidgets)
        self.tabWidget1 = TabWidget(self.splitterTabWidgets)
        self.tabWidget.setObjectName("tabWidget")
        self.gridLayout.addWidget(self.splitter, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", APPLICATION_NAME))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Search"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))

