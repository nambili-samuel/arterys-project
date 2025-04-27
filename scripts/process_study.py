
### scripts/process_study.py
```python
import os
import json
import logging
import requests
from dotenv import load_dotenv
from pydicom import dcmread

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

load_dotenv('.env/arterys.env')

class ArterysClient:
    def __init__(self):
        self.base_url = os.getenv('ARTERYS_API_URL')
        self.api_key = os.getenv('ARTERYS_API_KEY')
        self.client_id = os.getenv('ARTERYS_CLIENT_ID')
        self.token = self._authenticate()
        
    def _authenticate(self):
        """Authenticate with Arterys API"""
        with open('config/api_config.json') as f:
            config = json.load(f)
        
        auth_url = f"{self.base_url}{config['auth_endpoint']}"
        try:
            response = requests.post(
                auth_url,
                data={
                    'grant_type': 'client_credentials',
                    'client_id': self.client_id,
                    'client_secret': self.api_key
                },
                timeout=config.get('timeout', 30)
            response.raise_for_status()
            return response.json()['access_token']
        except Exception as e:
            logger.error(f"Authentication failed: {str(e)}")
            raise
        
    def upload_study(self, dicom_path):
        """Upload DICOM study to Arterys"""
        with open('config/api_config.json') as f:
            config = json.load(f)
        
        # Validate DICOM file
        try:
            dcmread(dicom_path)
        except Exception as e:
            logger.error(f"Invalid DICOM file: {str(e)}")
            raise
        
        upload_url = f"{self.base_url}{config['upload_endpoint']}"
        
        headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/dicom'
        }
        
        try:
            with open(dicom_path, 'rb') as f:
                response = requests.post(
                    upload_url,
                    headers=headers,
                    data=f,
                    timeout=config.get('timeout', 30)
                )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logger.error(f"Upload failed: {str(e)}")
            raise
    
    def analyze_study(self, study_id, workflow=None):
        """Request analysis for uploaded study"""
        with open('config/api_config.json') as f:
            config = json.load(f)
        
        analysis_url = f"{self.base_url}{config['analysis_endpoint']}"
        workflow = workflow or config['default_workflow']
        
        headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        }
        
        payload = {
            'study_id': study_id,
            'workflow': workflow
        }
        
        try:
            response = requests.post(
                analysis_url,
                headers=headers,
                json=payload,
                timeout=config.get('timeout', 30)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logger.error(f"Analysis request failed: {str(e)}")
            raise

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Process DICOM study with Arterys')
    parser.add_argument('dicom_file', help='Path to DICOM file')
    parser.add_argument('--workflow', help='Analysis workflow to use', default=None)
    
    args = parser.parse_args()
    
    client = ArterysClient()
    
    try:
        # Step 1: Upload study
        logger.info("Uploading study...")
        upload_result = client.upload_study(args.dicom_file)
        study_id = upload_result['id']
        logger.info(f"Study uploaded with ID: {study_id}")
        
        # Step 2: Request analysis
        logger.info("Requesting analysis...")
        analysis_result = client.analyze_study(study_id, args.workflow)
        logger.info(f"Analysis job created with ID: {analysis_result['job_id']}")
        
        # Save results
        os.makedirs('data/output', exist_ok=True)
        output_path = f"data/output/{study_id}_result.json"
        with open(output_path, 'w') as f:
            json.dump(analysis_result, f, indent=2)
        
        logger.info(f"Results saved to {output_path}")
        print(f"Success! Results saved to {output_path}")
    except Exception as e:
        logger.error(f"Processing failed: {str(e)}")
        print(f"Error: {str(e)}")
        exit(1)