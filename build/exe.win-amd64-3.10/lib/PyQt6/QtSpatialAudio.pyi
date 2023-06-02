# The PEP 484 type hints stub file for the QtSpatialAudio module.
#
# Generated by SIP 6.7.9
#
# Copyright (c) 2023 Riverbank Computing Limited <info@riverbankcomputing.com>
# 
# This file is part of PyQt6.
# 
# This file may be used under the terms of the GNU General Public License
# version 3.0 as published by the Free Software Foundation and appearing in
# the file LICENSE included in the packaging of this file.  Please review the
# following information to ensure the GNU General Public License version 3.0
# requirements will be met: http://www.gnu.org/copyleft/gpl.html.
# 
# If you do not wish to use this file under the terms of the GPL version 3.0
# then you may purchase a commercial license.  For more information contact
# info@riverbankcomputing.com.
# 
# This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
# WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.


import enum
import typing

import PyQt6.sip

from PyQt6 import QtCore
from PyQt6 import QtGui
from PyQt6 import QtNetwork
from PyQt6 import QtMultimedia

# Support for QDate, QDateTime and QTime.
import datetime

# Convenient type aliases.
PYQT_SIGNAL = typing.Union[QtCore.pyqtSignal, QtCore.pyqtBoundSignal]
PYQT_SLOT = typing.Union[typing.Callable[..., None], QtCore.pyqtBoundSignal]


class QAmbientSound(QtCore.QObject):

    class Loops(enum.Enum):
        Infinite = ... # type: QAmbientSound.Loops
        Once = ... # type: QAmbientSound.Loops

    def __init__(self, engine: 'QAudioEngine') -> None: ...

    def stop(self) -> None: ...
    def pause(self) -> None: ...
    def play(self) -> None: ...
    volumeChanged: typing.ClassVar[QtCore.pyqtSignal]
    autoPlayChanged: typing.ClassVar[QtCore.pyqtSignal]
    loopsChanged: typing.ClassVar[QtCore.pyqtSignal]
    sourceChanged: typing.ClassVar[QtCore.pyqtSignal]
    def engine(self) -> 'QAudioEngine': ...
    def volume(self) -> float: ...
    def setVolume(self, volume: float) -> None: ...
    def setAutoPlay(self, autoPlay: bool) -> None: ...
    def autoPlay(self) -> bool: ...
    def setLoops(self, loops: int) -> None: ...
    def loops(self) -> int: ...
    def source(self) -> QtCore.QUrl: ...
    def setSource(self, url: QtCore.QUrl) -> None: ...


class QAudioEngine(QtCore.QObject):

    class OutputMode(enum.Enum):
        Surround = ... # type: QAudioEngine.OutputMode
        Stereo = ... # type: QAudioEngine.OutputMode
        Headphone = ... # type: QAudioEngine.OutputMode

    DistanceScaleCentimeter = ... # type: float
    DistanceScaleMeter = ... # type: float

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, parent: QtCore.QObject) -> None: ...
    @typing.overload
    def __init__(self, sampleRate: int, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    def resume(self) -> None: ...
    def pause(self) -> None: ...
    def stop(self) -> None: ...
    def start(self) -> None: ...
    distanceScaleChanged: typing.ClassVar[QtCore.pyqtSignal]
    pausedChanged: typing.ClassVar[QtCore.pyqtSignal]
    masterVolumeChanged: typing.ClassVar[QtCore.pyqtSignal]
    outputDeviceChanged: typing.ClassVar[QtCore.pyqtSignal]
    outputModeChanged: typing.ClassVar[QtCore.pyqtSignal]
    def distanceScale(self) -> float: ...
    def setDistanceScale(self, scale: float) -> None: ...
    def roomEffectsEnabled(self) -> bool: ...
    def setRoomEffectsEnabled(self, enabled: bool) -> None: ...
    def paused(self) -> bool: ...
    def setPaused(self, paused: bool) -> None: ...
    def masterVolume(self) -> float: ...
    def setMasterVolume(self, volume: float) -> None: ...
    def outputDevice(self) -> QtMultimedia.QAudioDevice: ...
    def setOutputDevice(self, device: QtMultimedia.QAudioDevice) -> None: ...
    def sampleRate(self) -> int: ...
    def outputMode(self) -> 'QAudioEngine.OutputMode': ...
    def setOutputMode(self, mode: 'QAudioEngine.OutputMode') -> None: ...


class QAudioListener(QtCore.QObject):

    def __init__(self, engine: QAudioEngine) -> None: ...

    def engine(self) -> QAudioEngine: ...
    def rotation(self) -> QtGui.QQuaternion: ...
    def setRotation(self, q: QtGui.QQuaternion) -> None: ...
    def position(self) -> QtGui.QVector3D: ...
    def setPosition(self, pos: QtGui.QVector3D) -> None: ...


class QAudioRoom(QtCore.QObject):

    class Wall(enum.Enum):
        LeftWall = ... # type: QAudioRoom.Wall
        RightWall = ... # type: QAudioRoom.Wall
        Floor = ... # type: QAudioRoom.Wall
        Ceiling = ... # type: QAudioRoom.Wall
        FrontWall = ... # type: QAudioRoom.Wall
        BackWall = ... # type: QAudioRoom.Wall

    class Material(enum.Enum):
        Transparent = ... # type: QAudioRoom.Material
        AcousticCeilingTiles = ... # type: QAudioRoom.Material
        BrickBare = ... # type: QAudioRoom.Material
        BrickPainted = ... # type: QAudioRoom.Material
        ConcreteBlockCoarse = ... # type: QAudioRoom.Material
        ConcreteBlockPainted = ... # type: QAudioRoom.Material
        CurtainHeavy = ... # type: QAudioRoom.Material
        FiberGlassInsulation = ... # type: QAudioRoom.Material
        GlassThin = ... # type: QAudioRoom.Material
        GlassThick = ... # type: QAudioRoom.Material
        Grass = ... # type: QAudioRoom.Material
        LinoleumOnConcrete = ... # type: QAudioRoom.Material
        Marble = ... # type: QAudioRoom.Material
        Metal = ... # type: QAudioRoom.Material
        ParquetOnConcrete = ... # type: QAudioRoom.Material
        PlasterRough = ... # type: QAudioRoom.Material
        PlasterSmooth = ... # type: QAudioRoom.Material
        PlywoodPanel = ... # type: QAudioRoom.Material
        PolishedConcreteOrTile = ... # type: QAudioRoom.Material
        Sheetrock = ... # type: QAudioRoom.Material
        WaterOrIceSurface = ... # type: QAudioRoom.Material
        WoodCeiling = ... # type: QAudioRoom.Material
        WoodPanel = ... # type: QAudioRoom.Material
        UniformMaterial = ... # type: QAudioRoom.Material

    def __init__(self, engine: QAudioEngine) -> None: ...

    reverbBrightnessChanged: typing.ClassVar[QtCore.pyqtSignal]
    reverbTimeChanged: typing.ClassVar[QtCore.pyqtSignal]
    reverbGainChanged: typing.ClassVar[QtCore.pyqtSignal]
    reflectionGainChanged: typing.ClassVar[QtCore.pyqtSignal]
    wallsChanged: typing.ClassVar[QtCore.pyqtSignal]
    rotationChanged: typing.ClassVar[QtCore.pyqtSignal]
    dimensionsChanged: typing.ClassVar[QtCore.pyqtSignal]
    positionChanged: typing.ClassVar[QtCore.pyqtSignal]
    def reverbBrightness(self) -> float: ...
    def setReverbBrightness(self, factor: float) -> None: ...
    def reverbTime(self) -> float: ...
    def setReverbTime(self, factor: float) -> None: ...
    def reverbGain(self) -> float: ...
    def setReverbGain(self, factor: float) -> None: ...
    def reflectionGain(self) -> float: ...
    def setReflectionGain(self, factor: float) -> None: ...
    def wallMaterial(self, wall: 'QAudioRoom.Wall') -> 'QAudioRoom.Material': ...
    def setWallMaterial(self, wall: 'QAudioRoom.Wall', material: 'QAudioRoom.Material') -> None: ...
    def rotation(self) -> QtGui.QQuaternion: ...
    def setRotation(self, q: QtGui.QQuaternion) -> None: ...
    def dimensions(self) -> QtGui.QVector3D: ...
    def setDimensions(self, dim: QtGui.QVector3D) -> None: ...
    def position(self) -> QtGui.QVector3D: ...
    def setPosition(self, pos: QtGui.QVector3D) -> None: ...


class QSpatialSound(QtCore.QObject):

    class Loops(enum.Enum):
        Infinite = ... # type: QSpatialSound.Loops
        Once = ... # type: QSpatialSound.Loops

    class DistanceModel(enum.Enum):
        Logarithmic = ... # type: QSpatialSound.DistanceModel
        Linear = ... # type: QSpatialSound.DistanceModel
        ManualAttenuation = ... # type: QSpatialSound.DistanceModel

    def __init__(self, engine: QAudioEngine) -> None: ...

    def stop(self) -> None: ...
    def pause(self) -> None: ...
    def play(self) -> None: ...
    nearFieldGainChanged: typing.ClassVar[QtCore.pyqtSignal]
    directivityOrderChanged: typing.ClassVar[QtCore.pyqtSignal]
    directivityChanged: typing.ClassVar[QtCore.pyqtSignal]
    occlusionIntensityChanged: typing.ClassVar[QtCore.pyqtSignal]
    manualAttenuationChanged: typing.ClassVar[QtCore.pyqtSignal]
    distanceCutoffChanged: typing.ClassVar[QtCore.pyqtSignal]
    sizeChanged: typing.ClassVar[QtCore.pyqtSignal]
    distanceModelChanged: typing.ClassVar[QtCore.pyqtSignal]
    volumeChanged: typing.ClassVar[QtCore.pyqtSignal]
    rotationChanged: typing.ClassVar[QtCore.pyqtSignal]
    positionChanged: typing.ClassVar[QtCore.pyqtSignal]
    autoPlayChanged: typing.ClassVar[QtCore.pyqtSignal]
    loopsChanged: typing.ClassVar[QtCore.pyqtSignal]
    sourceChanged: typing.ClassVar[QtCore.pyqtSignal]
    def engine(self) -> QAudioEngine: ...
    def nearFieldGain(self) -> float: ...
    def setNearFieldGain(self, gain: float) -> None: ...
    def directivityOrder(self) -> float: ...
    def setDirectivityOrder(self, alpha: float) -> None: ...
    def directivity(self) -> float: ...
    def setDirectivity(self, alpha: float) -> None: ...
    def occlusionIntensity(self) -> float: ...
    def setOcclusionIntensity(self, occlusion: float) -> None: ...
    def manualAttenuation(self) -> float: ...
    def setManualAttenuation(self, attenuation: float) -> None: ...
    def distanceCutoff(self) -> float: ...
    def setDistanceCutoff(self, cutoff: float) -> None: ...
    def size(self) -> float: ...
    def setSize(self, size: float) -> None: ...
    def distanceModel(self) -> 'QSpatialSound.DistanceModel': ...
    def setDistanceModel(self, model: 'QSpatialSound.DistanceModel') -> None: ...
    def volume(self) -> float: ...
    def setVolume(self, volume: float) -> None: ...
    def rotation(self) -> QtGui.QQuaternion: ...
    def setRotation(self, q: QtGui.QQuaternion) -> None: ...
    def position(self) -> QtGui.QVector3D: ...
    def setPosition(self, pos: QtGui.QVector3D) -> None: ...
    def setAutoPlay(self, autoPlay: bool) -> None: ...
    def autoPlay(self) -> bool: ...
    def setLoops(self, loops: int) -> None: ...
    def loops(self) -> int: ...
    def source(self) -> QtCore.QUrl: ...
    def setSource(self, url: QtCore.QUrl) -> None: ...
