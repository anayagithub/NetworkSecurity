from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig

import sys


if __name__=="__main__":
    try:
        trainingpiplineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpiplineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Initiated the data ingestion")
        dataingestionartifact=data_ingestion.inititate_data_ingestion()
        logging.info("Data Initiation Completed")
        print(dataingestionartifact)
        data_validation_config=DataValidationConfig(trainingpiplineconfig)
        data_validation=DataValidation(dataingestionartifact,data_validation_config)
        logging.info("Initiated the data Validation")
        data_validation_artifacts=data_validation.initiate_data_validation()
        logging.info("datavalidation completed")
        print(data_validation_artifacts)        
       
    except Exception as e:
        raise NetworkSecurityException(e,sys)