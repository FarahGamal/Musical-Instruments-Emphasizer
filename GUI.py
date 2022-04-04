# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\spring22\SBEN311\task#3\GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Slider(QtWidgets.QSlider):
    def mousePressEvent(self, event):
        super(Slider, self).mousePressEvent(event)
        if event.button() == QtCore.Qt.LeftButton:
            val = self.pixelPosToRangeValue(event.pos())
            self.setValue(val)

    def pixelPosToRangeValue(self, pos):
        opt = QtWidgets.QStyleOptionSlider()
        self.initStyleOption(opt)
        gr = self.style().subControlRect(QtWidgets.QStyle.CC_Slider, opt, QtWidgets.QStyle.SC_SliderGroove, self)
        sr = self.style().subControlRect(QtWidgets.QStyle.CC_Slider, opt, QtWidgets.QStyle.SC_SliderHandle, self)

        if self.orientation() == QtCore.Qt.Horizontal:
            sliderLength = sr.width()
            sliderMin = gr.x()
            sliderMax = gr.right() - sliderLength + 1
        else:
            sliderLength = sr.height()
            sliderMin = gr.y()
            sliderMax = gr.bottom() - sliderLength + 1;
        pr = pos - sr.center() + sr.topLeft()
        p = pr.x() if self.orientation() == QtCore.Qt.Horizontal else pr.y()
        return QtWidgets.QStyle.sliderValueFromPosition(self.minimum(), self.maximum(), p - sliderMin,
                                               sliderMax - sliderMin, opt.upsideDown)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1497, 922)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MainTabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.MainTabWidget.setGeometry(QtCore.QRect(10, 0, 1471, 871))
        self.MainTabWidget.setStyleSheet("")
        self.MainTabWidget.setObjectName("MainTabWidget")
        self.PlayerAndEmphasizerTab = QtWidgets.QWidget()
        self.PlayerAndEmphasizerTab.setObjectName("PlayerAndEmphasizerTab")
        self.gridLayoutWidget = QtWidgets.QWidget(self.PlayerAndEmphasizerTab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 1431, 401))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.SongSpectrogramGridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.SongSpectrogramGridLayout.setContentsMargins(0, 0, 0, 0)
        self.SongSpectrogramGridLayout.setObjectName("SongSpectrogramGridLayout")
        self.SongGraphGraphicsView = PlotWidget(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SongGraphGraphicsView.sizePolicy().hasHeightForWidth())
        self.SongGraphGraphicsView.setSizePolicy(sizePolicy)
        self.SongGraphGraphicsView.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.SongGraphGraphicsView.setObjectName("SongGraphGraphicsView")
        self.SongSpectrogramGridLayout.addWidget(self.SongGraphGraphicsView, 1, 0, 1, 1)
        self.SongGraphTextLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.SongGraphTextLabel.setFont(font)
        self.SongGraphTextLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.SongGraphTextLabel.setObjectName("SongGraphTextLabel")
        self.SongSpectrogramGridLayout.addWidget(self.SongGraphTextLabel, 0, 0, 1, 1)
        self.SpectrogramGraphGraphicsView = PlotWidget(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SpectrogramGraphGraphicsView.sizePolicy().hasHeightForWidth())
        self.SpectrogramGraphGraphicsView.setSizePolicy(sizePolicy)
        self.SpectrogramGraphGraphicsView.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.SpectrogramGraphGraphicsView.setObjectName("SpectrogramGraphGraphicsView")
        self.SongSpectrogramGridLayout.addWidget(self.SpectrogramGraphGraphicsView, 1, 1, 1, 1)
        self.SpectrogramGraphTextLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.SpectrogramGraphTextLabel.setFont(font)
        self.SpectrogramGraphTextLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.SpectrogramGraphTextLabel.setObjectName("SpectrogramGraphTextLabel")
        self.SongSpectrogramGridLayout.addWidget(self.SpectrogramGraphTextLabel, 0, 1, 1, 1)
        self.PlayPauseVolumeGridLayout = QtWidgets.QGridLayout()
        self.PlayPauseVolumeGridLayout.setObjectName("PlayPauseVolumeGridLayout")
        self.VolumeIconPushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.VolumeIconPushButton.setStyleSheet("QPushButton{\n"
"border-radius:20px;\n"
"    \n"
"}")
        self.VolumeIconPushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/speaker-filled-audio-tool.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.VolumeIconPushButton.setIcon(icon)
        self.VolumeIconPushButton.setObjectName("VolumeIconPushButton")
        self.PlayPauseVolumeGridLayout.addWidget(self.VolumeIconPushButton, 0, 2, 1, 1)
        self.PlayPushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.PlayPushButton.setStyleSheet("QPushButton{\n"
"border-radius:20px;\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
" background-color: rgb(229,229,229);\n"
"}\n"
"")
        self.PlayPushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PlayPushButton.setIcon(icon1)
        self.PlayPushButton.setObjectName("PlayPushButton")
        self.PlayPauseVolumeGridLayout.addWidget(self.PlayPushButton, 0, 0, 1, 1)
        self.PausePushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.PausePushButton.setStyleSheet("QPushButton{\n"
"border-radius:20px;\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
" background-color: rgb(229,229,229);\n"
"}\n"
"")
        self.PausePushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PausePushButton.setIcon(icon2)
        self.PausePushButton.setObjectName("PausePushButton")
        self.PlayPauseVolumeGridLayout.addWidget(self.PausePushButton, 0, 1, 1, 1)
        self.VolumeUpDownHorizontalSlider = Slider(self.gridLayoutWidget)
        self.VolumeUpDownHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.VolumeUpDownHorizontalSlider.setObjectName("VolumeUpDownHorizontalSlider")
        self.PlayPauseVolumeGridLayout.addWidget(self.VolumeUpDownHorizontalSlider, 0, 3, 1, 1)
        self.SongSpectrogramGridLayout.addLayout(self.PlayPauseVolumeGridLayout, 2, 0, 1, 1)
        self.InstrumentEmphasizerGroupBox = QtWidgets.QGroupBox(self.PlayerAndEmphasizerTab)
        self.InstrumentEmphasizerGroupBox.setGeometry(QtCore.QRect(20, 420, 1431, 401))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        self.InstrumentEmphasizerGroupBox.setFont(font)
        self.InstrumentEmphasizerGroupBox.setObjectName("InstrumentEmphasizerGroupBox")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.InstrumentEmphasizerGroupBox)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(12, 32, 1411, 361))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.InstrumentEmphasizerGridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.InstrumentEmphasizerGridLayout.setContentsMargins(0, 0, 0, 0)
        self.InstrumentEmphasizerGridLayout.setObjectName("InstrumentEmphasizerGridLayout")
        self.BassMaximumFrequencyTextLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.BassMaximumFrequencyTextLabel.setFont(font)
        self.BassMaximumFrequencyTextLabel.setObjectName("BassMaximumFrequencyTextLabel")
        self.InstrumentEmphasizerGridLayout.addWidget(self.BassMaximumFrequencyTextLabel, 0, 0, 1, 1)
        self.TromboneTitelLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.TromboneTitelLabel.setObjectName("TromboneTitelLabel")
        self.InstrumentEmphasizerGridLayout.addWidget(self.TromboneTitelLabel, 4, 1, 1, 1)
        self.E_FlatClarinetMaximumFrequencyTextLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.E_FlatClarinetMaximumFrequencyTextLabel.setFont(font)
        self.E_FlatClarinetMaximumFrequencyTextLabel.setObjectName("E_FlatClarinetMaximumFrequencyTextLabel")
        self.InstrumentEmphasizerGridLayout.addWidget(self.E_FlatClarinetMaximumFrequencyTextLabel, 0, 2, 1, 1)
        self.E_FlatClarinetTitelLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.E_FlatClarinetTitelLabel.setObjectName("E_FlatClarinetTitelLabel")
        self.InstrumentEmphasizerGridLayout.addWidget(self.E_FlatClarinetTitelLabel, 4, 2, 1, 1)
        self.BassGainValueTextLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.BassGainValueTextLabel.setFont(font)
        self.BassGainValueTextLabel.setObjectName("BassGainValueTextLabel")
        self.InstrumentEmphasizerGridLayout.addWidget(self.BassGainValueTextLabel, 2, 0, 1, 1)
        self.TromboneGainValueTextLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.TromboneGainValueTextLabel.setFont(font)
        self.TromboneGainValueTextLabel.setObjectName("TromboneGainValueTextLabel")
        self.InstrumentEmphasizerGridLayout.addWidget(self.TromboneGainValueTextLabel, 2, 1, 1, 1)
        self.TromboneMaximumFrequencyTextLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.TromboneMaximumFrequencyTextLabel.setFont(font)
        self.TromboneMaximumFrequencyTextLabel.setObjectName("TromboneMaximumFrequencyTextLabel")
        self.InstrumentEmphasizerGridLayout.addWidget(self.TromboneMaximumFrequencyTextLabel, 0, 1, 1, 1)
        self.E_FlatClarinetGainValueTextLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.E_FlatClarinetGainValueTextLabel.setFont(font)
        self.E_FlatClarinetGainValueTextLabel.setObjectName("E_FlatClarinetGainValueTextLabel")
        self.InstrumentEmphasizerGridLayout.addWidget(self.E_FlatClarinetGainValueTextLabel, 2, 2, 1, 1)
        self.E_FlatClarinetImageLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.E_FlatClarinetImageLabel.setText("")
        self.E_FlatClarinetImageLabel.setPixmap(QtGui.QPixmap("D:\\spring22\\SBEN311\\task#3\\xxss.png"))
        self.E_FlatClarinetImageLabel.setObjectName("E_FlatClarinetImageLabel")
        self.InstrumentEmphasizerGridLayout.addWidget(self.E_FlatClarinetImageLabel, 3, 2, 1, 1)
        self.TromboneGainVerticalSlider = Slider(self.gridLayoutWidget_3)
        self.TromboneGainVerticalSlider.setMaximum(40)
        self.TromboneGainVerticalSlider.setProperty("value", 4)
        self.TromboneGainVerticalSlider.setSliderPosition(4)
        self.TromboneGainVerticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.TromboneGainVerticalSlider.setInvertedAppearance(False)
        self.TromboneGainVerticalSlider.setInvertedControls(False)
        self.TromboneGainVerticalSlider.setObjectName("TromboneGainVerticalSlider")
        self.InstrumentEmphasizerGridLayout.addWidget(self.TromboneGainVerticalSlider, 1, 1, 1, 1)
        self.TromboneImageLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.TromboneImageLabel.setText("")
        self.TromboneImageLabel.setPixmap(QtGui.QPixmap("D:\\spring22\\SBEN311\\task#3\\Musical-Instruments-Emphasizer/tromboneResize.png"))
        self.TromboneImageLabel.setObjectName("TromboneImageLabel")
        self.InstrumentEmphasizerGridLayout.addWidget(self.TromboneImageLabel, 3, 1, 1, 1)
        self.BassTitelLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.BassTitelLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.BassTitelLabel.setObjectName("BassTitelLabel")
        self.InstrumentEmphasizerGridLayout.addWidget(self.BassTitelLabel, 4, 0, 1, 1)
        self.BassGainVerticalSlider = Slider(self.gridLayoutWidget_3)
        self.BassGainVerticalSlider.setMaximum(40)
        self.BassGainVerticalSlider.setProperty("value", 4)
        self.BassGainVerticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.BassGainVerticalSlider.setObjectName("BassGainVerticalSlider")
        self.InstrumentEmphasizerGridLayout.addWidget(self.BassGainVerticalSlider, 1, 0, 1, 1)
        self.E_FlatClarinetGainVerticalSlider = Slider(self.gridLayoutWidget_3)
        self.E_FlatClarinetGainVerticalSlider.setMaximum(40)
        self.E_FlatClarinetGainVerticalSlider.setProperty("value", 4)
        self.E_FlatClarinetGainVerticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.E_FlatClarinetGainVerticalSlider.setObjectName("E_FlatClarinetGainVerticalSlider")
        self.InstrumentEmphasizerGridLayout.addWidget(self.E_FlatClarinetGainVerticalSlider, 1, 2, 1, 1)
        self.ViolaMaximumFrequencyTextLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.ViolaMaximumFrequencyTextLabel.setFont(font)
        self.ViolaMaximumFrequencyTextLabel.setObjectName("ViolaMaximumFrequencyTextLabel")
        self.InstrumentEmphasizerGridLayout.addWidget(self.ViolaMaximumFrequencyTextLabel, 0, 4, 1, 1)
        self.PiccoloMaximumFrequencyTextLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.PiccoloMaximumFrequencyTextLabel.setFont(font)
        self.PiccoloMaximumFrequencyTextLabel.setObjectName("PiccoloMaximumFrequencyTextLabel")
        self.InstrumentEmphasizerGridLayout.addWidget(self.PiccoloMaximumFrequencyTextLabel, 0, 3, 1, 1)
        self.BassImageLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.BassImageLabel.setText("")
        self.BassImageLabel.setPixmap(QtGui.QPixmap("D:\\spring22\\SBEN311\\task#3\\Musical-Instruments-Emphasizer/bass.png"))
        self.BassImageLabel.setScaledContents(False)
        self.BassImageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.BassImageLabel.setObjectName("BassImageLabel")
        self.InstrumentEmphasizerGridLayout.addWidget(self.BassImageLabel, 3, 0, 1, 1)
        self.ViolaTitelLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.ViolaTitelLabel.setObjectName("ViolaTitelLabel")
        self.InstrumentEmphasizerGridLayout.addWidget(self.ViolaTitelLabel, 4, 4, 1, 1)
        self.PiccoloGainValueTextLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.PiccoloGainValueTextLabel.setFont(font)
        self.PiccoloGainValueTextLabel.setObjectName("PiccoloGainValueTextLabel")
        self.InstrumentEmphasizerGridLayout.addWidget(self.PiccoloGainValueTextLabel, 2, 3, 1, 1)
        self.PiccoloGainVerticalSlider = Slider(self.gridLayoutWidget_3)
        self.PiccoloGainVerticalSlider.setMaximum(40)
        self.PiccoloGainVerticalSlider.setProperty("value", 4)
        self.PiccoloGainVerticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.PiccoloGainVerticalSlider.setObjectName("PiccoloGainVerticalSlider")
        self.InstrumentEmphasizerGridLayout.addWidget(self.PiccoloGainVerticalSlider, 1, 3, 1, 1)
        self.ViolaGainVerticalSlider = Slider(self.gridLayoutWidget_3)
        self.ViolaGainVerticalSlider.setMaximum(40)
        self.ViolaGainVerticalSlider.setProperty("value", 4)
        self.ViolaGainVerticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.ViolaGainVerticalSlider.setObjectName("ViolaGainVerticalSlider")
        self.InstrumentEmphasizerGridLayout.addWidget(self.ViolaGainVerticalSlider, 1, 4, 1, 1)
        self.PiccoloImageLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.PiccoloImageLabel.setText("")
        self.PiccoloImageLabel.setPixmap(QtGui.QPixmap("D:\\spring22\\SBEN311\\task#3\\Musical-Instruments-Emphasizer/piccoloPNG.png"))
        self.PiccoloImageLabel.setObjectName("PiccoloImageLabel")
        self.InstrumentEmphasizerGridLayout.addWidget(self.PiccoloImageLabel, 3, 3, 1, 1)
        self.ViolaGainValueTextLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.ViolaGainValueTextLabel.setFont(font)
        self.ViolaGainValueTextLabel.setObjectName("ViolaGainValueTextLabel")
        self.InstrumentEmphasizerGridLayout.addWidget(self.ViolaGainValueTextLabel, 2, 4, 1, 1)
        self.PiccoloTitelLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.PiccoloTitelLabel.setObjectName("PiccoloTitelLabel")
        self.InstrumentEmphasizerGridLayout.addWidget(self.PiccoloTitelLabel, 4, 3, 1, 1)
        self.ViolaImageLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.ViolaImageLabel.setText("")
        self.ViolaImageLabel.setPixmap(QtGui.QPixmap("D:\\spring22\\SBEN311\\task#3\\Musical-Instruments-Emphasizer/viola.png"))
        self.ViolaImageLabel.setObjectName("ViolaImageLabel")
        self.InstrumentEmphasizerGridLayout.addWidget(self.ViolaImageLabel, 3, 4, 1, 1)
        self.MainTabWidget.addTab(self.PlayerAndEmphasizerTab, "")
        self.VirtualMusicalInstrumnetsTab = QtWidgets.QWidget()
        self.VirtualMusicalInstrumnetsTab.setObjectName("VirtualMusicalInstrumnetsTab")
        self.PianoXylophoneSeparateLine = QtWidgets.QFrame(self.VirtualMusicalInstrumnetsTab)
        self.PianoXylophoneSeparateLine.setGeometry(QtCore.QRect(490, 90, 20, 751))
        self.PianoXylophoneSeparateLine.setFrameShape(QtWidgets.QFrame.VLine)
        self.PianoXylophoneSeparateLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.PianoXylophoneSeparateLine.setObjectName("PianoXylophoneSeparateLine")
        self.XylophoneBongosSeparateLine = QtWidgets.QFrame(self.VirtualMusicalInstrumnetsTab)
        self.XylophoneBongosSeparateLine.setGeometry(QtCore.QRect(1010, 90, 20, 751))
        self.XylophoneBongosSeparateLine.setFrameShape(QtWidgets.QFrame.VLine)
        self.XylophoneBongosSeparateLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.XylophoneBongosSeparateLine.setObjectName("XylophoneBongosSeparateLine")
        self.PianoImageLabel = QtWidgets.QLabel(self.VirtualMusicalInstrumnetsTab)
        self.PianoImageLabel.setGeometry(QtCore.QRect(20, 260, 431, 271))
        self.PianoImageLabel.setText("")
        self.PianoImageLabel.setPixmap(QtGui.QPixmap("D:\\spring22\\SBEN311\\task#3\\Musical-Instruments-Emphasizer/piano.jpg"))
        self.PianoImageLabel.setObjectName("PianoImageLabel")
        self.XylophoneImageLabel = QtWidgets.QLabel(self.VirtualMusicalInstrumnetsTab)
        self.XylophoneImageLabel.setGeometry(QtCore.QRect(580, 260, 361, 271))
        self.XylophoneImageLabel.setText("")
        self.XylophoneImageLabel.setPixmap(QtGui.QPixmap("D:\\spring22\\SBEN311\\task#3\\Musical-Instruments-Emphasizer/Xylophone.png"))
        self.XylophoneImageLabel.setObjectName("XylophoneImageLabel")
        self.BongosImageLabel = QtWidgets.QLabel(self.VirtualMusicalInstrumnetsTab)
        self.BongosImageLabel.setGeometry(QtCore.QRect(1040, 280, 311, 271))
        self.BongosImageLabel.setText("")
        self.BongosImageLabel.setPixmap(QtGui.QPixmap("D:\\spring22\\SBEN311\\task#3\\Musical-Instruments-Emphasizer/bongosPNG.png"))
        self.BongosImageLabel.setObjectName("BongosImageLabel")
        self.PianoTitelTextLabel = QtWidgets.QLabel(self.VirtualMusicalInstrumnetsTab)
        self.PianoTitelTextLabel.setGeometry(QtCore.QRect(160, 80, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.PianoTitelTextLabel.setFont(font)
        self.PianoTitelTextLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.PianoTitelTextLabel.setObjectName("PianoTitelTextLabel")
        self.XylophoneTitelTextLabel = QtWidgets.QLabel(self.VirtualMusicalInstrumnetsTab)
        self.XylophoneTitelTextLabel.setGeometry(QtCore.QRect(630, 60, 231, 81))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.XylophoneTitelTextLabel.setFont(font)
        self.XylophoneTitelTextLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.XylophoneTitelTextLabel.setObjectName("XylophoneTitelTextLabel")
        self.BongosTitelTextLabel = QtWidgets.QLabel(self.VirtualMusicalInstrumnetsTab)
        self.BongosTitelTextLabel.setGeometry(QtCore.QRect(1170, 70, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.BongosTitelTextLabel.setFont(font)
        self.BongosTitelTextLabel.setObjectName("BongosTitelTextLabel")
        self.PianoBKeyPushButton = QtWidgets.QPushButton(self.VirtualMusicalInstrumnetsTab)
        self.PianoBKeyPushButton.setGeometry(QtCore.QRect(390, 420, 51, 101))
        self.PianoBKeyPushButton.setStyleSheet("QPushButton{\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(229,229,229);\n"
"}")
        self.PianoBKeyPushButton.setObjectName("PianoBKeyPushButton")
        self.PianoAKeyPushButton = QtWidgets.QPushButton(self.VirtualMusicalInstrumnetsTab)
        self.PianoAKeyPushButton.setGeometry(QtCore.QRect(330, 420, 51, 101))
        self.PianoAKeyPushButton.setStyleSheet("QPushButton{\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(229,229,229);\n"
"}")
        self.PianoAKeyPushButton.setObjectName("PianoAKeyPushButton")
        self.PianoGKeyPushButton = QtWidgets.QPushButton(self.VirtualMusicalInstrumnetsTab)
        self.PianoGKeyPushButton.setGeometry(QtCore.QRect(270, 420, 51, 101))
        self.PianoGKeyPushButton.setStyleSheet("QPushButton{\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(229,229,229);\n"
"}")
        self.PianoGKeyPushButton.setObjectName("PianoGKeyPushButton")
        self.PianoFKeyPushButton = QtWidgets.QPushButton(self.VirtualMusicalInstrumnetsTab)
        self.PianoFKeyPushButton.setGeometry(QtCore.QRect(210, 420, 51, 101))
        self.PianoFKeyPushButton.setStyleSheet("QPushButton{\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(229,229,229);\n"
"}\n"
"")
        self.PianoFKeyPushButton.setObjectName("PianoFKeyPushButton")
        self.PianoEKeyPushButton = QtWidgets.QPushButton(self.VirtualMusicalInstrumnetsTab)
        self.PianoEKeyPushButton.setGeometry(QtCore.QRect(150, 420, 51, 101))
        self.PianoEKeyPushButton.setStyleSheet("QPushButton{\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(229,229,229);\n"
"}\n"
"")
        self.PianoEKeyPushButton.setObjectName("PianoEKeyPushButton")
        self.PianoDKeyPushButton = QtWidgets.QPushButton(self.VirtualMusicalInstrumnetsTab)
        self.PianoDKeyPushButton.setGeometry(QtCore.QRect(90, 420, 51, 101))
        self.PianoDKeyPushButton.setStyleSheet("QPushButton{\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(229,229,229);\n"
"}")
        self.PianoDKeyPushButton.setObjectName("PianoDKeyPushButton")
        self.PianoCKeyPushButton = QtWidgets.QPushButton(self.VirtualMusicalInstrumnetsTab)
        self.PianoCKeyPushButton.setGeometry(QtCore.QRect(20, 420, 51, 101))
        self.PianoCKeyPushButton.setStyleSheet("QPushButton{\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(229,229,229);\n"
"}")
        self.PianoCKeyPushButton.setObjectName("PianoCKeyPushButton")
        self.PianoZKeyPushButton = QtWidgets.QPushButton(self.VirtualMusicalInstrumnetsTab)
        self.PianoZKeyPushButton.setGeometry(QtCore.QRect(370, 260, 30, 151))
        self.PianoZKeyPushButton.setStyleSheet("QPushButton{\n"
"border-radius:0px;\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(229,229,229);\n"
"}")
        self.PianoZKeyPushButton.setObjectName("PianoZKeyPushButton")
        self.PianoTKeyPushButton = QtWidgets.QPushButton(self.VirtualMusicalInstrumnetsTab)
        self.PianoTKeyPushButton.setGeometry(QtCore.QRect(310, 260, 28, 151))
        self.PianoTKeyPushButton.setStyleSheet("QPushButton{\n"
"border-radius:0px;\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(229,229,229);\n"
"}")
        self.PianoTKeyPushButton.setObjectName("PianoTKeyPushButton")
        self.PianoRKeyPushButton = QtWidgets.QPushButton(self.VirtualMusicalInstrumnetsTab)
        self.PianoRKeyPushButton.setGeometry(QtCore.QRect(250, 260, 28, 151))
        self.PianoRKeyPushButton.setStyleSheet("QPushButton{\n"
"border-radius:0px;\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(229,229,229);\n"
"}")
        self.PianoRKeyPushButton.setObjectName("PianoRKeyPushButton")
        self.PianoWKeyPushButton = QtWidgets.QPushButton(self.VirtualMusicalInstrumnetsTab)
        self.PianoWKeyPushButton.setGeometry(QtCore.QRect(130, 260, 27, 151))
        self.PianoWKeyPushButton.setStyleSheet("QPushButton{\n"
"border-radius:0px;\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(229,229,229);\n"
"}")
        self.PianoWKeyPushButton.setObjectName("PianoWKeyPushButton")
        self.PianoQKeyPushButton = QtWidgets.QPushButton(self.VirtualMusicalInstrumnetsTab)
        self.PianoQKeyPushButton.setGeometry(QtCore.QRect(70, 260, 27, 151))
        self.PianoQKeyPushButton.setStyleSheet("QPushButton{\n"
"border-radius:0px;\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(229,229,229);\n"
"}")
        self.PianoQKeyPushButton.setObjectName("PianoQKeyPushButton")
        self.Xylophone8KeyPushButton = QtWidgets.QPushButton(self.VirtualMusicalInstrumnetsTab)
        self.Xylophone8KeyPushButton.setGeometry(QtCore.QRect(880, 360, 22, 70))
        self.Xylophone8KeyPushButton.setStyleSheet("QPushButton{\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(229,229,229);\n"
"}")
        self.Xylophone8KeyPushButton.setObjectName("Xylophone8KeyPushButton")
        self.BongosNKeyPushButton = QtWidgets.QPushButton(self.VirtualMusicalInstrumnetsTab)
        self.BongosNKeyPushButton.setGeometry(QtCore.QRect(1170, 330, 51, 60))
        self.BongosNKeyPushButton.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"")
        self.BongosNKeyPushButton.setObjectName("BongosNKeyPushButton")
        self.BongosMKeyPushButton = QtWidgets.QPushButton(self.VirtualMusicalInstrumnetsTab)
        self.BongosMKeyPushButton.setGeometry(QtCore.QRect(1220, 320, 51, 60))
        self.BongosMKeyPushButton.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"")
        self.BongosMKeyPushButton.setObjectName("BongosMKeyPushButton")
        self.Xylophone7KeyPushButton = QtWidgets.QPushButton(self.VirtualMusicalInstrumnetsTab)
        self.Xylophone7KeyPushButton.setGeometry(QtCore.QRect(840, 350, 25, 90))
        self.Xylophone7KeyPushButton.setStyleSheet("QPushButton{\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(229,229,229);\n"
"}")
        self.Xylophone7KeyPushButton.setObjectName("Xylophone7KeyPushButton")
        self.Xylophone6KeyPushButton = QtWidgets.QPushButton(self.VirtualMusicalInstrumnetsTab)
        self.Xylophone6KeyPushButton.setGeometry(QtCore.QRect(790, 350, 30, 95))
        self.Xylophone6KeyPushButton.setStyleSheet("QPushButton{\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(229,229,229);\n"
"}")
        self.Xylophone6KeyPushButton.setObjectName("Xylophone6KeyPushButton")
        self.Xylophone5KeyPushButton = QtWidgets.QPushButton(self.VirtualMusicalInstrumnetsTab)
        self.Xylophone5KeyPushButton.setGeometry(QtCore.QRect(750, 350, 26, 99))
        self.Xylophone5KeyPushButton.setStyleSheet("QPushButton{\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(229,229,229);\n"
"}")
        self.Xylophone5KeyPushButton.setObjectName("Xylophone5KeyPushButton")
        self.Xylophone4KeyPushButton = QtWidgets.QPushButton(self.VirtualMusicalInstrumnetsTab)
        self.Xylophone4KeyPushButton.setGeometry(QtCore.QRect(710, 350, 23, 100))
        self.Xylophone4KeyPushButton.setStyleSheet("QPushButton{\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(229,229,229);\n"
"}")
        self.Xylophone4KeyPushButton.setObjectName("Xylophone4KeyPushButton")
        self.Xylophone3KeyPushButton = QtWidgets.QPushButton(self.VirtualMusicalInstrumnetsTab)
        self.Xylophone3KeyPushButton.setGeometry(QtCore.QRect(670, 350, 23, 100))
        self.Xylophone3KeyPushButton.setStyleSheet("QPushButton{\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(229,229,229);\n"
"}")
        self.Xylophone3KeyPushButton.setObjectName("Xylophone3KeyPushButton")
        self.Xylophone2KeyPushButton = QtWidgets.QPushButton(self.VirtualMusicalInstrumnetsTab)
        self.Xylophone2KeyPushButton.setGeometry(QtCore.QRect(620, 340, 26, 114))
        self.Xylophone2KeyPushButton.setStyleSheet("QPushButton{\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(229,229,229);\n"
"}")
        self.Xylophone2KeyPushButton.setObjectName("Xylophone2KeyPushButton")
        self.Xylophone1KeyPushButton = QtWidgets.QPushButton(self.VirtualMusicalInstrumnetsTab)
        self.Xylophone1KeyPushButton.setGeometry(QtCore.QRect(590, 340, 16, 119))
        self.Xylophone1KeyPushButton.setStyleSheet("QPushButton{\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(229,229,229);\n"
"}")
        self.Xylophone1KeyPushButton.setObjectName("Xylophone1KeyPushButton")
        self.MainTitelTextLabel = QtWidgets.QLabel(self.VirtualMusicalInstrumnetsTab)
        self.MainTitelTextLabel.setGeometry(QtCore.QRect(410, 20, 701, 51))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.MainTitelTextLabel.setFont(font)
        self.MainTitelTextLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.MainTitelTextLabel.setObjectName("MainTitelTextLabel")
        self.MainTabWidget.addTab(self.VirtualMusicalInstrumnetsTab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1497, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon3)
        self.actionOpen.setObjectName("actionOpen")
        self.menuFile.addAction(self.actionOpen)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.MainTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SongGraphTextLabel.setText(_translate("MainWindow", "Song Graph"))
        self.SpectrogramGraphTextLabel.setText(_translate("MainWindow", "Spectrogram"))
        self.InstrumentEmphasizerGroupBox.setTitle(_translate("MainWindow", "Instrument Emphasizer"))
        self.BassMaximumFrequencyTextLabel.setText(_translate("MainWindow", "128 Hz"))
        self.TromboneTitelLabel.setText(_translate("MainWindow", "Trombone"))
        self.E_FlatClarinetMaximumFrequencyTextLabel.setText(_translate("MainWindow", "1000 Hz"))
        self.E_FlatClarinetTitelLabel.setText(_translate("MainWindow", "E-Flat Clarinet"))
        self.BassGainValueTextLabel.setText(_translate("MainWindow", "1x"))
        self.TromboneGainValueTextLabel.setText(_translate("MainWindow", "1x"))
        self.TromboneMaximumFrequencyTextLabel.setText(_translate("MainWindow", "550 Hz"))
        self.E_FlatClarinetGainValueTextLabel.setText(_translate("MainWindow", "1x"))
        self.BassTitelLabel.setText(_translate("MainWindow", "Bass"))
        self.ViolaMaximumFrequencyTextLabel.setText(_translate("MainWindow", "20,000 Hz"))
        self.PiccoloMaximumFrequencyTextLabel.setText(_translate("MainWindow", "2000 Hz"))
        self.ViolaTitelLabel.setText(_translate("MainWindow", "Viola"))
        self.PiccoloGainValueTextLabel.setText(_translate("MainWindow", "1x"))
        self.ViolaGainValueTextLabel.setText(_translate("MainWindow", "1x"))
        self.PiccoloTitelLabel.setText(_translate("MainWindow", "Piccolo"))
        self.MainTabWidget.setTabText(self.MainTabWidget.indexOf(self.PlayerAndEmphasizerTab), _translate("MainWindow", "Player & Emphasizer"))
        self.PianoTitelTextLabel.setText(_translate("MainWindow", "Piano"))
        self.XylophoneTitelTextLabel.setText(_translate("MainWindow", "Xylophone"))
        self.BongosTitelTextLabel.setText(_translate("MainWindow", "Bongos"))
        self.PianoBKeyPushButton.setText(_translate("MainWindow", "B"))
        self.PianoAKeyPushButton.setText(_translate("MainWindow", "A"))
        self.PianoGKeyPushButton.setText(_translate("MainWindow", "G"))
        self.PianoFKeyPushButton.setText(_translate("MainWindow", "F"))
        self.PianoEKeyPushButton.setText(_translate("MainWindow", "E"))
        self.PianoDKeyPushButton.setText(_translate("MainWindow", "D"))
        self.PianoCKeyPushButton.setText(_translate("MainWindow", "C"))
        self.PianoZKeyPushButton.setText(_translate("MainWindow", "Z"))
        self.PianoTKeyPushButton.setText(_translate("MainWindow", "T"))
        self.PianoRKeyPushButton.setText(_translate("MainWindow", "R"))
        self.PianoWKeyPushButton.setText(_translate("MainWindow", "W"))
        self.PianoQKeyPushButton.setText(_translate("MainWindow", "Q"))
        self.Xylophone8KeyPushButton.setText(_translate("MainWindow", "8"))
        self.BongosNKeyPushButton.setText(_translate("MainWindow", "N"))
        self.BongosMKeyPushButton.setText(_translate("MainWindow", "M"))
        self.Xylophone7KeyPushButton.setText(_translate("MainWindow", "7"))
        self.Xylophone6KeyPushButton.setText(_translate("MainWindow", "6"))
        self.Xylophone5KeyPushButton.setText(_translate("MainWindow", "5"))
        self.Xylophone4KeyPushButton.setText(_translate("MainWindow", "4"))
        self.Xylophone3KeyPushButton.setText(_translate("MainWindow", "3"))
        self.Xylophone2KeyPushButton.setText(_translate("MainWindow", "2"))
        self.Xylophone1KeyPushButton.setText(_translate("MainWindow", "1"))
        self.MainTitelTextLabel.setText(_translate("MainWindow", "Virtual Musical Instrumnets"))
        self.MainTabWidget.setTabText(self.MainTabWidget.indexOf(self.VirtualMusicalInstrumnetsTab), _translate("MainWindow", " Musical Instrumnets "))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
from pyqtgraph import PlotWidget
# import images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
