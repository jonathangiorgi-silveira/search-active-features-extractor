from logging import Logger

from data.repository.features_repository import provide_features_repository

logger = Logger(__name__)

def main():
    try:
        print(f"Program started!")
        logger.debug(msg=f"Program started!")
        repository = provide_features_repository()
        logger.debug(msg=f"Fecthing active features...")
        features = repository.get_active_features()
        logger.debug(msg=f"{len(features)} active features fetched!")
        repository.save_features_to_file(features)
        logger.debug(msg=f"Features saved to file successfully!")
        print(f"Program finished!")
    except Exception as e:
        print(f"Failed to retrieve search results: {e}")
        logger.error(msg=f"Failed to retrieve search results: {e}")

if __name__ == "__main__":
    main()
