# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hbaic1-misc.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(390, 140)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(390, 140))
        Dialog.setMaximumSize(QtCore.QSize(520, 140))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.emGroupBox = QtWidgets.QGroupBox(Dialog)
        self.emGroupBox.setObjectName("emGroupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.emGroupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.emFilter1Button = QtWidgets.QPushButton(self.emGroupBox)
        self.emFilter1Button.setCheckable(True)
        self.emFilter1Button.setAutoExclusive(True)
        self.emFilter1Button.setObjectName("emFilter1Button")
        self.horizontalLayout_2.addWidget(self.emFilter1Button)
        self.emFilter2Button = QtWidgets.QPushButton(self.emGroupBox)
        self.emFilter2Button.setCheckable(True)
        self.emFilter2Button.setAutoExclusive(True)
        self.emFilter2Button.setObjectName("emFilter2Button")
        self.horizontalLayout_2.addWidget(self.emFilter2Button)
        self.emFilter3Button = QtWidgets.QPushButton(self.emGroupBox)
        self.emFilter3Button.setCheckable(True)
        self.emFilter3Button.setAutoExclusive(True)
        self.emFilter3Button.setObjectName("emFilter3Button")
        self.horizontalLayout_2.addWidget(self.emFilter3Button)
        self.emFilter4Button = QtWidgets.QPushButton(self.emGroupBox)
        self.emFilter4Button.setCheckable(True)
        self.emFilter4Button.setAutoExclusive(True)
        self.emFilter4Button.setObjectName("emFilter4Button")
        self.horizontalLayout_2.addWidget(self.emFilter4Button)
        self.emFilter5Button = QtWidgets.QPushButton(self.emGroupBox)
        self.emFilter5Button.setCheckable(True)
        self.emFilter5Button.setAutoExclusive(True)
        self.emFilter5Button.setObjectName("emFilter5Button")
        self.horizontalLayout_2.addWidget(self.emFilter5Button)
        self.emFilter6Button = QtWidgets.QPushButton(self.emGroupBox)
        self.emFilter6Button.setCheckable(True)
        self.emFilter6Button.setAutoExclusive(True)
        self.emFilter6Button.setObjectName("emFilter6Button")
        self.horizontalLayout_2.addWidget(self.emFilter6Button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.emCheckBox = QtWidgets.QCheckBox(self.emGroupBox)
        self.emCheckBox.setObjectName("emCheckBox")
        self.horizontalLayout.addWidget(self.emCheckBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.emLabel = QtWidgets.QLabel(self.emGroupBox)
        self.emLabel.setObjectName("emLabel")
        self.horizontalLayout.addWidget(self.emLabel)
        self.emSpinBox = QtWidgets.QSpinBox(self.emGroupBox)
        self.emSpinBox.setMinimum(1)
        self.emSpinBox.setMaximum(1000)
        self.emSpinBox.setObjectName("emSpinBox")
        self.horizontalLayout.addWidget(self.emSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.emGroupBox)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.okButton = QtWidgets.QPushButton(Dialog)
        self.okButton.setCheckable(False)
        self.okButton.setObjectName("okButton")
        self.horizontalLayout_3.addWidget(self.okButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "HAL-4000 Miscellaneous Controls"))
        self.emGroupBox.setTitle(_translate("Dialog", "Emission Filter Wheel Control"))
        self.emFilter1Button.setText(_translate("Dialog", "1"))
        self.emFilter2Button.setText(_translate("Dialog", "2"))
        self.emFilter3Button.setText(_translate("Dialog", "3"))
        self.emFilter4Button.setText(_translate("Dialog", "4"))
        self.emFilter5Button.setText(_translate("Dialog", "5"))
        self.emFilter6Button.setText(_translate("Dialog", "6"))
        self.emCheckBox.setText(_translate("Dialog", "Move During Filming"))
        self.emLabel.setText(_translate("Dialog", "Period (frames)"))
        self.okButton.setText(_translate("Dialog", "Ok"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
