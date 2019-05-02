import os

from docci.file import extract_file_name, FileAttachment


def test_file_attachment_load_sets_name_and_has_contest() -> None:
    file_ = FileAttachment.load(__file__)

    assert file_.name == extract_file_name(__file__)
    assert file_.content


def test_file_attachment_save_creates_file_on_disk() -> None:
    file_ = FileAttachment.load(__file__)

    save_path = "delete_test_api.py"
    file_.save(save_path)

    assert os.path.exists(save_path)

    os.remove(save_path)
    assert not os.path.exists(save_path)
