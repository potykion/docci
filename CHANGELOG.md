<!-- https://keepachangelog.com/en/1.0.0/ -->

# Changelog

## 0.6.0 - 2019-12-22

### Added 

- docci.xlsx.dicts_to_xlsx - Create openpyxl.Workbook with rows of {dicts} values.

## 0.5.0 - 2019-10-18

### Added

- docci.xlsx.xlsx_to_bytes - Convert openpyxl.Workbook to bytes (#1)
- docci.xlsx.xlsx_to_file - Convert openpyxl.Workbook to FileAttachment (#2)
- docci.file.normalize_name:with_file_name_extract - If false don't extract file name from raw name (#3)

## [0.4.0] - 2019-05-13

### Added 

- docci.file.FileAttachment.content_json - return content as dict with content base64 

## [0.3.1] - 2019-05-13

### Fixed 

- docci.file.FileAttachment.content_disposition - percent encoding instead of plus encoding 

## [0.3.0] - 2019-05-11

### Added

- docci.file.FileAttachment.name - name without restricted chars like \/:*?"<>|
- docci.file.FileAttachment.mimetype - mimetype like application/octet-stream from extension
- docci.file.list_dir_files - return directory name and its files as FileAttachment
- docci.zip.raw_to_zip - convert path, bytes, stream, FileAttachment to ZipFile
- docci.zip.zip_files - zip files into single archive
- docci.zip.zip_dirs - zip directories into single archive

## [0.2.0] - 2019-05-11

### Added 

- docci.file.FileAttachment.content_disposition - convert name to Content-Disposition urlencoded headed

## [0.1.0] - 2019-05-06

### Added

- docci.file.FileAttachment - base class for document management - dataclass of file name and content
- docci.file.FileAttachment.content_stream - convert content to BytesIO stream
- docci.file.FileAttachment.content_base64 - convert content to base64 binary string
- docci.file.FileAttachment.load_from_base64 - decode base64 str, create FileAttachment with decoded content
- docci.file.FileAttachment.load/save - load/save FileAttachment to disk
- docci.file.FileAttachment.extension - return FileAttachment name extension
- docci.file.FileAttachment.name_without_extension - return FileAttachment name without extension
- docci.file.extract_file_name - extract file name from path
- docci.zip.list_zip_files - list zip archive files as FileAttachment