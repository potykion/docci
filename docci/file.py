"""
Utils for file manipulations like extracting file name from path
"""

import os
from dataclasses import dataclass, field
from typing import Optional


def extract_file_name(path: str) -> str:
    """
    >>> extract_file_name("tests/test_api.py")
    'test_api.py'
    """
    return os.path.basename(path)


@dataclass
class FileAttachment:
    """
    Class for file abstraction
    """

    name: str
    content: bytes = field(repr=False)

    @property
    def name_without_extension(self) -> str:
        """
        >>> FileAttachment("sample.py", b"").name_without_extension
        'sample'
        """
        return self.name.rsplit(".", 1)[0]

    @property
    def extension(self) -> str:
        """
        >>> FileAttachment("sample.py", b"").extension
        'py'
        """
        return self.name.rsplit(".", 1)[-1]

    def save(self, path: Optional[str] = None) -> None:
        """
        Save file to disk
        """
        path = path or self.name
        with open(path, "wb") as f:
            f.write(self.content)

    @classmethod
    def load(cls, path: str) -> 'FileAttachment':
        """
        Load file from disk
        """
        assert os.path.exists(path), f'No such file: "{path}"'
        with open(path, "rb") as f:
            return FileAttachment(extract_file_name(path), f.read())
