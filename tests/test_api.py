import os

from docci.api import FileAttachment, extract_file_name
from docci.config import BASE_DIR


def test_file_attachment_load_sets_name_and_has_contest() -> None:
    test_path = os.path.join(BASE_DIR, "tests", "test_api.py")
    file_ = FileAttachment.load(test_path)

    assert file_.name == extract_file_name(test_path)
    assert file_.content


def test_file_attachment_save_creates_file_on_disk() -> None:
    test_path = os.path.join(BASE_DIR, "tests", "test_api.py")
    file_ = FileAttachment.load(test_path)

    save_path = "delete_test_api.py"
    file_.save(save_path)

    assert os.path.exists(save_path)

    os.remove(save_path)
    assert not os.path.exists(save_path)
