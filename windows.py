# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_krr_anyKeys_convertor(object):
    def setupUi(self, krr_anyKeys_convertor):
        krr_anyKeys_convertor.setObjectName("krr_anyKeys_convertor")
        krr_anyKeys_convertor.setWindowModality(QtCore.Qt.NonModal)
        krr_anyKeys_convertor.setEnabled(True)
        krr_anyKeys_convertor.resize(370, 510)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(krr_anyKeys_convertor.sizePolicy().hasHeightForWidth())
        krr_anyKeys_convertor.setSizePolicy(sizePolicy)
        krr_anyKeys_convertor.setMinimumSize(QtCore.QSize(0, 0))
        krr_anyKeys_convertor.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        krr_anyKeys_convertor.setAcceptDrops(False)
        krr_anyKeys_convertor.setStyleSheet("font: 12pt \"Arial\";")
        self.centralwidget = QtWidgets.QWidget(krr_anyKeys_convertor)
        self.centralwidget.setAcceptDrops(False)
        self.centralwidget.setObjectName("centralwidget")
        self.splitter_15 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_15.setGeometry(QtCore.QRect(10, 10, 351, 441))
        self.splitter_15.setOrientation(QtCore.Qt.Vertical)
        self.splitter_15.setObjectName("splitter_15")
        self.layoutWidget = QtWidgets.QWidget(self.splitter_15)
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout_5 = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout_5.setContentsMargins(0, 0, 0, 0)
        self.formLayout_5.setObjectName("formLayout_5")
        self.splitter_6 = QtWidgets.QSplitter(self.layoutWidget)
        self.splitter_6.setOrientation(QtCore.Qt.Vertical)
        self.splitter_6.setObjectName("splitter_6")
        self.label = QtWidgets.QLabel(self.splitter_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.splitter_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.splitter_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_3.setObjectName("label_3")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.splitter_6)
        self.splitter_7 = QtWidgets.QSplitter(self.layoutWidget)
        self.splitter_7.setOrientation(QtCore.Qt.Vertical)
        self.splitter_7.setObjectName("splitter_7")
        self.lineEdit_savepath = QtWidgets.QLineEdit(self.splitter_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_savepath.sizePolicy().hasHeightForWidth())
        self.lineEdit_savepath.setSizePolicy(sizePolicy)
        self.lineEdit_savepath.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEdit_savepath.setWhatsThis("")
        self.lineEdit_savepath.setObjectName("lineEdit_savepath")
        self.lineEdit_title = QtWidgets.QLineEdit(self.splitter_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_title.sizePolicy().hasHeightForWidth())
        self.lineEdit_title.setSizePolicy(sizePolicy)
        self.lineEdit_title.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEdit_title.setText("")
        self.lineEdit_title.setObjectName("lineEdit_title")
        self.lineEdit_artist = QtWidgets.QLineEdit(self.splitter_7)
        self.lineEdit_artist.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEdit_artist.setText("")
        self.lineEdit_artist.setObjectName("lineEdit_artist")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.splitter_7)
        self.org_dir = QtWidgets.QRadioButton(self.layoutWidget)
        self.org_dir.setObjectName("org_dir")
        self.org_dir.setChecked(False)
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.org_dir)
        self.splitter_13 = QtWidgets.QSplitter(self.splitter_15)
        self.splitter_13.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_13.setObjectName("splitter_13")
        self.splitter_12 = QtWidgets.QSplitter(self.splitter_13)
        self.splitter_12.setOrientation(QtCore.Qt.Vertical)
        self.splitter_12.setObjectName("splitter_12")
        self.versionmod = QtWidgets.QRadioButton(self.splitter_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.versionmod.sizePolicy().hasHeightForWidth())
        self.versionmod.setSizePolicy(sizePolicy)
        self.versionmod.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.versionmod.setCheckable(True)
        self.versionmod.setChecked(True)
        self.versionmod.setObjectName("versionmod")
        self.layoutWidget_2 = QtWidgets.QWidget(self.splitter_12)
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.layoutWidget_2)
        self.formLayout_2.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.stap = QtWidgets.QLineEdit(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stap.sizePolicy().hasHeightForWidth())
        self.stap.setSizePolicy(sizePolicy)
        self.stap.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.stap.setObjectName("stap")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.stap)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.timestap = QtWidgets.QLineEdit(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timestap.sizePolicy().hasHeightForWidth())
        self.timestap.setSizePolicy(sizePolicy)
        self.timestap.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.timestap.setObjectName("timestap")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.timestap)
        self.splitter_4 = QtWidgets.QSplitter(self.splitter_13)
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setObjectName("splitter_4")
        self.splitter = QtWidgets.QSplitter(self.splitter_4)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label_8 = QtWidgets.QLabel(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_8.setStyleSheet("font: 12pt \"Arial\";")
        self.label_8.setObjectName("label_8")
        self.tokeys = QtWidgets.QLineEdit(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tokeys.sizePolicy().hasHeightForWidth())
        self.tokeys.setSizePolicy(sizePolicy)
        self.tokeys.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tokeys.setObjectName("tokeys")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_4)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.label_13 = QtWidgets.QLabel(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_13.setStyleSheet("font: 12pt \"Arial\";")
        self.label_13.setObjectName("label_13")
        self.blank_columns = QtWidgets.QLineEdit(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.blank_columns.sizePolicy().hasHeightForWidth())
        self.blank_columns.setSizePolicy(sizePolicy)
        self.blank_columns.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.blank_columns.setObjectName("blank_columns")
        self.splitter_3 = QtWidgets.QSplitter(self.splitter_4)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.label_5 = QtWidgets.QLabel(self.splitter_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_5.setStyleSheet("font: 12pt \"Arial\";")
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.del_jack_lv_slider = QtWidgets.QSlider(self.splitter_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.del_jack_lv_slider.sizePolicy().hasHeightForWidth())
        self.del_jack_lv_slider.setSizePolicy(sizePolicy)
        self.del_jack_lv_slider.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.del_jack_lv_slider.setMaximum(3)
        self.del_jack_lv_slider.setProperty("value", 2)
        self.del_jack_lv_slider.setOrientation(QtCore.Qt.Horizontal)
        self.del_jack_lv_slider.setObjectName("del_jack_lv_slider")
        self.splitter_11 = QtWidgets.QSplitter(self.splitter_15)
        self.splitter_11.setOrientation(QtCore.Qt.Vertical)
        self.splitter_11.setObjectName("splitter_11")
        self.NtoNC = QtWidgets.QRadioButton(self.splitter_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NtoNC.sizePolicy().hasHeightForWidth())
        self.NtoNC.setSizePolicy(sizePolicy)
        self.NtoNC.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.NtoNC.setChecked(True)
        self.NtoNC.setObjectName("NtoNC")
        self.buttonGroup = QtWidgets.QButtonGroup(krr_anyKeys_convertor)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.NtoNC)
        self.to4kdpc = QtWidgets.QRadioButton(self.splitter_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.to4kdpc.sizePolicy().hasHeightForWidth())
        self.to4kdpc.setSizePolicy(sizePolicy)
        self.to4kdpc.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.to4kdpc.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.to4kdpc.setObjectName("to4kdpc")
        self.buttonGroup.addButton(self.to4kdpc)
        self.everything_to_jack = QtWidgets.QRadioButton(self.splitter_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.everything_to_jack.sizePolicy().hasHeightForWidth())
        self.everything_to_jack.setSizePolicy(sizePolicy)
        self.everything_to_jack.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.everything_to_jack.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.everything_to_jack.setObjectName("everything_to_jack")
        self.buttonGroup.addButton(self.everything_to_jack)
        self.everything_to_stream = QtWidgets.QRadioButton(self.splitter_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.everything_to_stream.sizePolicy().hasHeightForWidth())
        self.everything_to_stream.setSizePolicy(sizePolicy)
        self.everything_to_stream.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.everything_to_stream.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.everything_to_stream.setObjectName("everything_to_stream")
        self.buttonGroup.addButton(self.everything_to_stream)
        self.splitter_5 = QtWidgets.QSplitter(self.splitter_11)
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName("splitter_5")
        self.label_jack = QtWidgets.QRadioButton(self.splitter_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_jack.sizePolicy().hasHeightForWidth())
        self.label_jack.setSizePolicy(sizePolicy)
        self.label_jack.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_jack.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_jack.setObjectName("label_jack")
        self.buttonGroup.addButton(self.label_jack)
        self.label_14 = QtWidgets.QLabel(self.splitter_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_14.setObjectName("label_14")
        self.jack_interval = QtWidgets.QLineEdit(self.splitter_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jack_interval.sizePolicy().hasHeightForWidth())
        self.jack_interval.setSizePolicy(sizePolicy)
        self.jack_interval.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.jack_interval.setObjectName("jack_interval")
        self.label_15 = QtWidgets.QLabel(self.splitter_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_15.setObjectName("label_15")
        self.jack_nums = QtWidgets.QLineEdit(self.splitter_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jack_nums.sizePolicy().hasHeightForWidth())
        self.jack_nums.setSizePolicy(sizePolicy)
        self.jack_nums.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.jack_nums.setObjectName("jack_nums")
        self.label_16 = QtWidgets.QLabel(self.splitter_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_16.setObjectName("label_16")
        self.splitter_8 = QtWidgets.QSplitter(self.splitter_11)
        self.splitter_8.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_8.setObjectName("splitter_8")
        self.simplecomvertmod = QtWidgets.QRadioButton(self.splitter_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.simplecomvertmod.sizePolicy().hasHeightForWidth())
        self.simplecomvertmod.setSizePolicy(sizePolicy)
        self.simplecomvertmod.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.simplecomvertmod.setObjectName("simplecomvertmod")
        self.buttonGroup.addButton(self.simplecomvertmod)
        self.convert_list = QtWidgets.QLineEdit(self.splitter_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.convert_list.sizePolicy().hasHeightForWidth())
        self.convert_list.setSizePolicy(sizePolicy)
        self.convert_list.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.convert_list.setObjectName("convert_list")
        self.label_9 = QtWidgets.QLabel(self.splitter_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_9.setObjectName("label_9")
        self.splitter_14 = QtWidgets.QSplitter(self.splitter_15)
        self.splitter_14.setOrientation(QtCore.Qt.Vertical)
        self.splitter_14.setObjectName("splitter_14")
        self.splitter_10 = QtWidgets.QSplitter(self.splitter_14)
        self.splitter_10.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_10.setObjectName("splitter_10")
        self.langlab = QtWidgets.QLabel(self.splitter_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.langlab.sizePolicy().hasHeightForWidth())
        self.langlab.setSizePolicy(sizePolicy)
        self.langlab.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.langlab.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.langlab.setObjectName("langlab")
        self.pushButton = QtWidgets.QPushButton(self.splitter_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.langlab_2 = QtWidgets.QLabel(self.splitter_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.langlab_2.sizePolicy().hasHeightForWidth())
        self.langlab_2.setSizePolicy(sizePolicy)
        self.langlab_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.langlab_2.setText("")
        self.langlab_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.langlab_2.setObjectName("langlab_2")
        self.splitter_9 = QtWidgets.QSplitter(self.splitter_14)
        self.splitter_9.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_9.setObjectName("splitter_9")
        self.label_11 = QtWidgets.QLabel(self.splitter_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_11.setObjectName("label_11")
        self.krrcream = QtWidgets.QLabel(self.splitter_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.krrcream.sizePolicy().hasHeightForWidth())
        self.krrcream.setSizePolicy(sizePolicy)
        self.krrcream.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.krrcream.setObjectName("krrcream")
        self.label_4 = QtWidgets.QLabel(self.splitter_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_12 = QtWidgets.QLabel(self.splitter_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.label_10 = QtWidgets.QLabel(self.splitter_9)
        self.label_10.setObjectName("label_10")
        self.lineEdit = QtWidgets.QLineEdit(self.splitter_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEdit.setText("")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setObjectName("lineEdit")
        self.seed = QtWidgets.QSplitter(self.centralwidget)
        self.seed.setGeometry(QtCore.QRect(10, 460, 351, 22))
        self.seed.setOrientation(QtCore.Qt.Horizontal)
        self.seed.setObjectName("seed")
        self.seed_check = QtWidgets.QCheckBox(self.seed)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.seed_check.sizePolicy().hasHeightForWidth())
        self.seed_check.setSizePolicy(sizePolicy)
        self.seed_check.setObjectName("seed_check")
        self.seed_line = QtWidgets.QLineEdit(self.seed)
        self.seed_line.setObjectName("seed_line")
        krr_anyKeys_convertor.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(krr_anyKeys_convertor)
        self.statusbar.setObjectName("statusbar")
        krr_anyKeys_convertor.setStatusBar(self.statusbar)
        self.label_lst = [self.org_dir, self.label, self.label_2, self.label_3, self.versionmod, self.label_6, self.label_7,
                          self.label_8,
                          self.label_5, self.NtoNC, self.to4kdpc, self.simplecomvertmod, self.langlab, self.pushButton,
                          self.label_4, self.label_9, self.everything_to_jack, self.everything_to_stream, self.label_jack,
                          self.label_14, self.label_15, self.label_13,self.seed_check]
        self.pushButton.clicked.connect(self.switchLanguage)
        self.retranslateUi(krr_anyKeys_convertor)
        QtCore.QMetaObject.connectSlotsByName(krr_anyKeys_convertor)
    def switchLanguage(self):
        _translate = QtCore.QCoreApplication.translate
        lang = [["保存到原路径(以上3参数失效)",
                 "保存路径:",
                 "标   题:",
                 "艺 术 家:",
                 "用包名命名Title",
                 "步距:",
                 "时间步距:",
                 "目标键数:",
                 "删子弹等级:",
                 "狂风插入    支持4-20键任意转换",
                 "混沌裤衩    仅4键转8键",
                 "简单矩阵转换",
                 "当前语言:中文",
                 "EN",
                 "说明",
                 "示例①4KDP:0,1,2,3,0,1,2,3 ②7k快速删空to6k 0,1,2,4,5,6",
                 "万物化叠      仅需目标键数",
                 "万物化切      仅需目标键数",
                 "杰克世界",
                 "步距:",
                 "数量:",
                 "随机空列数:",
                 "固定种子    种子:"],
                ["Save to the original path (the above are invalid)",
                 "Save path:",
                 "Title:",
                 "Artist:",
                 "Name version by title",
                 "Stap:",
                 "Time stap:",
                 "Target keys:",
                 "Jack deletion LV:",
                 "[NToNC]Supports 4-20keys arbitrary conversion",
                 "[4To8DPC]Only 4keys to 8keys",
                 "[NToNS]",
                 "Language:EN",
                 "中文",
                 "Instructions",
                 "E.g:①4KDP:0,1,2,3,0,1,2,3 ②7kdelspaceto6k:0,1,2,4,5,6",
                 "Everything to jack    Only need target keys",
                 "Everything to stream    Only need target keys",
                 "Jack World",
                 "JStap:",
                 "Quantity:",
                 "Random blank:",
                 "Fixed seed    Seed:"]]

        if self.langlab.text() == "当前语言:中文":
            for i in range(23):
                self.label_lst[i].setText(lang[1][i])
                self.label_9.setText(_translate("krr_anyKeys_convertor",
                                                "<html><head/><body><p><span style=\" font-size:10pt;\">E.g:①4KDP:0,1,2,3,0,1,2,3 ②7kdelspacek:0,1,2,4,5,6""</span></p></body></html>"))
                self.label_12.setText(_translate("krr_anyKeys_convertor",
                                                 "<html><head/><body><p><a href=\"https://github.com/krrcream/krr-s-osumania-anyKeys-converter\"><span style=\" text-decoration: underline; color:#0000ff;\">github</span></a></p></body></html>"))
                self.label_16.setText(_translate("krr_anyKeys_convertor",
                                                 "<html><head/><body><p><span style=\" font-size:9pt;\">Jack World and [NToNS] does not require target keys</span></p></body></html>"))

                self.setWindowTitle(
                    _translate("krr_anyKeys_convertor", "Krrcream's_anyKeys_Converter V0.90"))
        else:
            for i in range(23):
                self.label_lst[i].setText(lang[0][i])
                self.label_9.setText(_translate("krr_anyKeys_convertor", "<html><head/><body><p><span style=\" font-size:10pt;\">示例①4KDP:0,1,2,3,0,1,2,3 ②7k快速删空to6k 0,1,2,4,5,6</span></p></body></html>"))
                self.label_12.setText(_translate("krr_anyKeys_convertor",
                                                 "<html><head/><body><p><a href=\"https://github.com/krrcream/krr-s-osumania-anyKeys-converter\"><span style=\" text-decoration: underline; color:#0000ff;\">github</span></a></p></body></html>"))
                self.label_16.setText(_translate("krr_anyKeys_convertor",
                                                 "<html><head/><body><p><span style=\" font-size:9pt;\">杰克世界和简单矩阵转换，目标键数会失效</span></p></body></html>"))
                self.setWindowTitle(
                    _translate("krr_anyKeys_convertor", "Krrcream的任意Keys转换器 V0.90"))
    def retranslateUi(self, krr_anyKeys_convertor):
        _translate = QtCore.QCoreApplication.translate
        krr_anyKeys_convertor.setWindowTitle(_translate("krr_anyKeys_convertor", "Krrcream的任意Keys转换器 V0.90"))
        krr_anyKeys_convertor.setWhatsThis(_translate("krr_anyKeys_convertor", "<html><head/><body><p>这是krrcream写的任意Keys转换器。</p></body></html>"))
        self.label.setText(_translate("krr_anyKeys_convertor", "<html><head/><body><p align=\"right\">保存路径：</p></body></html>"))
        self.label_2.setText(_translate("krr_anyKeys_convertor", "<html><head/><body><p align=\"right\">标 题：</p></body></html>"))
        self.label_3.setText(_translate("krr_anyKeys_convertor", "<html><head/><body><p align=\"right\">艺 术 家：</p></body></html>"))
        self.org_dir.setText(_translate("krr_anyKeys_convertor", "保存到原路径(以上3个参数无效)"))
        self.versionmod.setText(_translate("krr_anyKeys_convertor", "用包名命名version"))
        self.label_6.setText(_translate("krr_anyKeys_convertor", "<html><head/><body><p align=\"right\"><span style=\" font-size:11pt;\">步距:</span></p></body></html>"))
        self.stap.setText(_translate("krr_anyKeys_convertor", "16"))
        self.label_7.setText(_translate("krr_anyKeys_convertor", "<html><head/><body><p align=\"right\"><span style=\" font-size:11pt;\">时间步距:</span></p></body></html>"))
        self.timestap.setText(_translate("krr_anyKeys_convertor", "1000"))
        self.label_8.setText(_translate("krr_anyKeys_convertor", "<html><head/><body><p align=\"right\"><span style=\" font-size:11pt;\">目 标 键 数:</span></p></body></html>"))
        self.tokeys.setText(_translate("krr_anyKeys_convertor", "8"))
        self.label_13.setText(_translate("krr_anyKeys_convertor", "<html><head/><body><p align=\"right\"><span style=\" font-size:11pt;\">随机空列数:</span></p></body></html>"))
        self.blank_columns.setText(_translate("krr_anyKeys_convertor", "0"))
        self.label_5.setToolTip(_translate("krr_anyKeys_convertor", "<html><head/><body><p><br/></p></body></html>"))
        self.label_5.setText(_translate("krr_anyKeys_convertor", "<html><head/><body><p align=\"right\"><span style=\" font-size:11pt;\">删子弹等级:</span></p></body></html>"))
        self.NtoNC.setText(_translate("krr_anyKeys_convertor", "狂风插入      支持4-20keys任意转换"))
        self.to4kdpc.setText(_translate("krr_anyKeys_convertor", "混沌裤衩      仅支持4to8keys"))
        self.everything_to_jack.setText(_translate("krr_anyKeys_convertor", "万物化叠      仅需目标键数"))
        self.everything_to_stream.setText(_translate("krr_anyKeys_convertor", "万物化切      仅需目标键数"))
        self.label_jack.setText(_translate("krr_anyKeys_convertor", "杰克世界"))
        self.label_14.setText(_translate("krr_anyKeys_convertor", "<html><head/><body><p align=\"right\">步距</p></body></html>"))
        self.jack_interval.setText(_translate("krr_anyKeys_convertor", "8"))
        self.label_15.setText(_translate("krr_anyKeys_convertor", "<html><head/><body><p align=\"right\">数量</p></body></html>"))
        self.jack_nums.setText(_translate("krr_anyKeys_convertor", "1"))
        self.label_16.setText(_translate("krr_anyKeys_convertor", "<html><head/><body><p><span style=\" font-size:9pt;\">杰克世界和简单矩阵转换，目标键数会失效</span></p></body></html>"))
        self.simplecomvertmod.setText(_translate("krr_anyKeys_convertor", "简单矩阵转换："))
        self.label_9.setText(_translate("krr_anyKeys_convertor", "<html><head/><body><p><span style=\" font-size:9pt;\">示例①4KDP:0,1,2,3,0,1,2,3   ②7k快速删空to6k:0,1,2,4,5,6</span></p></body></html>"))
        self.langlab.setText(_translate("krr_anyKeys_convertor", "当前语言:中文"))
        self.pushButton.setText(_translate("krr_anyKeys_convertor", "EN"))
        self.label_11.setText(_translate("krr_anyKeys_convertor", "<html><head/><body><p><span style=\" font-weight:600;\">by:</span></p></body></html>"))
        self.krrcream.setText(_translate("krr_anyKeys_convertor", "<html><head/><body><p><a href=\"https://space.bilibili.com/276844\"><span style=\" font-weight:600; text-decoration: underline; color:#0000ff;\">@krrcream</span></a></p></body></html>"))
        self.label_4.setText(_translate("krr_anyKeys_convertor", "说明:"))
        self.seed_check.setText(_translate("krr_anyKeys_convertor", "固定种子    种子:"))
        self.label_12.setText(_translate("krr_anyKeys_convertor", "<html><head/><body><p><a href=\"https://github.com/krrcream/krr-s-osumania-anyKeys-converter\"><span style=\" text-decoration: underline; color:#0000ff;\">github</span></a></p></body></html>"))
        self.label_10.setText(_translate("krr_anyKeys_convertor", "<html><head/><body><p><a href=\"https://www.bilibili.com/video/BV1Tt421F7xw\"><span style=\" text-decoration: underline; color:#0000ff;\">Bilibili</span></a></p></body></html>"))
        self.label_10.setOpenExternalLinks(True)
        self.label_12.setOpenExternalLinks(True)
        self.krrcream.setOpenExternalLinks(True)