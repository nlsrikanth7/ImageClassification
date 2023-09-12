from dataclasses import dataclass
from pathlib import Path


# Entity _ which return type should the function return.
#Data Ingestion related config

# @dataclass(frozen=True)
# class DataIngestionConfig:
#     root_dir:Path
#     source_URL:str
#     local_data_file:Path
#     unzip_dir:Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path