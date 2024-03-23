import re

def validate_url(url: str):
    regex_pattern = r"^(https?|ftp):\/\/[^\s/$.?#].[^\s]*$"
    return re.match(regex_pattern, url) is not None