# Arterys Project Setup Guide

## Prerequisites
- Python 3.8+
- DCMTK tools (for DICOM validation)
- Arterys API credentials

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Nambili-Samuel/arterys-project.git
   cd arterys-project
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment:
   - Copy `.env/arterys.example` to `.env/arterys.env`
   - Add your API credentials
   - Configure settings in `config/` files

## Usage

- Process a single DICOM file:
   ```bash
   python scripts/process_study.py data/input/sample.dcm --workflow cardiac_mri
   ```

- Process all DICOM files in a directory:
   ```bash
   python scripts/batch_process.py data/input --output_dir data/batch_output
   ```
