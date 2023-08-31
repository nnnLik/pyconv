from baseconverter import BaseConverter


class DocumentConverter(BaseConverter):
    def convert(self, input_file, output_format):
        raise NotImplementedError("DocumentConverter is not implemented")
