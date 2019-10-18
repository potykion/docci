import io

import pytest
from openpyxl import Workbook, load_workbook

from docci.xlsx import xlsx_to_bytes, xlsx_to_file


@pytest.fixture()
def xlsx() -> Workbook:
    xlsx_ = Workbook()
    xlsx_.active.append(["sam"])
    return xlsx_


def test_xlsx_to_bytes_saves_xlsx_as_valid_bytes(xlsx: Workbook) -> None:
    bytes_ = xlsx_to_bytes(xlsx)
    stream = io.BytesIO(bytes_)
    actual_xlsx = load_workbook(stream)

    assert tuple(actual_xlsx.active.values) == tuple(xlsx.active.values)


def test_xlsx_to_file_saves_xlsx_as_file_attachment(xlsx: Workbook) -> None:
    xlsx_file = xlsx_to_file(xlsx, "sam.xlsx")

    assert xlsx_file.name == "sam.xlsx"
    assert xlsx_file.content == xlsx_to_bytes(xlsx)
