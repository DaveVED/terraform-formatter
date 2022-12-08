class NotATerraformFileException(Exception):
    """Exception thrown when a file is not a Terraform file."""

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.message = f"{file_path} is not a Terraform file."

    def __str__(self) -> str:
        return self.message


class InvalidBlockTypeException(Exception):
    """Exception raised when the input dictionary contains an invalid block type."""

    def __init__(self, blocks: dict):
        self.blocks = blocks


class NoValidBlockTypeException(Exception):
    """Exception raised when the input dictionary does not contain a 'variable' or 'output' block."""

    def __init__(self, blocks: dict):
        self.blocks = blocks
