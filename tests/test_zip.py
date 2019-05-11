import os
from operator import attrgetter

from docci.config import TEST_DATA_DIR
from docci.file import FileAttachment
from docci.zip import list_zip_files, zip_files


def test_list_zip_files_show_zip_content() -> None:
    zip_files = list_zip_files(os.path.join(TEST_DATA_DIR, "response.zip"))
    zip_file_names = list(map(attrgetter("name"), zip_files))
    assert zip_file_names == ["PacketDescription.xml", "2f16e9ce590046abac1fd43479845c17.bin"]


def test_list_zip_files_show_zip_content_if_zip_is_inside_of_another_zip() -> None:
    zip_files = list_zip_files(os.path.join(TEST_DATA_DIR, "response.zip"))
    zip_files_map = dict(zip(map(attrgetter("name"), zip_files), zip_files))

    zip_files = list_zip_files(zip_files_map["2f16e9ce590046abac1fd43479845c17.bin"])
    zip_file_names = list(map(attrgetter("name"), zip_files))

    assert zip_file_names == ["file"]


def test_archive_created_by_zip_files_has_files() -> None:
    file_names = ["response.zip", "text.txt"]
    files = [
        FileAttachment.load(os.path.join(TEST_DATA_DIR, file_name)) for file_name in file_names
    ]
    archive = zip_files("sample.zip", files)

    assert list_zip_files(archive) == files
