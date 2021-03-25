# QCalendarWidget - Estructura (Composicion de objetos)

Si bien este wiget ya se encuentran en el repositorio [`Metodos y eventos (Widgets PyQT)`](https://github.com/ALEX7320/documentacionpyqt "Metodos y eventos (Widgets PyQT)") se encuentra nuevamente aqui para encontrarlo con mayor facilidad, debido a que la composición del QCalendarWidget es muy peculiar.

**Fuentes**
 * [ProgrammerSought](https://www.programmersought.com/article/76123739163/ "ProgrammerSought")
 * [Stackoverflow](https://stackoverflow.com/questions/58911972/qcalendarwidget-on-year-click-using-pyqt5 "Stackoverflow") 
 
**Indice**

  * [Recursos utilizados](#recursos-utilizados)
  * [Ditribución](#ditribución)
  * [Previsualización](#previsualización)

# Recursos utilizados

`pip install PySide2`

# Ditribución

| Nombre  | Objeto  |Función|
| :------------: | :------------: | :------------: |
|"qt_calendar_prevmonth"   | QToolButton|Mes anterior|
|"qt_calendar_nextmonth"   | QToolButton|Mes siguiente|
|"qt_calendar_monthbutton"|QToolButton|Selección de mes|
|"qt_calendar_yearedit"|QSpinBox|Seleccíon de año|
|"qt_calendar_calendarview"|QTableView|Vista y Scroll del calendario|

# Previsualización

![](https://1.bp.blogspot.com/-09bpn1yb6sQ/YE_Zsa2mCTI/AAAAAAAAAGo/1MKOVyG1JP8uk49mKFq4erQbpPeHBZe7gCLcBGAsYHQ/s1600/6124614242.jpg)