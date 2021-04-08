import os
import sys

from PyQt5.QtWidgets import QApplication, QAbstractItemView, QMessageBox, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QDate, QTimer, Qt
from PyQt5 import uic, QtCore, QtGui
from lib import functions as fc
from lib import browser_functions as browser

# Version
version_info = "Shopify Automation App v0.0.1"


# Fix problem with macOs Big Sur
os.environ['QT_MAC_WANTS_LAYER'] = '1'
os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"

# LOAD UI FILES
main_ui = 'UI/main.ui'
main_form, main_base = uic.loadUiType(main_ui)


def show_warning_dialog(text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText(text)
    msg.exec_()


def show_info_dialog(text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText(text)
    msg.exec_()


def show_url_dialog(text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText(text)
    msg.setTextInteractionFlags(Qt.TextSelectableByMouse)
    msg.exec_()


def show_question_dialog(text):
    # def msg_button_click(i):
    #     print("Button clicked is:", i.text())
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Warning)
    msg_box.setText(text)
    msg_box.setWindowTitle("Warning")
    msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    # msg_box.buttonClicked.connect(msg_button_click)
    answer = False

    return_value = msg_box.exec()
    if return_value == QMessageBox.Ok:
        answer = True
    return answer


def copy_to_clipboard(text):
    cb = QApplication.clipboard()
    cb.clear(mode=cb.Clipboard)
    cb.setText(text, mode=cb.Clipboard)
    show_info_dialog("Text copied to the clipboard")


def clear_list_widget(list_widget):
    for i in range(list_widget.count()):
        item = list_widget.item(i)
        item.setSelected(False)


class MainPage(main_base, main_form):
    def __init__(self):
        super(main_base, self).__init__()
        self.setupUi(self)
        logo_img_path = fc.resources_project_path("logo_full.png")
        logo_pixmap = QPixmap(logo_img_path)
        self.mainLogo.setPixmap(logo_pixmap)

        self.makeProductsBtn.clicked.connect(self.make_products_available)
        self.makeCollectionsBtn.clicked.connect(self.make_products_available)

    def make_products_available(self):
        email = self.emailLine.text()
        password = self.passwordLine.text()
        store_url = self.storeUrlLine.text()
        if fc.email_check(email) and password != "" and store_url != "":
            browser.shopify_make_all_products_available_to_all_channels(store_url, email, password)
            show_info_dialog("Products are available now for all channels")
        else:
            show_warning_dialog("Please verify the inserted data!")

    def make_collections_available(self):
        email = self.emailLine.text()
        password = self.passwordLine.text()
        store_url = self.storeUrlLine.text()
        if fc.email_check(email) and password != "" and store_url != "":
            browser.shopify_make_all_collections_available_to_all_channels(store_url, email, password)
            show_info_dialog("Collections are available now for all channels")
        else:
            show_warning_dialog("Please verify the inserted data!")

    def test_mode(self):
        email = self.emailLine.text()
        password = self.passwordLine.text()
        store_url = self.storeUrlLine.text()
        if fc.email_check(email) and password != "" and store_url != "":
            browser.shopify_buy_products_automatically_bogus_test_mode(store_url, email, password, password)
            show_info_dialog("Store tested")
        else:
            show_warning_dialog("Please verify the inserted data!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mp = MainPage()
    mp.show()
    sys.exit(app.exec_())
