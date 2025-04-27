# Arterys API Reference

## Authentication
- Endpoint: `/oauth2/token`
- Method: POST
- Content-Type: application/x-www-form-urlencoded
- Parameters:
  - `grant_type`: "client_credentials"
  - `client_id`: Your client ID
  - `client_secret`: Your API key

## Study Upload
- Endpoint: `/api/v2/studies`
- Method: POST
- Headers:
  - `Authorization: Bearer <token>`
  - `Content-Type: application/dicom`
- Body: Raw DICOM file bytes

## Analysis Request
- Endpoint: `/api/v2/analysis`
- Method: POST
- Headers:
  - `Authorization: Bearer <token>`
  - `Content-Type: application/json`
- Body:
  ```json
  {
    "study_id": "<uploaded_study_id>",
    "workflow": "cardiac_mri|lung_ct|etc"
  }