from typing import Union

from enums import ConversionFormat
from imageconverter import ImageConverter
from audioconverter import AudioConverter
from documentconverter import DocumentConverter


class ConverterProcessor:
    def __init__(
        self,
        converter: Union[
            ImageConverter,
            AudioConverter,
            DocumentConverter,
        ],
    ):
        self.converter: Union[
            ImageConverter, AudioConverter, DocumentConverter
        ] = converter

    def process(self, input_data: str, output_format: ConversionFormat):
        self.converter.convert(input_data, output_format)
