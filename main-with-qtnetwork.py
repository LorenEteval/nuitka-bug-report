from PySide6 import QtCore
from PySide6.QtWidgets import *
from PySide6.QtNetwork import *

import functools


def handleFinishedByNetworkReply(networkReply):
    print('finished')


app = QApplication()

manager = QNetworkAccessManager()
reply = manager.get(QNetworkRequest(QtCore.QUrl('http://cp.cloudflare.com/')))
reply.finished.connect(
    functools.partial(
        handleFinishedByNetworkReply,
        reply,
    )
)

window = QMainWindow()
window.show()

app.exec()
