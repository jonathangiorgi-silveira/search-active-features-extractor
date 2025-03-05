from abc import (ABC, abstractmethod)

from model.feature import Feature

from data.opensearch.opensearch_client_wrapper import (
    OpenSearchClientWrapper,
    opensearch_client_wrapper
)

class FeaturesDataSource(ABC):
    
    @abstractmethod
    def get_active_features(self) -> list[Feature]:
        pass

class FeaturesDataSourceImpl(FeaturesDataSource):
    __index: str = "feature-0002"

    def __init__(self, client_wrapper: OpenSearchClientWrapper) -> None:
        self.client_wrapper = client_wrapper

    def get_active_features(self) -> list[Feature]:
        query = {
            "size": 1000,
            "_source": [
                "origin_id", 
                "search_id", 
                "name", 
                "description", 
                "min_ios_version", 
                "min_android_version", 
                "extra_parameters", 
                "tags"
            ],
            "query": {
                "match": {
                    "is_active": True
                }
            }
        }
        try:
            self.client_wrapper.open()
            hits = self.client_wrapper.execute_query(
                query=query,
                index=self.__index
            )
        finally:
            self.client_wrapper.close_quietly()
        features: list[Feature] = []
        for hit in hits:
            source = hit["_source"]
            min_ios_version = source["min_ios_version"]
            min_android_version = source["min_android_version"]
            extra_params = {param["name"]: param["value"] for param in source["extra_parameters"]}
            feature = Feature(
                search_id=source["search_id"],
                search_key=source["origin_id"],
                name=source["name"],
                description=source["description"],
                min_ios_version=min_ios_version if min_ios_version else 0,
                min_android_version=min_android_version if min_android_version else 0,
                extra_params=extra_params,
                tags=source["tags"]
            )
            features.append(feature)
        return features
    
features_datasource: FeaturesDataSource = FeaturesDataSourceImpl(
    client_wrapper=opensearch_client_wrapper
)