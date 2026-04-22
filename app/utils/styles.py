APP_STYLE = """
QWidget {
    background-color: #F4F4F5;
    color: #111111;
    font-family: Roboto, Arial, sans-serif;
    font-size: 13px;
}

QMainWindow {
    background-color: #F4F4F5;
}

QLabel {
    color: #111111;
    background: transparent;
}

QLabel#pageTitle {
    font-size: 30px;
    font-weight: 700;
    color: #111111;
}

QLabel#sectionTitle {
    font-size: 14px;
    font-weight: 600;
    color: #555555;
}

QLabel#metricValue {
    font-size: 28px;
    font-weight: 800;
    color: #C91843;
}

QLineEdit {
    background-color: white;
    border: 1px solid #D4D4D8;
    border-radius: 10px;
    padding: 12px;
    color: #111111;
}

QLineEdit:focus {
    border: 2px solid #C91843;
}

QPushButton {
    background-color: #C91843;
    color: white;
    border: none;
    border-radius: 10px;
    padding: 12px 14px;
    font-weight: 700;
}

QPushButton:hover {
    background-color: #9B1B39;
}

QPushButton:pressed {
    background-color: #870027;
}

QPushButton#menuButton {
    background-color: transparent;
    color: #F5F5F5;
    border: 1px solid transparent;
    border-radius: 10px;
    text-align: left;
    padding: 12px 14px;
    font-weight: 700;
}

QPushButton#menuButton:hover {
    background-color: #1F1F1F;
    border: 1px solid #2A2A2A;
}

QPushButton#menuButton:checked {
    background-color: #C91843;
    color: white;
}

QWidget#sidebar {
    background-color: #111111;
}

QFrame#logoCard {
    background-color: #18181B;
    border: 1px solid #27272A;
    border-radius: 14px;
}

QLabel#brandTitle {
    color: white;
    font-size: 20px;
    font-weight: 800;
}

QLabel#brandSubtitle {
    color: #D4D4D8;
    font-size: 12px;
}

QLabel#sidebarUser {
    color: #D4D4D8;
    font-size: 12px;
}

QFrame#card {
    background-color: white;
    border: 1px solid #E4E4E7;
    border-radius: 16px;
}

QTableWidget {
    background-color: white;
    border: 1px solid #E4E4E7;
    border-radius: 12px;
    gridline-color: #F1F1F1;
    selection-background-color: #C91843;
    selection-color: white;
}

QHeaderView::section {
    background-color: #111111;
    color: white;
    padding: 10px;
    border: none;
    font-weight: 700;
}
QTableWidget {
    background-color: white;
    border: 1px solid #E4E4E7;
    border-radius: 12px;
    gridline-color: transparent;
    selection-background-color: #C91843;
    selection-color: white;
    padding: 6px;
}

QTableWidget::item {
    padding: 8px;
}

QScrollBar:vertical {
    background: #F1F1F1;
    width: 12px;
    margin: 0px;
    border-radius: 6px;
}

QScrollBar::handle:vertical {
    background: #C91843;
    min-height: 25px;
    border-radius: 6px;
}

QScrollBar::handle:vertical:hover {
    background: #9B1B39;
}

QScrollBar::add-line:vertical,
QScrollBar::sub-line:vertical {
    height: 0px;
}

QScrollBar:horizontal {
    background: #F1F1F1;
    height: 12px;
    margin: 0px;
    border-radius: 6px;
}

QScrollBar::handle:horizontal {
    background: #C91843;
    min-width: 25px;
    border-radius: 6px;
}

QScrollBar::handle:horizontal:hover {
    background: #9B1B39;
}

QScrollBar::add-line:horizontal,
QScrollBar::sub-line:horizontal {
    width: 0px;
}
"""