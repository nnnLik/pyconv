from enum import Enum


class ImageFormat(Enum):
    JPEG = "jpeg"
    PNG = "png"
    GIF = "gif"


class AudioFormat(Enum):
    MP3 = "mp3"
    WAV = "wav"
    FLAC = "flac"


class DocumentFormat(Enum):
    PDF = "pdf"
    DOC = "doc"
    DOCX = "docx"


class ConversionFormat(Enum):
    IMAGE = ImageFormat
    AUDIO = AudioFormat
    DOCUMENT = DocumentFormat
