import sys
from functools import partial
from PySide.QtGui import *
from PySide.QtCore import *
from SteganographyGUI import *
from scipy.misc import *
from Steganography import *


class Consumer(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Consumer, self).__init__(parent)
        self.setupUi(self)
        self.chkApplyCompression.setEnabled(False)
        self.chkApplyCompression.setChecked(False)
        self.chkApplyCompression.stateChanged.connect(self.enable_slider)
        self.chkOverride.stateChanged.connect(self.check_embed)
        self.slideCompression.valueChanged.connect(self.update_compress)
        self.btnSave.clicked.connect(self.save_file)
        self.btnClean.clicked.connect(self.clean_carrier2)
        self.btnExtract.clicked.connect(self.extract_carrier2)

        views = [self.viewPayload1, self.viewCarrier1, self.viewCarrier2]

        for view in views:
            view.dragEnterEvent = self.accept_event
            view.dropEvent = partial(self.processDrop, view)

    def accept_event(self, event):
        event.accept()

    def enable_slider(self):
        if self.slideCompression.isEnabled():
            self.slideCompression.setEnabled(False)
            self.payload1 = Payload(self.payload1_img)
            self.txtPayloadSize.setText(str(self.payload1.content.size))
            self.check_embed()
        else:
            self.slideCompression.setEnabled(True)
            self.update_compress()

    def update_compress(self):
        comp_lvl = self.slideCompression.value()
        self.txtCompression.setText(str(comp_lvl))
        self.payload1 = Payload(self.payload1_img,compressionLevel=comp_lvl)
        self.txtPayloadSize.setText(str(self.payload1.content.size))
        self.check_embed()


    def processDrop(self,view,event):
        mime = event.mimeData()
        if not mime.hasUrls():
            return
        filePath = mime.urls()[0].toLocalFile()
        ext = filePath[-3:]
        if not ext =="png":
            return

        scene = QGraphicsScene()
        pixMap = QPixmap(filePath)
        scene.addPixmap(pixMap)
        scene.dragMoveEvent = self.accept_event

        view.setScene(scene)
        view.fitInView(scene.sceneRect(), Qt.KeepAspectRatio)
        view.show()

        if view is self.viewPayload1:
            self.setup_payload1(filePath)
        elif view is self.viewCarrier1:
            self.setup_carrier1(filePath)
        else:
            self.carrier2_filePath = filePath
            self.setup_carrier2()


    def setup_payload1(self,filePath):
        self.chkApplyCompression.setEnabled(True)
        self.chkApplyCompression.setChecked(False)
        self.slideCompression.setValue(0)
        self.slideCompression.setEnabled(False)
        self.txtCompression.setEnabled(False)
        self.txtCompression.setText("0")
        self.payload1_img = imread(filePath)
        self.payload1 = Payload(self.payload1_img)
        self.txtPayloadSize.setText(str(self.payload1.content.size))
        self.check_embed()

    def setup_carrier1(self,filePath):
        self.chkOverride.setChecked(False)
        self.carrier1_img = imread(filePath)
        self.carrier1 = Carrier(self.carrier1_img)
        self.txtCarrierSize.setText(str(int(self.carrier1_img.size/3)))
        if self.carrier1.payloadExists():
            self.chkOverride.setEnabled(True)
            self.lblPayloadFound.setText(">>>>Payload Found<<<<")
        else:
            self.chkOverride.setEnabled(False)
            self.lblPayloadFound.setText("")
        self.check_embed()

    def setup_carrier2(self):
        self.viewPayload2.setScene(None)
        self.carrier2_img = imread(self.carrier2_filePath)
        self.carrier2 = Carrier(self.carrier2_img)
        if self.carrier2.payloadExists():
            self.btnClean.setEnabled(True)
            self.btnExtract.setEnabled(True)
            self.lblCarrierEmpty.setText("")
        else:
            self.lblCarrierEmpty.setText(">>>>Carrier Empty<<<<")
            self.btnClean.setEnabled(False)
            self.btnExtract.setEnabled(False)

    def check_embed(self):
        try:
            if self.payload1 is not None and self.carrier1 is not None:
                if self.payload1.content.size <= self.carrier1_img.size/3:
                    if not self.chkOverride.isEnabled():
                        self.btnSave.setEnabled(True)
                    elif self.chkOverride.isChecked():
                        self.btnSave.setEnabled(True)
                    else:
                        self.btnSave.setEnabled(False)
                else:
                    self.btnSave.setEnabled(False)
            else:
                self.btnSave.setEnabled(False)
        except:
            pass

    def save_file(self):
        new_carrier = self.carrier1.embedPayload(self.payload1,override=True)
        f_name,_ = QFileDialog.getSaveFileName(self)
        if f_name[-4:] != ".png":
            f_name += ".png"
        imsave(f_name,new_carrier)

    def clean_carrier2(self):
        cleaned_carrier = self.carrier2.clean()
        imsave(self.carrier2_filePath,cleaned_carrier)
        self.setup_carrier2()

    def extract_carrier2(self):
        exted_img = self.carrier2.extractPayload().img
        height, width, _ = exted_img.shape
        qimg = QImage(exted_img,width,height,width*3,QImage.Format_RGB888)
        scene = QGraphicsScene()
        scene.addPixmap(QPixmap(qimg))
        self.viewPayload2.setScene(scene)
        self.viewPayload2.fitInView(scene.sceneRect(), Qt.KeepAspectRatio)
        self.viewPayload2.show()




if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = Consumer()

    currentForm.show()
    currentApp.exec_()

