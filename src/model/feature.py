from typing import Optional

class Feature:

    def __init__(self, 
        search_id: str, 
        search_key: str,
        name: str,
        description: str,
        min_ios_version: int = 0,
        min_android_version: int = 0,
        extra_params: dict = {},
        tags: list[str] = [],
    ) -> None:
        self.search_id = search_id
        self.search_key = search_key
        self.name = name
        self.description = description
        self.min_ios_version = min_ios_version
        self.min_android_version = min_android_version
        self.extra_params = extra_params
        self.tags = tags

    def deeplink(self, prefix: Optional[str] = None) -> str:
        path = self.extra_params.get("path", "")
        if prefix and not path.startswith(prefix):
            return f"{prefix}/{path}"
        return path
    
    def icon_name_v3(self) -> str:
        return self.extra_params.get("icon_name_v3", "")
    
    def feature_flag(self) -> str:
        return self.extra_params.get("segmentation_flag", "")
