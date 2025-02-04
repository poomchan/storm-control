# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spotcounter.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(554, 645)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(0, 0))
        Dialog.setMaximumSize(QtCore.QSize(10000, 10000))
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.countsTab = QtWidgets.QWidget()
        self.countsTab.setObjectName("countsTab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.countsTab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.countsText1 = QtWidgets.QLabel(self.countsTab)
        self.countsText1.setObjectName("countsText1")
        self.horizontalLayout_3.addWidget(self.countsText1)
        self.countsLabel1 = QtWidgets.QLabel(self.countsTab)
        self.countsLabel1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.countsLabel1.setObjectName("countsLabel1")
        self.horizontalLayout_3.addWidget(self.countsLabel1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.maxSpinBox = QtWidgets.QSpinBox(self.countsTab)
        self.maxSpinBox.setMinimum(10)
        self.maxSpinBox.setMaximum(1000)
        self.maxSpinBox.setSingleStep(10)
        self.maxSpinBox.setProperty("value", 1000)
        self.maxSpinBox.setObjectName("maxSpinBox")
        self.verticalLayout_2.addWidget(self.maxSpinBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.graphFrame = QtWidgets.QFrame(self.countsTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphFrame.sizePolicy().hasHeightForWidth())
        self.graphFrame.setSizePolicy(sizePolicy)
        self.graphFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.graphFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.graphFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.graphFrame.setObjectName("graphFrame")
        self.horizontalLayout_2.addWidget(self.graphFrame)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.label = QtWidgets.QLabel(self.countsTab)
        self.label.setMinimumSize(QtCore.QSize(0, 150))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.tabWidget.addTab(self.countsTab, "")
        self.imageTab = QtWidgets.QWidget()
        self.imageTab.setObjectName("imageTab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.imageTab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.countsText2 = QtWidgets.QLabel(self.imageTab)
        self.countsText2.setObjectName("countsText2")
        self.horizontalLayout_5.addWidget(self.countsText2)
        self.countsLabel2 = QtWidgets.QLabel(self.imageTab)
        self.countsLabel2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.countsLabel2.setObjectName("countsLabel2")
        self.horizontalLayout_5.addWidget(self.countsLabel2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.imageScrollArea = QtWidgets.QScrollArea(self.imageTab)
        self.imageScrollArea.setMinimumSize(QtCore.QSize(512, 512))
        self.imageScrollArea.setFrameShape(QtWidgets.QFrame.Box)
        self.imageScrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.imageScrollArea.setWidgetResizable(True)
        self.imageScrollArea.setObjectName("imageScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 510, 522))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.imageScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_4.addWidget(self.imageScrollArea)
        self.tabWidget.addTab(self.imageTab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.analyzerComboBox = QtWidgets.QComboBox(Dialog)
        self.analyzerComboBox.setObjectName("analyzerComboBox")
        self.horizontalLayout.addWidget(self.analyzerComboBox)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.okButton = QtWidgets.QPushButton(Dialog)
        self.okButton.setObjectName("okButton")
        self.horizontalLayout.addWidget(self.okButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "HAL-4000 Spot Counter"))
        self.countsText1.setText(_translate("Dialog", "Total Localizations:"))
        self.countsLabel1.setText(_translate("Dialog", "TextLabel"))
        self.label.setText(_translate("Dialog", "This Space Intentionally Left Blank"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.countsTab), _translate("Dialog", "Counts"))
        self.countsText2.setText(_translate("Dialog", "Total Localizations:"))
        self.countsLabel2.setText(_translate("Dialog", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.imageTab), _translate("Dialog", "STORM Image"))
        self.okButton.setText(_translate("Dialog", "Ok"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
