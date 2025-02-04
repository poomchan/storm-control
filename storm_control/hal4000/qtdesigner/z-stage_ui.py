# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'z-stage.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(162, 298)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.upLButton = QtWidgets.QPushButton(Dialog)
        self.upLButton.setMinimumSize(QtCore.QSize(66, 68))
        self.upLButton.setMaximumSize(QtCore.QSize(66, 68))
        self.upLButton.setText("")
        self.upLButton.setIconSize(QtCore.QSize(56, 56))
        self.upLButton.setAutoDefault(False)
        self.upLButton.setObjectName("upLButton")
        self.verticalLayout_2.addWidget(self.upLButton)
        self.upSButton = QtWidgets.QPushButton(Dialog)
        self.upSButton.setMinimumSize(QtCore.QSize(66, 52))
        self.upSButton.setMaximumSize(QtCore.QSize(66, 52))
        self.upSButton.setText("")
        self.upSButton.setIconSize(QtCore.QSize(56, 56))
        self.upSButton.setAutoDefault(False)
        self.upSButton.setObjectName("upSButton")
        self.verticalLayout_2.addWidget(self.upSButton)
        self.downSButton = QtWidgets.QPushButton(Dialog)
        self.downSButton.setMinimumSize(QtCore.QSize(66, 52))
        self.downSButton.setMaximumSize(QtCore.QSize(66, 52))
        self.downSButton.setText("")
        self.downSButton.setIconSize(QtCore.QSize(56, 56))
        self.downSButton.setAutoDefault(False)
        self.downSButton.setObjectName("downSButton")
        self.verticalLayout_2.addWidget(self.downSButton)
        self.downLButton = QtWidgets.QPushButton(Dialog)
        self.downLButton.setMinimumSize(QtCore.QSize(66, 68))
        self.downLButton.setMaximumSize(QtCore.QSize(66, 68))
        self.downLButton.setText("")
        self.downLButton.setIconSize(QtCore.QSize(56, 56))
        self.downLButton.setAutoDefault(False)
        self.downLButton.setObjectName("downLButton")
        self.verticalLayout_2.addWidget(self.downLButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.zPosLabel = QtWidgets.QLabel(self.groupBox)
        self.zPosLabel.setObjectName("zPosLabel")
        self.verticalLayout.addWidget(self.zPosLabel)
        self.homeButton = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.homeButton.sizePolicy().hasHeightForWidth())
        self.homeButton.setSizePolicy(sizePolicy)
        self.homeButton.setObjectName("homeButton")
        self.verticalLayout.addWidget(self.homeButton)
        self.retractButton = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.retractButton.sizePolicy().hasHeightForWidth())
        self.retractButton.setSizePolicy(sizePolicy)
        self.retractButton.setObjectName("retractButton")
        self.verticalLayout.addWidget(self.retractButton)
        self.zeroButton = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zeroButton.sizePolicy().hasHeightForWidth())
        self.zeroButton.setSizePolicy(sizePolicy)
        self.zeroButton.setObjectName("zeroButton")
        self.verticalLayout.addWidget(self.zeroButton)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.moveToGroupBox = QtWidgets.QGroupBox(Dialog)
        self.moveToGroupBox.setObjectName("moveToGroupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.moveToGroupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.goLabel = QtWidgets.QLabel(self.moveToGroupBox)
        self.goLabel.setObjectName("goLabel")
        self.verticalLayout_3.addWidget(self.goLabel)
        self.goSpinBox = QtWidgets.QDoubleSpinBox(self.moveToGroupBox)
        self.goSpinBox.setMinimum(-10000.0)
        self.goSpinBox.setMaximum(10000.0)
        self.goSpinBox.setSingleStep(0.05)
        self.goSpinBox.setObjectName("goSpinBox")
        self.verticalLayout_3.addWidget(self.goSpinBox)
        self.goButton = QtWidgets.QPushButton(self.moveToGroupBox)
        self.goButton.setObjectName("goButton")
        self.verticalLayout_3.addWidget(self.goButton)
        self.verticalLayout_4.addWidget(self.moveToGroupBox)
        spacerItem1 = QtWidgets.QSpacerItem(17, 48, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.okButton = QtWidgets.QPushButton(Dialog)
        self.okButton.setObjectName("okButton")
        self.horizontalLayout_2.addWidget(self.okButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Position"))
        self.zPosLabel.setText(_translate("Dialog", "NA"))
        self.homeButton.setText(_translate("Dialog", "Home"))
        self.retractButton.setText(_translate("Dialog", "Retract"))
        self.zeroButton.setText(_translate("Dialog", "Zero"))
        self.moveToGroupBox.setTitle(_translate("Dialog", "Move To"))
        self.goLabel.setText(_translate("Dialog", "Z (um):"))
        self.goButton.setText(_translate("Dialog", "Go"))
        self.okButton.setText(_translate("Dialog", "Ok"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
