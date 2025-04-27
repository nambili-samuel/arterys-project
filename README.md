# Arterys DICOM Processing Project

A Python project for interacting with the Arterys medical imaging AI platform via its API.

## Features
- Upload DICOM studies to Arterys cloud
- Request AI analysis of medical images
- Support for multiple workflows (cardiac, pulmonary, etc.)
- Command-line interface for batch processing

## Getting Started

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Configure your API credentials in `.env/arterys.env`
4. Run the processing script: `python scripts/process_study.py data/input/sample.dcm`

## Documentation
- [API Reference](docs/API_REFERENCE.md)
- [Setup Guide](docs/SETUP.md)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.