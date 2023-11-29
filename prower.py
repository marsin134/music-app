import sys
import io
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtMultimedia
from PyQt5 import uic
from random import choice

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>420</width>
    <height>429</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="playBtn">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>240</y>
      <width>111</width>
      <height>91</height>
     </rect>
    </property>
    <property name="text">
     <string>Старт</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pauseBtn">
    <property name="geometry">
     <rect>
      <x>160</x>
      <y>290</y>
      <width>111</width>
      <height>91</height>
     </rect>
    </property>
    <property name="text">
     <string>Пауза</string>
    </property>
   </widget>
   <widget class="QPushButton" name="stopBtn">
    <property name="geometry">
     <rect>
      <x>290</x>
      <y>240</y>
      <width>111</width>
      <height>91</height>
     </rect>
    </property>
    <property name="text">
     <string>Стоп</string>
    </property>
   </widget>
   <widget class="QPushButton" name="randomBtn">
    <property name="geometry">
     <rect>
      <x>170</x>
      <y>200</y>
      <width>91</width>
      <height>71</height>
     </rect>
    </property>
    <property name="text">
     <string>random</string>
    </property>
   </widget>
   <widget class="QPushButton" name="ringtonBtn">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>10</y>
      <width>91</width>
      <height>71</height>
     </rect>
    </property>
    <property name="text">
     <string>🤵</string>
    </property>
   </widget>
   <widget class="QPushButton" name="zerepahaBtn">
    <property name="geometry">
     <rect>
      <x>110</x>
      <y>10</y>
      <width>91</width>
      <height>71</height>
     </rect>
    </property>
    <property name="text">
     <string>🐢</string>
    </property>
   </widget>
   <widget class="QPushButton" name="xozehBtn">
    <property name="geometry">
     <rect>
      <x>210</x>
      <y>10</y>
      <width>91</width>
      <height>71</height>
     </rect>
    </property>
    <property name="text">
     <string>🥪</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>320</x>
      <y>10</y>
      <width>91</width>
      <height>71</height>
     </rect>
    </property>
    <property name="text">
     <string>🍕</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_2">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>90</y>
      <width>91</width>
      <height>71</height>
     </rect>
    </property>
    <property name="text">
     <string>🔫</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_3">
    <property name="geometry">
     <rect>
      <x>110</x>
      <y>90</y>
      <width>91</width>
      <height>71</height>
     </rect>
    </property>
    <property name="text">
     <string>💰</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_4">
    <property name="geometry">
     <rect>
      <x>210</x>
      <y>90</y>
      <width>91</width>
      <height>71</height>
     </rect>
    </property>
    <property name="text">
     <string>😑</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_5">
    <property name="geometry">
     <rect>
      <x>320</x>
      <y>90</y>
      <width>91</width>
      <height>71</height>
     </rect>
    </property>
    <property name="text">
     <string>👨‍🚀</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>420</width>
     <height>22</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.music = ['0.mp3', '1.mp3', '2.mp3', '3.mp3', '4.mp3', '5.mp3', '6.mp3', '7.mp3']
        self.ringtonBtn.clicked.connect(self.rington)
        self.zerepahaBtn.clicked.connect(self.zerepaha)
        self.xozehBtn.clicked.connect(self.xozeh)
        self.randomBtn.clicked.connect(self.randomi)
        self.pushButton.clicked.connect(self.pizza)
        self.pushButton_2.clicked.connect(self.pywka)
        self.pushButton_3.clicked.connect(self.xozy)
        self.pushButton_4.clicked.connect(self.ne_xozy)
        self.pushButton_5.clicked.connect(self.musika)

    def rington(self):
        self.load_mp3('music/0.mp3')
        self.run()

    def zerepaha(self):
        self.load_mp3(f'music/{self.music[1]}')
        self.run()

    def xozeh(self):
        self.load_mp3(f'music/{self.music[2]}')
        self.run()

    def pizza(self):
        self.load_mp3(f'music/{self.music[3]}')
        self.run()

    def pywka(self):
        self.load_mp3(f'music/{self.music[4]}')
        self.run()

    def xozy(self):
        self.load_mp3(f'music/{self.music[5]}')
        self.run()

    def ne_xozy(self):
        self.load_mp3(f'music/{self.music[6]}')
        self.run()

    def musika(self):
        self.load_mp3(f'music/{self.music[7]}')
        self.run()

    def randomi(self):
        self.load_mp3(f'music/{choice(self.music)}')
        self.run()

    def load_mp3(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)

    def run(self):
        self.player.play()
        self.playBtn.clicked.connect(self.player.play)
        self.pauseBtn.clicked.connect(self.player.pause)
        self.stopBtn.clicked.connect(self.player.stop)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
