from src.data_access.mongo_handler import MongoDBHandler

if __name__ == "__main__":
    MONGO_URI = "mongodb://localhost:27017"
    DB_NAME = "cutoff_db"
    COLLECTION_NAME = "cutoffs"
    FILE_PATH = "cutoff_data.csv"

    handler = MongoDBHandler(MONGO_URI, DB_NAME, COLLECTION_NAME)
    handler.upload_csv(FILE_PATH)
