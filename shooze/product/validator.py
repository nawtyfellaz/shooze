import os
import magic
from django.core.exceptions import ValidationError

MIME_TYPE = [
    'application/mp4',
    'video/mp4',
    'video/mpeg',
    'video/webm',
    'audio/webm',
]

def file_validator(file):
    valid_mime_types = MIME_TYPE
    file_mime_type = magic.from_buffer(file.read(), mime=True)
    if file_mime_type not in valid_mime_types:
        raise ValidationError(u'Unsupported file type.')
    valid_file_extensions = ['.webm', '.mp4', '.mpeg']
    ext = os.path.splitext(file.name)[1]
    if ext.lower() not in valid_file_extensions:
        raise ValidationError(u'File format nor supported.')
    # ext = os.path.splitext(value.name)[1]
    # valid_extensions = ['.pdf', '.doc', '.docx']
    # if not ext in valid_extensions:
    #     raise ValidationError(u'File format not supported!')