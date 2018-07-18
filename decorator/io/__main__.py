import io


class LowerCaseInputStream(io.IOBase):
    def __init__(self, in_, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.input_stream = in_

    def read(self, *args, **kwargs):
        data = self.input_stream.read(*args, **kwargs)
        return data.lower()


input_stream = LowerCaseInputStream(io.TextIOWrapper(io.FileIO("test.txt")))
print(input_stream.read())

