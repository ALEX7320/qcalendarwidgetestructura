# modulos de PySide2 utilizados
from PySide2.QtWidgets import QApplication,QMainWindow,QToolButton,QSpinBox,QTableView
from PySide2.QtCore import QEvent

# importar diseño
from view.ui_calendario import Ui_Calendario

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()

        self.raiz = Ui_Calendario()
        self.raiz.setupUi(self)

        # boton mes previo *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.btnCalPrev = self.raiz.calendario.findChild(QToolButton, "qt_calendar_prevmonth")
        self.btnCalPrev.clicked.connect(lambda: print('cal btn mesPrev'))

        # boton mes siguiente *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.btnCalNext = self.raiz.calendario.findChild(QToolButton, "qt_calendar_nextmonth")
        self.btnCalNext.clicked.connect(lambda aa: print('cal btn mesNext'))

        # boton seleccion mes *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.btnCalMes = self.raiz.calendario.findChild(QToolButton, "qt_calendar_monthbutton")
        self.btnCalMes.triggered.connect(lambda elemento:print('cal btn Mes',elemento.text()))

        # spinbox seleccion año *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.spinCalYear = self.raiz.calendario.findChild(QSpinBox, "qt_calendar_yearedit")
        self.spinCalYear.valueChanged.connect(lambda year: print('cal spin Año',year))

        # bloquear envento scroll en calendario (p1) *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.scrollcalen = self.raiz.calendario.findChild(QTableView, "qt_calendar_calendarview")
        self.scrollcalen.viewport().installEventFilter(self)

    def eventFilter(self, obj, event):
        # bloquear envento scroll en calendario (p2) 
        # scroll de qcalendar widgets (bloquear evento scroll)
        if(obj is self.scrollcalen.viewport() and event.type() == QEvent.Wheel):
            return True
        else:
            return super(VentanaPrincipal, self).eventFilter(obj, event)

if __name__ == "__main__":

    import sys

    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())
