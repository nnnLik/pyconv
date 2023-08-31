import argparse

from enums import ConversionFormat
from processor import ConverterProcessor
from converters import (
    image_converter,
    audio_converter,
    document_converter,
)
from exceptions import UnsupportedFormatError, MissingArgumentError
from utils import format_arg, is_supported_format


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert Any to Any")
    parser.add_argument("input", help="Input file/directory to convert")
    parser.add_argument(
        "-to", dest="output_format", help="Output format", type=format_arg
    )

    args = parser.parse_args()

    input_data: str = args.input
    output_format: ConversionFormat = args.output_format

    if not input_data or not output_format:
        raise MissingArgumentError()

    file_extension = input_data.split(".")[-1].lower()

    if not is_supported_format(file_extension):
        raise UnsupportedFormatError(file_extension)

    if not is_supported_format(output_format.value.lower()):
        raise UnsupportedFormatError(output_format.value.lower())

    if file_extension in ["jpg", "jpeg", "png", "gif"]:
        selected_converter = image_converter
    elif file_extension in ["mp3", "wav", "flac"]:
        selected_converter = audio_converter
    elif file_extension in ["pdf", "doc", "docx"]:
        selected_converter = document_converter

    processor = ConverterProcessor(selected_converter)
    processor.process(input_data, output_format)
