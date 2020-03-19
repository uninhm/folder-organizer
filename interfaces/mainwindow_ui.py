# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(490, 321)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setEnabled(True)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tree = QtWidgets.QTreeWidget(self.centralWidget)
        self.tree.setObjectName("tree")
        self.tree.header().setMinimumSectionSize(0)
        self.gridLayout.addWidget(self.tree, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 490, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.actionNewFilter = QtWidgets.QAction(MainWindow)
        self.actionNewFilter.setObjectName("actionNewFilter")
        self.actionEdit_selected_filter = QtWidgets.QAction(MainWindow)
        self.actionEdit_selected_filter.setObjectName("actionEdit_selected_filter")
        self.actionEditFilter = QtWidgets.QAction(MainWindow)
        self.actionEditFilter.setObjectName("actionEditFilter")
        self.actionStartProgram = QtWidgets.QAction(MainWindow)
        self.actionStartProgram.setObjectName("actionStartProgram")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionDeleteFilter = QtWidgets.QAction(MainWindow)
        self.actionDeleteFilter.setObjectName("actionDeleteFilter")
        self.actionSetFolder = QtWidgets.QAction(MainWindow)
        self.actionSetFolder.setObjectName("actionSetFolder")
        self.menu.addAction(self.actionNewFilter)
        self.menu.addAction(self.actionEditFilter)
        self.menu.addAction(self.actionDeleteFilter)
        self.menu.addSeparator()
        self.menu.addAction(self.actionSetFolder)
        self.menu.addAction(self.actionStartProgram)
        self.menu.addSeparator()
        self.menu.addAction(self.actionExit)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Download Manager"))
        self.tree.headerItem().setText(0, _translate("MainWindow", "Id"))
        self.tree.headerItem().setText(1, _translate("MainWindow", "Name"))
        self.tree.headerItem().setText(2, _translate("MainWindow", "Extensions"))
        self.menu.setTitle(_translate("MainWindow", "Menu"))
        self.actionNewFilter.setText(_translate("MainWindow", "New filter"))
        self.actionEdit_selected_filter.setText(_translate("MainWindow", "Edit selected filter"))
        self.actionEditFilter.setText(_translate("MainWindow", "Edit selected filter"))
        self.actionStartProgram.setText(_translate("MainWindow", "Start program"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionDeleteFilter.setText(_translate("MainWindow", "Delete filter"))
        self.actionSetFolder.setText(_translate("MainWindow", "Set downloads folder"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
