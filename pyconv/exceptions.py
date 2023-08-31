class PyConvError(Exception):
    pass


class UnsupportedFormatError(PyConvError):
    def __init__(self, input_format: str):
        self.input_format = input_format
        super().__init__(f"Unsupported input format: {input_format}")


class MissingArgumentError(PyConvError):
    def __init__(self):
        super().__init__("You must provide both input and output format.")


class ConverterError(PyConvError):
    def __init__(self, msg: str):
        self.msg = msg
        super().__init__(msg)
