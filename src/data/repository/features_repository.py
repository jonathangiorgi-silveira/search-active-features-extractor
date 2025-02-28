from abc import (ABC, abstractmethod)
from typing import Optional

from model.feature import Feature
from data.datasource.features_datasource import (
    FeaturesDataSource,
    features_datasource
)
from transformer.text_transformation_pipeline import (
    TextTransformationPipeline,
    AccentRemovalTransformer, 
    TextTransformationPipeline, 
    WhiteSpaceToUnderscoreReplacement, 
    LowerCaseTransformer,
    SpecialCharacterRemovalTransformer
)
from util import (file_writter, app_version)

class FeaturesRepository(ABC):
    
    @abstractmethod
    def get_active_features(self) -> list[dict]:
        pass

    @abstractmethod
    def save_features_to_file(self, features: list[Feature]) -> None:
        pass

class FeaturesRepositoryImpl(FeaturesRepository):
    
    def __init__(
        self, 
        datasource: FeaturesDataSource,
        item_id_pipeline: TextTransformationPipeline
    ) -> None:
        self.datasource = datasource
        self.item_id_pipeline = item_id_pipeline

    def get_active_features(self) -> list[dict]:
        return self.datasource.get_active_features()

    def save_features_to_file(self, features: list[Feature]) -> None:
        header = (
            "id_pesquisavel",
            "chave_pesquisavel",
            "id_item",
            "descricao",
            "titulo",
            "subtitulo",
            "versao_min_ios",
            "versao_min_android",
            "deeplink",
            "icone",
            "feature_flag",
            "palavras_chave"
        )
        lines = (self.__map_feature_to_line(feature) for feature in features)
        file_writter.write_to_csv(
            file_path="results/opensearch_to_contenthub.csv",
            header=header,
            lines=lines
        )

    def __map_feature_to_line(self, feature: Feature) -> tuple:
        return (
            feature.search_id,
            feature.search_key,
            self.item_id_pipeline.transform(feature.name),
            feature.description,
            feature.name,
            feature.description,
            app_version.format_app_version(feature.min_ios_version) if feature.min_ios_version > 0 else "",
            app_version.format_app_version(feature.min_android_version) if feature.min_android_version > 0 else "",
            feature.deeplink(prefix="picpay://picpay"),
            feature.icon_name_v3(),
            feature.feature_flag(),
            ",".join(feature.tags)
        )
    
def provide_features_repository(
    datasource: FeaturesDataSource = features_datasource,
    item_id_pipeline: Optional[TextTransformationPipeline] = None
) -> FeaturesRepository:
    pipeline = item_id_pipeline or TextTransformationPipeline(
        transformers=(
            AccentRemovalTransformer(),
            SpecialCharacterRemovalTransformer(),
            WhiteSpaceToUnderscoreReplacement(),
            LowerCaseTransformer()
        )
    )
    return FeaturesRepositoryImpl(
        datasource=datasource,
        item_id_pipeline=pipeline
    )