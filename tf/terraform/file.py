import hcl2

from terraform.block import BlockType, Block


class TerraformFile:
    def __init__(self, file_path: str):
        self._file_content = self._parse_terrafrom_file(file_path)
        self._file_path = file_path
        self._blocks = self._generate_blocks(self._file_content)

    def _generate_blocks(self, file_content: str) -> Block:
        for key, attrs in file_content.items():
            block = Block(key, attrs)

    def _parse_terrafrom_file(self, file_path: str) -> dict:
        """Parse a Terraform file and return its contents as a dictionary.

        Args:
            file_path (str): The path to the Terraform file.

        Returns:
            dict: A dictionary containing the parsed contents of the Terraform file.
        """
        with open(file_path, "r") as file:
            return hcl2.load(file)

    def sort(self, content: dict, block_type: str, order: bool) -> dict:
        """Sort the blocks in a Terraform file by resource type.

        Args:
            blocks (dict): The blocks to be sorted.
            block_type (str): The type of block to sort by.

        Returns:
            dict: The sorted blocks.
        """
        if block_type == BlockType.variable:
            variables = content["variable"]
            sorted_ = sorted(variables, key=lambda d: list(d.keys())[0])
            return sorted_

        return None

    @property
    def file_content(self) -> dict:
        """Return the contents of the Terraform file.

        Returns:
            dict: The contents of the Terraform file.
        """
        return self._file_content

    @property
    def file_path(self) -> str:
        """Return the path to the Terraform file.

        Returns:
            str: The path to the Terraform file.
        """
        return self._file_path

    @property
    def file_name(self) -> str:
        """Return the name of the Terraform file.

        Returns:
            str: The name of the Terraform file.
        """
        return self._file_path.split("/")[-1]
