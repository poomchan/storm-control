# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lockdisplay.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GroupBox(object):
    def setupUi(self, GroupBox):
        GroupBox.setObjectName("GroupBox")
        GroupBox.resize(310, 282)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(GroupBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.offsetLabel = QtWidgets.QLabel(GroupBox)
        self.offsetLabel.setMinimumSize(QtCore.QSize(52, 0))
        self.offsetLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.offsetLabel.setObjectName("offsetLabel")
        self.verticalLayout.addWidget(self.offsetLabel)
        self.offsetFrame = QtWidgets.QFrame(GroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.offsetFrame.sizePolicy().hasHeightForWidth())
        self.offsetFrame.setSizePolicy(sizePolicy)
        self.offsetFrame.setMinimumSize(QtCore.QSize(21, 0))
        self.offsetFrame.setMaximumSize(QtCore.QSize(21, 16777215))
        self.offsetFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.offsetFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.offsetFrame.setObjectName("offsetFrame")
        self.verticalLayout.addWidget(self.offsetFrame, 0, QtCore.Qt.AlignHCenter)
        self.offsetText = QtWidgets.QLabel(GroupBox)
        self.offsetText.setMaximumSize(QtCore.QSize(50, 16777215))
        self.offsetText.setAlignment(QtCore.Qt.AlignCenter)
        self.offsetText.setObjectName("offsetText")
        self.verticalLayout.addWidget(self.offsetText, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.sumLabel = QtWidgets.QLabel(GroupBox)
        self.sumLabel.setMinimumSize(QtCore.QSize(52, 0))
        self.sumLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.sumLabel.setObjectName("sumLabel")
        self.verticalLayout_2.addWidget(self.sumLabel)
        self.sumFrame = QtWidgets.QFrame(GroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sumFrame.sizePolicy().hasHeightForWidth())
        self.sumFrame.setSizePolicy(sizePolicy)
        self.sumFrame.setMinimumSize(QtCore.QSize(21, 0))
        self.sumFrame.setMaximumSize(QtCore.QSize(21, 16777215))
        self.sumFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sumFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.sumFrame.setObjectName("sumFrame")
        self.verticalLayout_2.addWidget(self.sumFrame, 0, QtCore.Qt.AlignHCenter)
        self.sumText = QtWidgets.QLabel(GroupBox)
        self.sumText.setMaximumSize(QtCore.QSize(50, 16777215))
        self.sumText.setAlignment(QtCore.Qt.AlignCenter)
        self.sumText.setObjectName("sumText")
        self.verticalLayout_2.addWidget(self.sumText, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.zLabel = QtWidgets.QLabel(GroupBox)
        self.zLabel.setMinimumSize(QtCore.QSize(52, 0))
        self.zLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.zLabel.setObjectName("zLabel")
        self.verticalLayout_3.addWidget(self.zLabel)
        self.zFrame = QtWidgets.QFrame(GroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zFrame.sizePolicy().hasHeightForWidth())
        self.zFrame.setSizePolicy(sizePolicy)
        self.zFrame.setMinimumSize(QtCore.QSize(21, 0))
        self.zFrame.setMaximumSize(QtCore.QSize(21, 16777215))
        self.zFrame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.zFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.zFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.zFrame.setObjectName("zFrame")
        self.verticalLayout_3.addWidget(self.zFrame, 0, QtCore.Qt.AlignHCenter)
        self.zText = QtWidgets.QLabel(GroupBox)
        self.zText.setMaximumSize(QtCore.QSize(50, 16777215))
        self.zText.setAlignment(QtCore.Qt.AlignCenter)
        self.zText.setObjectName("zText")
        self.verticalLayout_3.addWidget(self.zText, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.qpdLabel = QtWidgets.QLabel(GroupBox)
        self.qpdLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.qpdLabel.setObjectName("qpdLabel")
        self.verticalLayout_4.addWidget(self.qpdLabel)
        self.qpdFrame = QtWidgets.QFrame(GroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qpdFrame.sizePolicy().hasHeightForWidth())
        self.qpdFrame.setSizePolicy(sizePolicy)
        self.qpdFrame.setMinimumSize(QtCore.QSize(120, 120))
        self.qpdFrame.setMaximumSize(QtCore.QSize(120, 120))
        self.qpdFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.qpdFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.qpdFrame.setObjectName("qpdFrame")
        self.verticalLayout_4.addWidget(self.qpdFrame)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.qpdXText = QtWidgets.QLabel(GroupBox)
        self.qpdXText.setObjectName("qpdXText")
        self.horizontalLayout.addWidget(self.qpdXText)
        self.qpdYText = QtWidgets.QLabel(GroupBox)
        self.qpdYText.setObjectName("qpdYText")
        self.horizontalLayout.addWidget(self.qpdYText)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.irSlider = QtWidgets.QSlider(GroupBox)
        self.irSlider.setMinimum(0)
        self.irSlider.setMaximum(100)
        self.irSlider.setProperty("value", 0)
        self.irSlider.setOrientation(QtCore.Qt.Horizontal)
        self.irSlider.setObjectName("irSlider")
        self.verticalLayout_4.addWidget(self.irSlider)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.irButton = QtWidgets.QPushButton(GroupBox)
        self.irButton.setCheckable(True)
        self.irButton.setObjectName("irButton")
        self.horizontalLayout_2.addWidget(self.irButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.retranslateUi(GroupBox)
        QtCore.QMetaObject.connectSlotsByName(GroupBox)

    def retranslateUi(self, GroupBox):
        _translate = QtCore.QCoreApplication.translate
        GroupBox.setWindowTitle(_translate("GroupBox", "GroupBox"))
        GroupBox.setTitle(_translate("GroupBox", "Status"))
        self.offsetLabel.setText(_translate("GroupBox", "Offset"))
        self.offsetText.setText(_translate("GroupBox", "na"))
        self.sumLabel.setText(_translate("GroupBox", "Sum"))
        self.sumText.setText(_translate("GroupBox", "na"))
        self.zLabel.setText(_translate("GroupBox", "Stage Z"))
        self.zText.setText(_translate("GroupBox", "na"))
        self.qpdLabel.setText(_translate("GroupBox", "QPD Signal"))
        self.qpdXText.setText(_translate("GroupBox", "x:"))
        self.qpdYText.setText(_translate("GroupBox", "y:"))
        self.irButton.setText(_translate("GroupBox", "IR ON"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GroupBox = QtWidgets.QGroupBox()
    ui = Ui_GroupBox()
    ui.setupUi(GroupBox)
    GroupBox.show()
    sys.exit(app.exec_())
