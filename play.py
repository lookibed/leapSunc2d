from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import QUrl

class VideoPlayer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt Video Player")
        self.setGeometry(100, 100, 800, 600)

        # Создаем виджеты
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.videoWidget = QVideoWidget()
        self.openButton = QPushButton("Open Video")
        self.playButton = QPushButton("Play")
        self.pauseButton = QPushButton("Pause")

        # Подключаем кнопки
        self.openButton.clicked.connect(self.open_file)
        self.playButton.clicked.connect(self.play_video)
        self.pauseButton.clicked.connect(self.pause_video)

        # Размещаем виджеты
        layout = QVBoxLayout()
        layout.addWidget(self.videoWidget)
        layout.addWidget(self.openButton)
        layout.addWidget(self.playButton)
        layout.addWidget(self.pauseButton)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Связываем плеер с видео-виджетом
        self.mediaPlayer.setVideoOutput(self.videoWidget)

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Video")
        if file_name:
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(file_name)))

    def play_video(self):
        self.mediaPlayer.play()

    def pause_video(self):
        self.mediaPlayer.pause()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    player = VideoPlayer()
    player.show()
    sys.exit(app.exec_())
