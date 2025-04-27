import unittest
import os
from unittest.mock import patch, MagicMock
from scripts.process_study import ArterysClient

class TestArterysClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create a test DICOM file
        os.makedirs('data/input', exist_ok=True)
        with open('data/input/test.dcm', 'wb') as f:
            f.write(b'DICM\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')

    def setUp(self):
        self.client = ArterysClient()

    @patch('requests.post')
    def test_authentication(self, mock_post):
        mock_response = MagicMock()
        mock_response.json.return_value = {'access_token': 'test_token'}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response

        token = self.client._authenticate()
        self.assertEqual(token, 'test_token')

    @patch('requests.post')
    def test_upload_study(self, mock_post):
        mock_response = MagicMock()
        mock_response.json.return_value = {'id': 'test_id'}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response

        result = self.client.upload_study('data/input/test.dcm')
        self.assertEqual(result['id'], 'test_id')

    @patch('requests.post')
    def test_analyze_study(self, mock_post):
        mock_response = MagicMock()
        mock_response.json.return_value = {'job_id': 'test_job'}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response

        result = self.client.analyze_study('test_id')
        self.assertEqual(result['job_id'], 'test_job')

    @classmethod
    def tearDownClass(cls):
        # Clean up test files
        if os.path.exists('data/input/test.dcm'):
            os.remove('data/input/test.dcm')

if __name__ == '__main__':
    unittest.main()