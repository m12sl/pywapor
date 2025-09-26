import fsspec


def get_filesystem(path: str) -> fsspec.AbstractFileSystem:
    if path.startswith("s3://"):
        fs = fsspec.filesystem("s3")
    elif path.startswith("gcs://") or path.startswith("gs://"):
        fs = fsspec.filesystem("gcs")
    else:
        fs = fsspec.filesystem("file")
    return fs
