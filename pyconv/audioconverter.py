from baseconverter import BaseConverter


class AudioConverter(BaseConverter):
    def convert(self, input_file, output_format):
        raise NotImplementedError("AudioConverter is not implemented")
