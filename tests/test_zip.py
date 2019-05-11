import os
from operator import attrgetter

from docci.config import TEST_DATA_DIR
from docci.file import FileAttachment, list_dir_files
from docci.zip import list_zip_files, zip_files, raw_to_zip, zip_dirs


def test_raw_to_zip_convert_bytes_to_zip() -> None:
    raw_zip = FileAttachment.load(os.path.join(TEST_DATA_DIR, "response.zip")).content

    zip_file = raw_to_zip(raw_zip)

    zip_files = list_zip_files(zip_file)
    zip_file_names = list(map(attrgetter("name"), zip_files))
    assert zip_file_names == ["PacketDescription.xml", "2f16e9ce590046abac1fd43479845c17.bin"]


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


def test_zipped_folder_archive_has_folder_files() -> None:
    archive = zip_dirs("sample.zip", [list_dir_files(TEST_DATA_DIR)])
    files = [file.name for file in list_zip_files(archive)]
    assert files == ["response.zip", "text.txt"]
