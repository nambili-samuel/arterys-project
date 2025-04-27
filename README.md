# Arterys DICOM Processing Project
<p align="center">
  <img src="https://media.licdn.com/dms/image/v2/C561BAQHB4CAyIvw-oQ/company-background_10000/company-background_10000/0/1636408064637/arterys_cover?e=1746385200&v=beta&t=VbK8JFvGSqZNI_1Jbj3OdtriSs6XkwvvfbTGxizMxEY" alt="Arterys Project Banner" style="width:100%;max-width:1000px;">
</p>

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
