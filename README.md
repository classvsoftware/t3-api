# t3-api

These are example python scripts that use the [T3 API](https://api.trackandtrace.tools/v2/docs/) to automatically talk to metrc.com

Request additional scripts as needed! Email [matt@trackandtrace.tools](mailto:matt@trackandtrace.tools) or file an issue in this repository.

## Examples

- [license_data_csv.py](license_data_csv.py) is a simple introductory script that securely reads the user's password in the command line, authenticates with the API, loads the active licenses, and writes the data to a CSV file
- [load_all_active_packages.py](load_all_active_packages.py) shows how to load a large number of packages, one page at a time, and writes the package data to a CSV file
- [download_all_outgoing_manifests.py](download_all_outgoing_manifests.py) shows how to download manifest PDFs into one directory, separated by the parent license number
- [write_one_license_outgoing_transfer_data_to_csv.py](write_one_license_outgoing_transfer_data_to_csv.py) shows how to select a single license using a command line menu, and write all outgoing transfers into a CSV file
- [download_all_transfer_coa_pdfs.py](download_all_transfer_coa_pdfs.py) shows how to download all COA PDFs from a single outgoing transfer
