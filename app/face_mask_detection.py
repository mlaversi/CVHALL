import os
import sys
import cv2
import numpy as np
from pathlib import Path
from datetime import datetime
from PyQt5.QtCore import QTimer, QRegExp, Qt
from PyQt5.QtGui import QImage, QPixmap, QColor, QRegExpValidator
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QWidget, QMessageBox

from start_menu import *
from main_menu import *

LABELS = ["Mask", "Without Mask"]
COLORS = [[0, 255, 0], [0, 0, 255]]
weightsPath = "yolo_utils/yolov4-tiny-mask.weights"
configPath = "yolo_utils/yolov4-tiny-mask.cfg"
photo_path = "photos"
camera_list_path = "app/resources/camera_list.txt"
connect_log_path = "app/resources/connect_history.log"

photo_dir = Path(photo_path)
photo_dir.mkdir(parents=True, exist_ok=True)
cam_list_filename = Path(camera_list_path)
cam_list_filename.touch(exist_ok=True)
connect_log_filename = Path(connect_log_path)
connect_log_filename.touch(exist_ok=True)

# Tres imoprtant pour le reseau de neuronne
def create_detection_net(config_path, weights_path):
    net = cv2.dnn_DetectionModel(config_path, weights_path)
    net.setInputSize(416, 416)
    net.setInputScale(1.0 / 255)
    net.setInputSwapRB(True)
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
    net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
    return net

# Tres important pour obtenir la detection de masque
def get_processed_image(img, net, confThreshold, nmsThreshold):
    mask_count = 0
    nomask_count = 0
    classes, confidences, boxes = net.detect(img, confThreshold, nmsThreshold)#fonction de detection
    for cl, score, (left, top, width, height) in zip(classes, confidences, boxes):
        mask_count += (1 - cl[0])
        nomask_count += cl[0]
        start_point = (int(left), int(top)) #definie la taille et position du petit carre autour de la tete
        end_point = (int(left + width), int(top + height))
        color = COLORS[cl[0]] #definie la couleur du carre
        img = cv2.rectangle(img, start_point, end_point, color, 2)  #dessine le carre sur l'image 
        text = f'{LABELS[cl[0]]}: {score[0]:0.2f}'
        (test_width, text_height), baseline = cv2.getTextSize(text, cv2.FONT_ITALIC, 0.6, 1)
        end_point = (int(left + test_width + 2), int(top - text_height - 2))
        img = cv2.rectangle(img, start_point, end_point, color, -1)
        cv2.putText(img, text, start_point, cv2.FONT_ITALIC, 0.6, COLORS[1 - cl[0]], 1)  #ecrit les information de port du masque sur l'image
    ratio = nomask_count / (mask_count + nomask_count + 0.000001)
    
    if ratio >= 0.1 and nomask_count >= 3: #
        status = "Danger"
    elif ratio != 0 and np.isnan(ratio) is not True:
        status = "Attention"
    else:
        status = "Pas de danger"
    return img, status, mask_count, nomask_count


class Camera(QTimer):
    def __init__(self, camName, camID, confThreshold=0.4, nmsThreshold=0.4):
        super().__init__()
        self.camName = camName
        self.camID = camID
        self.confThreshold = confThreshold
        self.nmsThreshold = nmsThreshold
        self.viewable = False
        self.status = "pas de connection"
        self.prev_status = "pas de connection"
        self.last_image = None
        self.camera_name_item = QTableWidgetItem(self.camName)
        self.camera_name_item.setTextAlignment(Qt.AlignCenter)
        self.camera_status_item = QTableWidgetItem(self.status)
        self.camera_status_item.setTextAlignment(Qt.AlignCenter)
        self.cam = cv2.VideoCapture(self.camID)
        self.timeout.connect(self.camera_run)

    def start_camera(self):
        self.cam = cv2.VideoCapture(self.camID)
        self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)#attribu optionnel
        self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    def take_photo(self):
        today = datetime.now().strftime("%d.%m.%Y")
        photo_dir_today = Path(os.path.join(photo_path, today, self.status))
        photo_dir_today.mkdir(parents=True, exist_ok=True)
        image_name = self.camName + "_" + datetime.now().strftime("%d.%m.%Y_%H.%M.%S") + ".jpg"
        cv2.imwrite(os.path.join(photo_dir_today, image_name), self.last_image)

    def view_disconnected_cam(self):
        mainMenu.ui.image_label.setStyleSheet("color: rgb(210, 105, 30);")
        mainMenu.ui.image_label.setText(self.camName + " pas de connection")
        status_stylesheet = "border: transparent; background-color: transparent; font: 63 24pt \"URW Gothic L\"; color: rgb(210, 105, 30);"
        mainMenu.ui.image_label.setStyleSheet("color: rgb(210, 105, 30);")
        mainMenu.ui.image_label.setText(self.camName + " pas de connection")
        mainMenu.ui.mask_count_label.setText("")
        mainMenu.ui.no_mask_count_label.setText("")
        mainMenu.ui.status_label.setText('Status:')
        mainMenu.ui.status_type_label.setText(self.status)
        mainMenu.ui.status_type_label.setStyleSheet(status_stylesheet)

    def camera_run(self):
        if self.status != "pas de connection":
            try:
                ret, image = self.cam.read() #lecture de la camera
                self.last_image = image.copy()
                image, status, mask_count, nomask_count = get_processed_image(image, mainMenu.net, self.confThreshold, self.nmsThreshold) #recuperation de l'image avec la detection
                self.status = status
                if status == "Pas de danger": #changement de l'etat du text en fonction de l'etat de danger
                    self.camera_name_item.setForeground(QColor(21, 200, 8))
                    self.camera_status_item.setForeground(QColor(21, 200, 8))
                    status_stylesheet = "border: transparent; background-color: transparent; font: 63 24pt \"URW Gothic L\"; color: rgb(21, 200, 8);"
                elif status == "Attention":
                    self.camera_name_item.setForeground(QColor("yellow"))
                    self.camera_status_item.setForeground(QColor("yellow"))
                    status_stylesheet = "border: transparent; background-color: transparent; font: 63 24pt \"URW Gothic L\"; color: yellow;"
                else:
                    self.camera_name_item.setForeground(QColor("red"))
                    self.camera_status_item.setForeground(QColor("red"))
                    status_stylesheet = "border: transparent; background-color: transparent; font: 63 24pt \"URW Gothic L\"; color: red;"
                self.camera_status_item.setText(self.status)
                if self.viewable is True:
                    mainMenu.ui.image_label.setStyleSheet("color: rgb(255, 255, 255);")
                    mainMenu.ui.image_label.setText("Selectionnez une camera")
                    mainMenu.ui.mask_count_label.setText(f'Avec masque:  {mask_count}')
                    mainMenu.ui.no_mask_count_label.setText(f'Sans Masque:  {nomask_count}')
                    mainMenu.ui.status_label.setText('Status:')
                    mainMenu.ui.status_type_label.setText(status)
                    mainMenu.ui.status_type_label.setStyleSheet(status_stylesheet)
                    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                    height, width, channel = image.shape
                    step = channel * width
                    qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
                    mainMenu.ui.image_label.setPixmap(QPixmap.fromImage(qImg))
            except:
                with open(connect_log_path, "a") as connect_log:
                    connect_log.write(datetime.now().strftime("%d/%m/%Y - %H:%M:%S ->\t") + self.camName + " (ID: " + str(self.camID) + ") disconnected from the system.\n\n")
                self.status = "Not Connected"
                self.camera_name_item.setForeground(QColor(210, 105, 30))
                self.camera_status_item.setForeground(QColor(210, 105, 30))
                self.camera_status_item.setText(self.status)
                self.cam.release()
                if self.viewable is True:
                    self.view_disconnected_cam()

        else:
            self.cam = cv2.VideoCapture(self.camID)
            if self.cam.isOpened() and self.cam.get(cv2.CAP_PROP_FPS) != 0:
                with open(connect_log_path, "a") as connect_log:
                    connect_log.write(datetime.now().strftime("%d/%m/%Y - %H:%M:%S ->\t") + self.camName + " (ID: " + str(self.camID) + ") connected to the system.\n\n")
                self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
                self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
                self.status = "Safe"
            elif self.viewable is True:
                self.view_disconnected_cam()
        # automatically take a photo when the status of the camera switches to "Warning" or "Danger"
        # if self.prev_status == "Safe" or self.prev_status == "Not Connected":
        #     if self.status == "Warning" or self.status == "Danger":
        #         self.take_photo()
        # elif self.prev_status == "Warning" and self.status == "Danger":
        #     self.take_photo()
        # elif self.prev_status == "Danger" and self.status == "Warning":
        #     self.take_photo()
        # self.prev_status = self.status


class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainMenu()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('resources/medical-mask.ico'))
        #header = self.ui.camera_table.horizontalHeader()
        #header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        #header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.net = create_detection_net(configPath, weightsPath) #creation de la fonction de detection
        self.camera_list = []
        self.current_camera = None
        self.ui.camera_select.activated.connect(self.change_cam)
        self.ui.take_photo_button.clicked.connect(self.take_photo)
        self.ui.start_menu_button.clicked.connect(self.close_app)

        self.button1 = QtWidgets.QLabel(self.centralwidget) # image
        self.button1.setGeometry(QtCore.QRect(0, 100, 1280, 720)) 
        self.button1.setText("")
        self.button1.setPixmap(QtGui.QPixmap("ressources/Logo_EPF.png"))
        self.button1.setScaledContents(True)
        self.button1.setObjectName("button1")

    def get_camera_list(self):
        self.camera_list = []
        self.ui.camera_select.clear()
        #self.ui.camera_table.clearContents()
        #self.ui.camera_table.setRowCount(0)
        self.ui.image_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.ui.image_label.setText("Selectionnez une camera")
        for camera in startMenu.camera_dict:
            self.camera_list.append(Camera(camera, startMenu.camera_dict[camera]))
        for camera in self.camera_list:
            self.ui.camera_select.addItem(camera.camName)
            #self.ui.camera_table.insertRow(self.ui.camera_table.rowCount())
            #current_row = self.ui.camera_table.rowCount() - 1
            #self.ui.camera_table.setItem(current_row, 0, camera.camera_name_item)
            #self.ui.camera_table.setItem(current_row, 1, camera.camera_status_item)

    def start_cameras(self):
        for camera in self.camera_list:
            camera.start_camera()
            camera.start(30)

    def stop_cameras(self):
        for camera in self.camera_list:
            camera.stop()
            camera.cam.release()

    def change_cam(self, i):
        self.current_camera = self.camera_list[i]
        for camera in self.camera_list:
            camera.viewable = False
        self.current_camera.viewable = True

    def take_photo(self):
        if self.current_camera is not None and self.current_camera.status != "pas de connection":
            image_name = self.current_camera.camName + "_" + datetime.now().strftime("%d.%m.%Y_%H.%M.%S") + ".jpg"
            cv2.imwrite(os.path.join(photo_path, image_name), self.current_camera.last_image)
            QTimer.singleShot(0, lambda: self.ui.photo_taken_notification.setText("Photo prise!"))
        else:
            QTimer.singleShot(0, lambda: self.ui.photo_taken_notification.setText("Camera non disponible!"))
        QTimer.singleShot(2000, lambda: self.ui.photo_taken_notification.setText(""))

    # def open_start_menu(self):
    #     self.hide()
    #     self.stop_cameras()
    #     startMenu.get_camera_list(cam_list_filename)
    #     startMenu.show()
    #   
    def close_app(self):
        self.stop_cameras()
        self.close()
         



class StartMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_StartMenu()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())
        self.setWindowIcon(QtGui.QIcon('resources/medical-mask.ico'))
        header = self.ui.camera_table.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.ui.add_cam_button.clicked.connect(self.open_new_cam_menu)
        self.ui.main_menu_button.clicked.connect(self.open_main_menu)
        self.ui.exit_button.clicked.connect(self.close_app)
        self.ui.delete_cam_button.clicked.connect(self.delete_cam)
        self.ui.camera_table.cellDoubleClicked.connect(self.show_cam_info)
        self.camera_dict = {}
        self.get_camera_list(cam_list_filename)

    def insert_dict_in_table(self):
        for camera in self.camera_dict:
            self.ui.camera_table.insertRow(self.ui.camera_table.rowCount())
            current_row = self.ui.camera_table.rowCount() - 1
            cam_name = QTableWidgetItem(camera)
            cam_name.setTextAlignment(Qt.AlignCenter)
            self.ui.camera_table.setItem(current_row, 0, cam_name)
            cam_id = QTableWidgetItem(str(self.camera_dict[camera]))
            cam_id.setTextAlignment(Qt.AlignCenter)
            self.ui.camera_table.setItem(current_row, 1, cam_id)

    def get_camera_list(self, cam_list_filename):
        self.camera_dict = {}
        self.ui.camera_table.clearContents()
        self.ui.camera_table.setRowCount(0)
        for cam_line in [cam_line.strip() for cam_line in open(cam_list_filename)]:
            if cam_line.split(" ")[1].isdigit():
                self.camera_dict[cam_line.split(" ")[0]] = int(cam_line.split(" ")[1])
            else:
                self.camera_dict[cam_line.split(" ")[0]] = cam_line.split(" ")[1]
        self.insert_dict_in_table()

    def update_camera_list(self, cam_list_filename):
        self.ui.camera_table.clearContents()
        self.ui.camera_table.setRowCount(0)
        self.insert_dict_in_table()
        cam_file = open(cam_list_filename, "w")
        for camera in self.camera_dict:
            cam_file.write(camera + " " + str(self.camera_dict[camera]) + "\n")

    def open_new_cam_menu(self):
        newCameraMenu.refresh_menu()
        newCameraMenu.show()

    def delete_cam(self):
        if self.ui.camera_table.currentRow() > -1:
            selected_row = self.ui.camera_table.currentRow()
            del self.camera_dict[self.ui.camera_table.item(selected_row, 0).text()]
            self.ui.camera_table.removeRow(selected_row)
            self.update_camera_list(cam_list_filename)

    def show_cam_info(self):
        current_row = self.ui.camera_table.currentRow()
        camera_name = self.ui.camera_table.item(current_row, 0).text()
        camera_id = self.ui.camera_table.item(current_row, 1).text()
        info = QMessageBox(QMessageBox.Information, camera_name + " Info", "Camera Name:\t" + camera_name + "\nCamera ID:\t" + camera_id)
        info.setWindowIcon(QtGui.QIcon("resources/medical-mask.ico"))
        info.setStyleSheet("background-color: rgb(15, 50, 80); color: #32CD32; font: 75 13pt \"Gill Sans MT\";")
        info.exec_()

    def open_main_menu(self):
        self.hide()
        mainMenu.current_camera = None
        mainMenu.ui.mask_count_label.setText("")
        mainMenu.ui.no_mask_count_label.setText("")
        mainMenu.ui.status_label.setText("")
        mainMenu.ui.status_type_label.setText("")
        mainMenu.get_camera_list()
        mainMenu.showMaximized()
        mainMenu.start_cameras()

    def close_app(self):
        self.close()
        mainMenu.close()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    startMenu = StartMenu()
    mainMenu = MainMenu()
    #startMenu.show()
    mainMenu.get_camera_list()
    mainMenu.showMaximized()
    mainMenu.start_cameras()

    mainMenu.show()

    mainMenu.change_cam(0)

    sys.exit(app.exec_())