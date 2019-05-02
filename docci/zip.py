"""
Utils for working with zip archives
"""

from typing import Union, Iterable, Sequence
from zipfile import ZipFile

from docci.file import FileAttachment


def list_zip_files(zip_file: Union[str, ZipFile]) -> Sequence[FileAttachment]:
    """
    List zip archive files
    """

    def zip_file_generator(zip_file: ZipFile) -> Iterable[FileAttachment]:
        for filename in zip_file.namelist():
            content = zip_file.read(filename)
            yield FileAttachment(filename, content)

    if isinstance(zip_file, str):
        zip_file = ZipFile(zip_file)

    return list(zip_file_generator(zip_file))
