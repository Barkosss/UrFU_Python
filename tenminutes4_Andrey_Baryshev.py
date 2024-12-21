class FileOperator:

    def __init__(self, filename):
        self.mode = None
        self.filename = filename
        self.file = None

    def __enter__(self):

        try:
            print(f"File \"{self.filename}\" is open")
            return open(self.filename, self.mode)
        except Exception as err:
            raise ValueError("Error: " + err)

    def __exit__(self, exc_type, exc_val, exc_tb):

        if self.file is not None:
            try:
                self.file.close()
                print(f"File \"{self.filename}\"is closed")
                self.file = None
            except Exception as err:
                raise ValueError("Error: " + err)

        if exc_type is not None:
            print("Exception type: " + str(exc_type))
            return True


class ReadFileOperator(FileOperator):
    mode = 'r'

    def read(self):
        try:
            file_content = self.file.read()
            print(f"From file \"{self.filename}\" read data")
            return file_content
        except FileNotFoundError as err:
            raise ValueError("File is not found: " + err)
        except IOError as err:
            raise ValueError("Read file is error: " + err)


class WriteFileOperator(FileOperator):
    mode = 'w'

    def write(self, data):

        try:
            self.file.write(data)
            print(f"In file \"{self.filename}\" write data")
        except IOError as err:
            raise ValueError("Write file is error: " + err)
