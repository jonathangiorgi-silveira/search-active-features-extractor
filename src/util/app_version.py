

def format_app_version(full_version: int) -> str:
    full_version_str = str(full_version)
    minor = full_version_str[-3:]
    major = full_version_str[-5:-3]
    version = full_version_str[:-5]
    return f"{version}.{major}.{minor}"