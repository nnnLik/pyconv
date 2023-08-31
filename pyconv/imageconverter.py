from PIL import Image
from typing import Optional

from exceptions import ConverterError, UnsupportedFormatError
from enums import ImageFormat
from baseconverter import BaseConverter


class ImageConverter(BaseConverter):
    def _get_format_enum(self, format_str: str) -> Optional[ImageFormat]:
        try:
            return ImageFormat(format_str)
        except ValueError:
            return None

    def _generate_output_filename(
        self, input_filename: str, output_format: ImageFormat
    ) -> str:
        base_name, _ = input_filename.split(".")
        return f"{base_name}.{output_format.value}"

    def convert(self, input_file: str, output_format: str) -> None:
        format_enum = self._get_format_enum(output_format)
        if format_enum is None:
            raise UnsupportedFormatError(output_format)

        output_file = self._generate_output_filename(input_file, format_enum)

        try:
            image = Image.open(input_file)
        except Exception as e:
            raise ConverterError(f"Image open error: {e}")

        try:
            image.save(output_file, format=format_enum.value)
        except Exception as e:
            raise ConverterError(f"Image save error: {e}")
