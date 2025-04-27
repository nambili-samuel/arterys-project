import os
import json
import logging
from pydicom import dcmread

logger = logging.getLogger(__name__)

def validate_dicom_file(file_path):
    """Validate that a file is a proper DICOM file"""
    try:
        dcmread(file_path)
        return True
    except Exception as e:
        logger.error(f"DICOM validation failed: {str(e)}")
        return False

def load_config():
    """Load configuration files"""
    config = {}
    try:
        with open('config/api_config.json') as f:
            config['api'] = json.load(f)
        with open('config/settings.json') as f:
            config['settings'] = json.load(f)
        return config
    except Exception as e:
        logger.error(f"Config loading failed: {str(e)}")
        raise

def prepare_output_dir():
    """Ensure output directory exists"""
    os.makedirs('data/output', exist_ok=True)