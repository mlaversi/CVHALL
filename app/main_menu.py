# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_menu.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainMenu(object):
    def setupUi(self, MainMenu):
        MainMenu.setObjectName("MainMenu")
        MainMenu.resize(1400, 720)
        MainMenu.setStyleSheet("QMainWindow \n"
"{\n"
"background-color: rgb(245, 253, 247);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.image_label = QtWidgets.QLabel(self.centralwidget)
        self.image_label.setGeometry(QtCore.QRect(20, 120, 1280, 720))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.image_label.setFont(font)
        self.image_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.setObjectName("image_label")
        self.take_photo_button = QtWidgets.QPushButton(self.centralwidget)
        self.take_photo_button.setGeometry(QtCore.QRect(450, 930, 331, 61))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.take_photo_button.setFont(font)
        self.take_photo_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.take_photo_button.setStyleSheet("QPushButton{\n"
"font: 63 28pt \"URW Gothic L\";\n"
"border:1px transparent;\n"
"border-radius: 20px;\n"
"color: #fff;\n"
"background-color: #228B22;\n"
"border: transparent\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #fff;\n"
"background-color: #006400;\n"
"border: transparent\n"
"}\n"
"\n"
"")
        self.take_photo_button.setObjectName("take_photo_button")
        self.start_menu_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_menu_button.setGeometry(QtCore.QRect(840, 930, 331, 61))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.start_menu_button.setFont(font)
        self.start_menu_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start_menu_button.setStyleSheet("QPushButton{\n"
"font: 63 24pt \"URW Gothic L\";\n"
"border:1px transparent;\n"
"border-radius: 20px;\n"
"color: #fff;\n"
"background-color: #8B0000;\n"
"border: transparent\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #fff;\n"
"background-color: rgb(121, 0, 0);\n"
"border: transparent\n"
"}\n"
"\n"
"")
        self.start_menu_button.setObjectName("start_menu_button")
#         self.camera_list_label = QtWidgets.QLabel(self.centralwidget)
#         self.camera_list_label.setGeometry(QtCore.QRect(1440, 60, 371, 51))
#         font = QtGui.QFont()
#         font.setFamily("URW Gothic L")
#         font.setPointSize(22)
#         font.setBold(False)
#         font.setItalic(False)
#         font.setWeight(7)
#         self.camera_list_label.setFont(font)
#         self.camera_list_label.setStyleSheet("border: transparent;\n"
# "background-color: transparent;\n"
# "color:#228B22;\n"
# "font: 63 22pt \"URW Gothic L\";")
#         self.camera_list_label.setAlignment(QtCore.Qt.AlignCenter)
#         self.camera_list_label.setObjectName("camera_list_label")
        self.photo_taken_notification = QtWidgets.QLabel(self.centralwidget)
        self.photo_taken_notification.setEnabled(True)
        self.photo_taken_notification.setGeometry(QtCore.QRect(20, 930, 381, 61))
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
"color: #DAA520;\n"
"font: 63 24pt \"URW Gothic L\";")
        self.photo_taken_notification.setText("")
        self.photo_taken_notification.setAlignment(QtCore.Qt.AlignCenter)
        self.photo_taken_notification.setObjectName("photo_taken_notification")
#         self.camera_table = QtWidgets.QTableWidget(self.centralwidget)
#         self.camera_table.setGeometry(QtCore.QRect(1440, 120, 381, 871))
#         palette = QtGui.QPalette()
#         brush = QtGui.QBrush(QtGui.QColor(210, 105, 30))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
#         brush = QtGui.QBrush(QtGui.QColor(20, 30, 60))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
#         brush = QtGui.QBrush(QtGui.QColor(210, 105, 30))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
#         brush = QtGui.QBrush(QtGui.QColor(210, 105, 30))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
#         brush = QtGui.QBrush(QtGui.QColor(20, 30, 60))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
#         brush = QtGui.QBrush(QtGui.QColor(20, 30, 60))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
#         brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
#         brush = QtGui.QBrush(QtGui.QColor(0, 209, 0))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
#         brush = QtGui.QBrush(QtGui.QColor(210, 105, 30))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
#         brush = QtGui.QBrush(QtGui.QColor(20, 30, 60))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
#         brush = QtGui.QBrush(QtGui.QColor(210, 105, 30))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
#         brush = QtGui.QBrush(QtGui.QColor(210, 105, 30))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
#         brush = QtGui.QBrush(QtGui.QColor(20, 30, 60))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
#         brush = QtGui.QBrush(QtGui.QColor(20, 30, 60))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
#         brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
#         brush = QtGui.QBrush(QtGui.QColor(0, 209, 0))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
#         brush = QtGui.QBrush(QtGui.QColor(210, 105, 30))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
#         brush = QtGui.QBrush(QtGui.QColor(20, 30, 60))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
#         brush = QtGui.QBrush(QtGui.QColor(210, 105, 30))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
#         brush = QtGui.QBrush(QtGui.QColor(210, 105, 30))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
#         brush = QtGui.QBrush(QtGui.QColor(20, 30, 60))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
#         brush = QtGui.QBrush(QtGui.QColor(20, 30, 60))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
#         brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
#         brush = QtGui.QBrush(QtGui.QColor(0, 209, 0))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
#         self.camera_table.setPalette(palette)
#         font = QtGui.QFont()
#         font.setFamily("Gill Sans MT")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         self.camera_table.setFont(font)
#         self.camera_table.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
#         self.camera_table.setFocusPolicy(QtCore.Qt.StrongFocus)
#         self.camera_table.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
#         self.camera_table.setAutoFillBackground(False)
#         self.camera_table.setStyleSheet("QTableWidget {\n"
# "color:#D2691E;\n"
# "gridline-color: rgb(0, 170, 0);\n"
# "background-color: rgb(20, 30, 60);\n"
# "hover {background-color: #1E90FF;}\n"
# "}\n"
# "\n"
# "QHeaderView::section { \n"
# "border-bottom: 1px solid green;\n"
# "gridline-color: rgb(0, 170, 0);\n"
# "background-color: rgb(6, 34, 50);\n"
# " }\n"
# "")
#         self.camera_table.setFrameShape(QtWidgets.QFrame.Box)
#         self.camera_table.setFrameShadow(QtWidgets.QFrame.Plain)
#         self.camera_table.setLineWidth(1)
#         self.camera_table.setMidLineWidth(1)
#         self.camera_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
#         self.camera_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
#         self.camera_table.setAutoScrollMargin(20)
#         self.camera_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
#         self.camera_table.setDragDropOverwriteMode(False)
#         self.camera_table.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
#         self.camera_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
#         self.camera_table.setCornerButtonEnabled(False)
#         self.camera_table.setRowCount(0)
#         self.camera_table.setObjectName("camera_table")
#         self.camera_table.setColumnCount(2)
#         item = QtWidgets.QTableWidgetItem()
#         item.setTextAlignment(QtCore.Qt.AlignCenter)
#         font = QtGui.QFont()
#         font.setFamily("Gill Sans MT")
#         font.setPointSize(20)
#         font.setBold(True)
#         font.setWeight(75)
#         font.setKerning(True)
#         item.setFont(font)
#         item.setBackground(QtGui.QColor(6, 34, 67))
#         brush = QtGui.QBrush(QtGui.QColor(20, 140, 10))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         item.setForeground(brush)
#         self.camera_table.setHorizontalHeaderItem(0, item)
#         item = QtWidgets.QTableWidgetItem()
#         item.setTextAlignment(QtCore.Qt.AlignCenter)
#         font = QtGui.QFont()
#         font.setFamily("Gill Sans MT")
#         font.setPointSize(20)
#         font.setBold(True)
#         font.setWeight(75)
#         item.setFont(font)
#         item.setBackground(QtGui.QColor(6, 34, 68))
#         brush = QtGui.QBrush(QtGui.QColor(20, 140, 10))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         item.setForeground(brush)
#         self.camera_table.setHorizontalHeaderItem(1, item)
#         self.camera_table.horizontalHeader().setCascadingSectionResizes(False)
#         self.camera_table.horizontalHeader().setDefaultSectionSize(180)
#         self.camera_table.horizontalHeader().setHighlightSections(True)
#         self.camera_table.horizontalHeader().setMinimumSectionSize(40)
#         self.camera_table.horizontalHeader().setStretchLastSection(True)
#         self.camera_table.verticalHeader().setVisible(False)
#         self.camera_table.verticalHeader().setDefaultSectionSize(40)
#         self.camera_table.verticalHeader().setMinimumSectionSize(30)
#         self.camera_table.verticalHeader().setStretchLastSection(False)
        self.mask_count_label = QtWidgets.QLabel(self.centralwidget)
        self.mask_count_label.setEnabled(True)
        self.mask_count_label.setGeometry(QtCore.QRect(130, 80, 401, 51))
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
"color: rgb(0, 0, 0);\n"
"font: 63 24pt \"URW Gothic L\";")
        self.mask_count_label.setText("")
        self.mask_count_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.mask_count_label.setIndent(10)
        self.mask_count_label.setObjectName("mask_count_label")
        self.no_mask_count_label = QtWidgets.QLabel(self.centralwidget)
        self.no_mask_count_label.setEnabled(True)
        self.no_mask_count_label.setGeometry(QtCore.QRect(530, 80, 431, 51))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.no_mask_count_label.setFont(font)
        self.no_mask_count_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.no_mask_count_label.setStyleSheet("border: transparent;\n"
"background-color: transparent;\n"
"color: rgb(0, 0, 0);\n"
"font: 63 24pt \"URW Gothic L\";")
        self.no_mask_count_label.setText("")
        self.no_mask_count_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.no_mask_count_label.setIndent(10)
        self.no_mask_count_label.setObjectName("no_mask_count_label")
        self.status_label = QtWidgets.QLabel(self.centralwidget)
        self.status_label.setEnabled(True)
        self.status_label.setGeometry(QtCore.QRect(1000, 70, 141, 51))
        self.status_label.setScaledContents(True)
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.status_label.setFont(font)
        self.status_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.status_label.setStyleSheet("border: transparent;\n"
"background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"font: 63 24pt \"URW Gothic L\";")
        self.status_label.setText("")
        self.status_label.setAlignment(QtCore.Qt.AlignCenter)
        self.status_label.setIndent(10)
        self.status_label.setObjectName("status_label")
        self.status_type_label = QtWidgets.QLabel(self.centralwidget)
        self.status_type_label.setEnabled(True)
        self.status_type_label.setGeometry(QtCore.QRect(1150, 70, 271, 51))
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
        self.camera_select_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
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
"QComboBox::down-arrow\n"
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
        self.epf.setPixmap(QtGui.QPixmap("resources/epf_logo.png"))
        self.epf.setScaledContents(True)
        #self.epf.setIcon(QtGui.QIcon("resources/epf_logo.png"))
        #self.epf.setIconSize(QtCore.QSize(100,100))
        self.epf.setObjectName("epf")
     
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget) 
        self.pushButton1.setGeometry(QtCore.QRect(1550, 180, 200, 100))
        self.pushButton1.setObjectName("pushButton1")

        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget) 
        self.pushButton2.setGeometry(QtCore.QRect(1550, 430, 200, 100))
        self.pushButton2.setObjectName("pushButton2")

        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget) 
        self.pushButton3.setGeometry(QtCore.QRect(1550, 680, 200, 100))
        self.pushButton3.setObjectName("pushButton3")

        self.timer1 = QtWidgets.QPushButton(self.centralwidget) 
        self.timer1.setGeometry(QtCore.QRect(1550, 180, 200, 100))
        self.timer1.setObjectName("timer1")
        self.timer1.setVisible(False) 
        self.timer1.setEnabled(False)

        self.timer2 = QtWidgets.QPushButton(self.centralwidget)
        self.timer2.setGeometry(QtCore.QRect(1550, 430, 200, 100))
        self.timer2.setObjectName("timer2")
        self.timer2.setVisible(False) 
        self.timer2.setEnabled(False)

        self.timer3 = QtWidgets.QPushButton(self.centralwidget)
        self.timer3.setGeometry(QtCore.QRect(1550, 680, 200, 100))
        self.timer3.setObjectName("timer3")
        self.timer3.setVisible(False) 
        self.timer3.setEnabled(False)     

        self.arrow = QtWidgets.QPushButton(self.centralwidget)
        self.arrow.setGeometry(QtCore.QRect(1550, 900, 80, 40))
        self.arrow.setText("")
        icon = QtGui.QIcon()
        #icon.addPixmap(QtGui.QPixmap("resources\LeftArrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.arrow.setStyleSheet("qproperty-icon: url(:resources\LeftArrow.png);")


        self.arrow.setIcon(icon)
        self.arrow.setObjectName("pushButton")
        #self.arrow.setVisible(False) # par defaut la fleche est desactivee
        #self.arrow.setEnabled(False)

        self.retranslateUi(MainMenu)
        QtCore.QMetaObject.connectSlotsByName(MainMenu)

    def retranslateUi(self, MainMenu):
        _translate = QtCore.QCoreApplication.translate
        MainMenu.setWindowTitle(_translate("MainMenu", "Face Mask Detector"))
        self.image_label.setText(_translate("MainMenu", "Select a Camera"))
        self.take_photo_button.setText(_translate("MainMenu", "Capture"))
        self.start_menu_button.setText(_translate("MainMenu", "Sortir"))
        #self.epf.setText(_translate("MainMenu", "Test"))
        #self.camera_list_label.setText(_translate("MainMenu", "Camera Control Panel"))
        #item = self.camera_table.horizontalHeaderItem(0)
        #item.setText(_translate("MainMenu", "Camera"))
        #item = self.camera_table.horizontalHeaderItem(1)
        #item.setText(_translate("MainMenu", "Status"))
        self.camera_select_label.setText(_translate("MainMenu", "List cameras:    "))
        self.camera_select.setProperty("placeholderText", _translate("MainMenu", "Select Camera"))
        #self.epf.setText(_translate("MainMenu","AAAAAA"))
        self.pushButton1.setText(_translate("MainMenu", "Timer"))
        self.pushButton2.setText(_translate("MainMenu", "Statistiques"))
        self.pushButton3.setText(_translate("MainMenu", "Description du projet"))

        self.timer1.setText(_translate("MainMenu", "5 min"))
        self.timer2.setText(_translate("MainMenu", "10 min"))
        self.timer3.setText(_translate("MainMenu", "15 min"))