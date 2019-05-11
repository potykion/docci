<!-- https://keepachangelog.com/en/1.0.0/ -->

# Changelog

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