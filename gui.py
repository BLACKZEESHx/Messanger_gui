import sys

from PyQt5.QtCore import QPoint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget



class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.layout  = QVBoxLayout()
        self.layout.addWidget(MyBar(self))
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.addStretch(-1)
        self.setMinimumSize(800,400)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.pressing = False


class MyBar(QWidget):
    def __init__(self, parent):
        super(MyBar, self).__init__()
        self.parent = parent
        print(self.parent.width())
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.title = QLabel("My Own Bar")

        btn_size = 35

        self.btn_close = QPushButton("x")
        self.btn_close.clicked.connect(self.btn_close_clicked)
        self.btn_close.setFixedSize(btn_size,btn_size)
        self.btn_close.setStyleSheet("background-color: red;")

        self.btn_min = QPushButton("-")
        self.btn_min.clicked.connect(self.btn_min_clicked)
        self.btn_min.setFixedSize(btn_size, btn_size)
        self.btn_min.setStyleSheet("background-color: gray;")

        self.btn_max = QPushButton("+")
        self.btn_max.clicked.connect(self.btn_max_clicked)
        self.btn_max.setFixedSize(btn_size, btn_size)
        self.btn_max.setStyleSheet("background-color: gray;")

        self.title.setFixedHeight(35)
        self.title.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.title)
        self.layout.addWidget(self.btn_min)
        self.layout.addWidget(self.btn_max)
        self.layout.addWidget(self.btn_close)

        self.title.setStyleSheet("""
            background-color: black;
            color: white;
        """)
        self.setLayout(self.layout)

        self.start = QPoint(0, 0)
        self.pressing = False

    def resizeEvent(self, QResizeEvent):
        super(MyBar, self).resizeEvent(QResizeEvent)
        self.title.setFixedWidth(self.parent.width())

    def mousePressEvent(self, event):
        self.start = self.mapToGlobal(event.pos())
        self.pressing = True

    def mouseMoveEvent(self, event):
        if self.pressing:
            self.end = self.mapToGlobal(event.pos())
            self.movement = self.end-self.start
            self.parent.setGeometry(self.mapToGlobal(self.movement).x(),
                                self.mapToGlobal(self.movement).y(),
                                self.parent.width(),
                                self.parent.height())
            self.start = self.end

    def mouseReleaseEvent(self, QMouseEvent):
        self.pressing = False


    def btn_close_clicked(self):
        self.parent.close()

    def btn_max_clicked(self):
        self.parent.showMaximized()

    def btn_min_clicked(self):
        self.parent.showMinimized()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())
exit()
# Importing libraries
from write_type_animations import write_like_gpt
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtCore import Qt
import os
import threading
import socket
import pyautogui as auto_press
from message_scroll_label import Ui_Form
# Checking the size of the window
width, height = auto_press.size()

# Create a new window that will be the default window for the application
class MainWindow(QMainWindow):
    # initialization and updating screen
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Form()

        # Setting the stylesheet for the window
        self.setStyleSheet("""
        *{
            background-color: #313338;

        }
        """)

        # Making message lineedit that sends messages to user
        self.msg_input = QLineEdit(self)
        # Connecting to send message when we press "Enter" key
        self.msg_input.returnPressed.connect(self.show_send_message)

        # Setting the geometry of lineedit
        self.msg_input.setGeometry(
            int(width / 6), height - 140, width - 680, height - 723)
        # Setting the stylesheet for the lineedit
        self.msg_input.setStyleSheet("""

        *{
            border-radius: 3px;
            background-color: #383a40;
            color: white;

        }
        """)
        # Setting text left margin to make nicely aligned
        self.msg_input.setTextMargins(10, 0, 0, 0)
        # Setting "Message @Server" a placeholder of the lineedit
        self.msg_input.setPlaceholderText("Message @Server")
        # Creating the message viewer widget
        self.message_viewer = QWidget(self)
        # Setting message_viewer style sheet for now
        self.ui.setupUi(self.message_viewer)

        # Setting message_viewer Geometry size of message_viewer
        self.message_viewer.setGeometry(0, 0, width - 280, height - 142)

        # Set the margin of the message_viewer_label text
        self.ui.message_viewer_label.setMargin(100)

        # Making widget that displays how many users are there and show there username
        self.online_member_widget = QWidget(self)

        # Setting the geometry of online_member_amount_label
        self.online_member_widget.setGeometry(
            self.message_viewer.geometry().width(), 0, 280, height)
        # Setting the stylesheet for the online_member_amount_label

        # self.online_member_widget.setStyleSheet("background-color: #2b2d31;")

        # Create a label for the online_member_amount display
        self.online_member_label = QLabel(self.online_member_widget)

        # Change this value to client list index of online member
        self.online_member_amount = f""

        self.online_member_label.setText(
            f"{self.online_member_amount} Members")

        self.online_member_label.setGeometry(self.online_member_label.geometry().x(),
                                             self.online_member_label.geometry().y(),
                                             self.online_member_widget.geometry().width(),
                                             self.online_member_widget.geometry().height())

        self.online_member_label.setStyleSheet("color: #FFFFFF;")

        self.online_member_label.setContentsMargins(20, 0, 0, 700)
        self.ui.scrollArea.verticalScrollBar().setStyleSheet("""

QScrollBar:vertical
    {
        background-color: #2b2d35;
        width: 15px;
        margin: 2px 3px 2px 3px;
        border: 1px transparent #2b2d35;
        border-radius: 4px;
    }

    QScrollBar::handle:vertical
    {
        background-color: #1a1b1e;         /* #605F5F; */
        min-height: 5px;
        border-radius: 4px;
    }
    
    QScrollBar::sub-line:vertical
    {
        margin: 0px 0px 3px 0px;
        border-image: url(:/qss_icons/rc/up_arrow_disabled.png);
        height: 0px;
        width: 0px;
        subcontrol-position: top;
        subcontrol-origin: margin;
    }

    QScrollBar::add-line:vertical
    {
        margin: 0px 0px 0px 0px;
        border-image: url(:/qss_icons/rc/down_arrow_disabled.png);
        height: 0px;
        width: 0px;
        subcontrol-position: bottom;
        subcontrol-origin: margin;
    }


    QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical
    {
        background: none;
    }

    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical
    {
        background: none;
    }
""")
        self.ui.scrollArea.horizontalScrollBar().setStyleSheet("""

QScrollBar:horizontal
    {
        background-color: #2b2d35;
        width: 15px;
        margin: 2px 3px 2px 3px;
        border: 1px transparent #2b2d35;
        border-radius: 4px;
    }

    QScrollBar::handle:horizontal
    {
        background-color: #1a1b1e;         /* #605F5F; */
        min-height: 5px;
        border-radius: 4px;
    }



    QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal
    {
        background: none;
    }

    QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal
    {
        background: none;
    }

""")

    def show_send_message(self):
        self.ui.message_viewer_label.setText(
            self.ui.message_viewer_label.text() + username +": "+ self.msg_input.text() + "\n")
        messagegui = f"{username}: {self.msg_input.text()}"
        self.msg_input.setText("")


class messagerecvgui(MainWindow):
    def __init__(self):
        super().__init__()
        # while True:
        # self.messages = client.recv(1024).decode("utf-8")
        # self.ui.message_viewer_label.setText(self.messages)

# Creating function to run and show window
# decorator
# def show_window(func):
#     def mfx():
#         os.system("cls")
#         write_like_gpt("Showing window...", waite=0.030)
#         func()

#     return mfx


# @show_window
def app_runner():
    mapp = QApplication(sys.argv)
    window = MainWindow()
    window.showMaximized()
    # messagerecvguiobj = messagerecvgui()
    sys.exit(mapp.exec_())


# Running the application
app_runner()
