from enums import AudioFormat, DocumentFormat, ImageFormat
from exceptions import UnsupportedFormatError


def is_supported_format(format):
    for enum_class in [ImageFormat, AudioFormat, DocumentFormat]:
        if format in [format_enum.value for format_enum in enum_class]:
            return True
    return False


def format_arg(value):
    for format_enum in [ImageFormat, AudioFormat, DocumentFormat]:
        try:
            return format_enum(value)
        except ValueError:
            continue
    raise UnsupportedFormatError(value)
