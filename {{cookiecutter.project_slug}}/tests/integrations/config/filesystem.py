from masonite.utils.location import base_path
from masonite.environment import env

DISKS = {
    "default": "local",
    "local": {
        "driver": "file",
        "path": base_path("storage/framework/filesystem"),
    },
    "s3": {
        "driver": "s3",
        "client": env("AWS_CLIENT"),
        "secret": env("AWS_SECRET"),
        "bucket": env("AWS_BUCKET"),
    },
}
