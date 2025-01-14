# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_menu.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os


class Ui_MainMenu(object):
    def setupUi(self, MainMenu):
        MainMenu.setObjectName("MainMenu")
        MainMenu.resize(1280, 720)
        MainMenu.setStyleSheet("QMainWindow \n"
"{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.image_label = QtWidgets.QLabel(self.centralwidget)
        self.image_label.setGeometry(QtCore.QRect(1, 85, 1280, 660)) #cam
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.image_label.setFont(font)
        self.image_label.setStyleSheet("color: rgb(255, 255, 255);")
        #self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.setScaledContents(True)
        self.image_label.setObjectName("image_label")
        
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(35, 200, 120, 120))
        camIcon = QtGui.QIcon()
        camIcon.addPixmap(QtGui.QPixmap("resources/CamIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.start_button.setIcon(camIcon)
        self.start_button.setIconSize(QtCore.QSize(100,100))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.start_button.setFont(font)
        self.start_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start_button.setObjectName("start_button")
        self.start_button.setStyleSheet("QPushButton{\n"
"font: 63 28pt \"URW Gothic L\";\n"
"border:1px transparent;\n"
"border-radius: 20px;\n"
"color: #fff;\n"
"background-color: #00FF00;\n"
"border: transparent\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #fff;\n"
"background-color: #00FF00;\n"
"border: transparent\n"
"}\n"
"\n"
"")
        
        self.stop_button = QtWidgets.QPushButton(self.centralwidget)
        self.stop_button.setGeometry(QtCore.QRect(35, 420, 120, 120))
        crossIcon = QtGui.QIcon()
        crossIcon.addPixmap(QtGui.QPixmap("resources/cross.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stop_button.setIcon(crossIcon)
        self.stop_button.setIconSize(QtCore.QSize(80,80))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.stop_button.setFont(font)
        self.stop_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stop_button.setStyleSheet("QPushButton{\n"
"font: 63 24pt \"URW Gothic L\";\n"
"border:1px transparent;\n"
"border-radius: 20px;\n"
"color: #fff;\n"
"background-color: #FF0000;\n"
"border: transparent\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #fff;\n"
"background-color: #FF0000;\n"
"border: transparent\n"
"}\n"
"\n"
"")
        self.stop_button.setObjectName("stop_button")
        self.photo_taken_notification = QtWidgets.QLabel(self.centralwidget)
        self.photo_taken_notification.setEnabled(True)
        self.photo_taken_notification.setGeometry(QtCore.QRect(1200, 0, 420, 61))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.photo_taken_notification.setFont(font)
        self.photo_taken_notification.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.photo_taken_notification.setStyleSheet("border: transparent;\n"
"background-color: transparent;\n"
"color: #DA7720;\n"
"font: 63 24pt \"URW Gothic L\";")
        self.photo_taken_notification.setText("")
        self.photo_taken_notification.setAlignment(QtCore.Qt.AlignCenter)
        self.photo_taken_notification.setObjectName("photo_taken_notification")
        self.mask_count_label = QtWidgets.QLabel(self.centralwidget)
        self.mask_count_label.setEnabled(True)
        self.mask_count_label.setGeometry(QtCore.QRect(10, 80, 401, 51))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.mask_count_label.setFont(font)
        self.mask_count_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mask_count_label.setStyleSheet("border: transparent;\n"
"background-color: transparent;\n"
"color: rgb(255,255,255);\n"
"font-weight: bold;\n"
"font-weight:600;"
"font: 63 30pt \"URW Gothic L\";")
        self.mask_count_label.setText("")
        self.mask_count_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.mask_count_label.setIndent(10)
        self.mask_count_label.setObjectName("mask_count_label")
        self.no_mask_count_label = QtWidgets.QLabel(self.centralwidget)
        self.no_mask_count_label.setEnabled(True)
        self.no_mask_count_label.setGeometry(QtCore.QRect(410, 80, 431, 51))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(7)
        self.no_mask_count_label.setFont(font)
        self.no_mask_count_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.no_mask_count_label.setStyleSheet("border: transparent;\n"
"background-color: transparent;\n"
"color: rgb(255,255,255);\n"
"font-weight: bold;\n"
"font-weight:600;"
"font: 63 30pt \"URW Gothic L\";")
        self.no_mask_count_label.setText("")
        self.no_mask_count_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.no_mask_count_label.setIndent(10)
        self.no_mask_count_label.setObjectName("no_mask_count_label")
        self.status_label = QtWidgets.QLabel(self.centralwidget)
        self.status_label.setEnabled(True)
        self.status_label.setGeometry(QtCore.QRect(810, 80, 141, 51))
        self.status_label.setScaledContents(True)
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(7)
        self.status_label.setFont(font)
        self.status_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.status_label.setStyleSheet("border: transparent;\n"
"background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"font: 63 24pt \"URW Gothic L\";")
        self.status_label.setText("")
        #self.status_label.setAlignment(QtCore.Qt.AlignCenter)
        self.status_label.setIndent(10)
        self.status_label.setObjectName("status_label")
        self.status_type_label = QtWidgets.QLabel(self.centralwidget)
        self.status_type_label.setEnabled(True)
        self.status_type_label.setGeometry(QtCore.QRect(850, 70, 271, 51))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.status_type_label.setFont(font)
        self.status_type_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.status_type_label.setStyleSheet("border: transparent;\n"
"background-color: transparent;\n"
"font: 63 24pt \"URW Gothic L\";")
        self.status_type_label.setText("")
        self.status_type_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.status_type_label.setIndent(10)
        self.status_type_label.setObjectName("status_type_label")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(300, 0, 781, 62))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.camera_select_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(32)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.camera_select_label.setFont(font)
        self.camera_select_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.camera_select_label.setStyleSheet("border: transparent;\n"
"background-color: transparent;\n"
"color: #228B22;\n"
"font: 32pt \"Gill Sans MT\";")
        self.camera_select_label.move(10,170)
        
        self.camera_select_label.setObjectName("camera_select_label")
        self.horizontalLayout.addWidget(self.camera_select_label)
        self.camera_select = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.camera_select.sizePolicy().hasHeightForWidth())
        self.camera_select.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(60, 76, 173))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.503, 0.0, 0.503, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(190, 201, 184))
        gradient.setColorAt(0.511364, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 76, 173))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 76, 173))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.503, 0.0, 0.503, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(190, 201, 184))
        gradient.setColorAt(0.511364, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.503, 0.0, 0.503, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(190, 201, 184))
        gradient.setColorAt(0.511364, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 76, 173))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.503, 0.0, 0.503, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(190, 201, 184))
        gradient.setColorAt(0.511364, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 76, 173))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 76, 173))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.503, 0.0, 0.503, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(190, 201, 184))
        gradient.setColorAt(0.511364, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.503, 0.0, 0.503, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(190, 201, 184))
        gradient.setColorAt(0.511364, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 76, 173))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.503, 0.0, 0.503, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(190, 201, 184))
        gradient.setColorAt(0.511364, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 76, 173))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 76, 173))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.503, 0.0, 0.503, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(190, 201, 184))
        gradient.setColorAt(0.511364, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.503, 0.0, 0.503, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(190, 201, 184))
        gradient.setColorAt(0.511364, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        self.camera_select.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.camera_select.setFont(font)
        self.camera_select.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.camera_select.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.camera_select.setStyleSheet("QComboBox\n"
"{\n"
"font: 14pt \"URW Gothic L\";\n"
"color: #3C4CAD;\n"
"border: 1px solid #D3D3D3;\n"
"background-color: qlineargradient(spread:pad, x1:0.503, y1:0, x2:0.503, y2:1, stop:0 rgba(190, 201, 184, 255), stop:0.511364 rgba(255, 255, 255, 255));\n"
"selection-color: rgb(255, 255, 255);\n"
"    selection-background-color: rgb(255, 0, 0);\n"
"border-radius: 16px;\n"
"padding: 1px 15px 1px 10px;\n"
"min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"background-color: qlineargradient(spread:pad, x1:0.52, y1:0, x2:0.503, y2:1, stop:0 rgba(143, 198, 118, 255), stop:0.511364 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"border: 1px solid #D3D3D3;\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0.503, y1:0, x2:0.503, y2:1, stop:0 rgba(190, 201, 184, 255), stop:0.511364 rgba(255, 255, 255, 255));\n"
"padding: 1px 15px 1px 10px;\n"
"}\n"
"\n"
"QComboBox::down-\n"
"{\n"
"padding: 10px 10px 5px 5px;\n"
" }\n"
"\n"
"QComboBox::down-arrow:on \n"
"{\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"\n"
"QComboBox QListView\n"
"{\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.camera_select.setCurrentText("")
        self.camera_select.setMaxVisibleItems(15)
        self.camera_select.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.camera_select.setObjectName("camera_select")
        self.horizontalLayout.addWidget(self.camera_select)
        MainMenu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainMenu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1880, 22))
        self.menubar.setObjectName("menubar")
        MainMenu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainMenu)
        self.statusbar.setObjectName("statusbar")
        MainMenu.setStatusBar(self.statusbar)

        self.epf = QtWidgets.QLabel(self.centralwidget) # image
        self.epf.setGeometry(QtCore.QRect(0, 0, 195, 90)) 
        self.epf.setPixmap(QtGui.QPixmap("resources/Logo_EPF.png"))
        self.epf.setScaledContents(True)
        self.epf.setObjectName("epf")
     
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget) 
        self.pushButton1.setGeometry(QtCore.QRect(380, 10, 200, 70))
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton1.setVisible(False)

        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget) 
        self.pushButton2.setGeometry(QtCore.QRect(680, 10, 200, 70))
        self.pushButton2.setObjectName("pushButton2")

        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget) 
        self.pushButton3.setGeometry(QtCore.QRect(980, 10, 200, 70))
        self.pushButton3.setObjectName("pushButton3")

        self.description = QtWidgets.QLabel(self.centralwidget)
        self.description.setGeometry(QtCore.QRect(50, 150, 900, 650)) # texte de description
        str = open('resources/Description.txt', 'r').read()
        self.description.setText(str)
        self.description.setFont(QtGui.QFont('Arial', 38))
        self.description.setStyleSheet("QLabel { background-color : white; color : black; }")
        self.description.adjustSize()
        self.description.setVisible(False)
        self.description.setEnabled(True)

        self.QRCodeTxt = QtWidgets.QLabel(self.centralwidget)
        self.QRCodeTxt.setGeometry(QtCore.QRect(650, 300, 400, 650)) # texte de description
        strQR = open('resources/QRCode.txt', 'r').read()
        self.QRCodeTxt.setText(strQR)
        self.QRCodeTxt.setFont(QtGui.QFont('Arial', 38))
        self.QRCodeTxt.setStyleSheet("QLabel { background-color : white; color : black; }")
        self.QRCodeTxt.adjustSize()
        self.QRCodeTxt.setVisible(False)
        self.QRCodeTxt.setEnabled(True)

        self.QRCode = QtWidgets.QLabel(self.centralwidget)
        self.QRCode.setGeometry(QtCore.QRect(100, 150, 500, 500))
        self.QRCode.setPixmap(QtGui.QPixmap("resources/QRCode.PNG"))
        self.QRCode.setScaledContents(True)
        self.QRCode.setVisible(False)

        self.arrow = QtWidgets.QPushButton(self.centralwidget)
        self.arrow.setGeometry(QtCore.QRect(1050, 600, 120, 60))
        self.arrow.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/LeftArrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.arrow.setVisible(False)
        self.arrow.setEnabled(False)
        self.arrow.setIconSize(QtCore.QSize(30,30))
        self.arrow.setIcon(icon)
        self.arrow.setObjectName("pushButton")

        self.DownArrow = QtWidgets.QPushButton(self.centralwidget)
        self.DownArrow.setGeometry(QtCore.QRect(930, 600, 120, 60))
        self.DownArrow.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("resources/DownArrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DownArrow.setVisible(False)
        self.DownArrow.setEnabled(False)
        self.DownArrow.setIcon(icon2)
        self.DownArrow.setIconSize(QtCore.QSize(30,30))

        self.UpArrow = QtWidgets.QPushButton(self.centralwidget)
        self.UpArrow.setGeometry(QtCore.QRect(930, 600, 120, 60))
        self.UpArrow.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("resources/UpArrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.UpArrow.setVisible(False)
        self.UpArrow.setEnabled(False)
        self.UpArrow.setIcon(icon3)
        self.UpArrow.setIconSize(QtCore.QSize(30,30))

        self.chart2 = QtWidgets.QLabel(self.centralwidget)
        self.chart2.setGeometry(QtCore.QRect(50, 150, 800, 800))
        self.chart2.adjustSize()
        self.chart2.setVisible(False)
        self.chart2.setEnabled(True)

        self.labelStat = QtWidgets.QLabel(self.centralwidget)
        self.labelStat.setGeometry(QtCore.QRect(690, 150, 900, 400))
        self.labelStat.setVisible(False)
        self.labelStat.setEnabled(True)

        self.fond = QtWidgets.QLabel(self.centralwidget)
        self.fond.setGeometry(QtCore.QRect(300, 100, 900, 400))
        self.fond.setPixmap(QtGui.QPixmap("resources/fmde_logo.png"))
        self.fond.adjustSize()

        self.retranslateUi(MainMenu)
        QtCore.QMetaObject.connectSlotsByName(MainMenu)

        #self.status_label.move(930,80)
        self.status_label.setStyleSheet("border: transparent;\n"
"background-color: transparent;\n"
"color: rgb(255,255,255);\n"
"font-weight: bold;\n"
"font-weight:600;"
"font: 63 30pt \"URW Gothic L\";")
        self.status_type_label.move(950,80)
        self.status_type_label.setStyleSheet("border: transparent;\n"
"background-color: transparent;\n"
"color: rgb(255,255,255);\n"
"font-weight: bold;\n"
"font-weight:600;"
"font: 63 30pt \"URW Gothic L\";")

    def retranslateUi(self, MainMenu):
        _translate = QtCore.QCoreApplication.translate
        MainMenu.setWindowTitle(_translate("MainMenu", "Face Mask Detector"))
        self.image_label.setText(_translate("MainMenu", "Select a Camera"))
        self.camera_select_label.setText(_translate("MainMenu", "Liste caméras:    "))
        self.camera_select.setProperty("placeholderText", _translate("MainMenu", "Select Camera"))
        self.camera_select.setVisible(False)
        self.camera_select_label.setVisible(False)
        self.pushButton1.setText(_translate("MainMenu", "Afficher \ntempérature"))
        self.pushButton2.setText(_translate("MainMenu", "Statistiques"))
        self.pushButton3.setText(_translate("MainMenu", "Description du \nprojet"))
        #self.status_label.move(1050,60)

        self.pushButton1.setStyleSheet("QPushButton{\n"
"font: 63 20pt \"URW Gothic L\";\n"
"border:1px transparent;\n"
"border-radius: 20px;\n"
"color: #FFFFFF;\n"
"background-color: #000000;\n"
"border: transparent\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #fff;\n"
"background-color: #000000;\n"
"border: transparent\n"
"}\n"
"\n"
"")

        self.pushButton2.setStyleSheet("QPushButton{\n"
"font: 63 25pt \"URW Gothic L\";\n"
"border:1px transparent;\n"
"border-radius: 20px;\n"
"color: #FFFFFF;\n"
"background-color: #000000;\n"
"border: transparent\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #fff;\n"
"background-color: #000000;\n"
"border: transparent\n"
"}\n"
"\n"
"")

        self.pushButton3.setStyleSheet("QPushButton{\n"
"font: 63 18pt \"URW Gothic L\";\n"
"border:1px transparent;\n"
"border-radius: 20px;\n"
"color: #FFFFFF;\n"
"background-color: #000000;\n"
"border: transparent\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #fff;\n"
"background-color: #000000;\n"
"border: transparent\n"
"}\n"
"\n"
"")