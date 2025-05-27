# Privacy Compliance Scanner

An interactive Python tool for detecting privacy-sensitive identifiers in source code, aligned with GDPR and CCPA standards.

## Overview

The Privacy Compliance Scanner is a python command-line application that scans source code for potentially exposed personally identifiable information (PII) and protected health information (PHI). It supports Python, C/C++, Java, and JavaScript and generates actionable, numbered reports.

## Key Features

* **Multi-Language Scanning**: Single Python script covers `.py`, `.c/.cpp/.h`, `.java`, and `.js` files.
* **Interactive Menu**: Scan directories, load custom patterns, review numbered results, export JSON or text reports.
* **Regulation-Aligned Patterns**: Default rules map to GDPR and CCPA categories; easily extendable via JSON for HIPAA, LGPD, and more.
* **Comment Stripping**: Automatically removes inline and full-line comments to reduce false positives.

## Requirements & Design

* **Environment**: Python 3.6 or higher, using standard library modules (`argparse`, `os`, `re`, `json`, `sys`).
* **Modular Architecture**: Organized functions for file scanning (`scan_file`), directory traversal (`scan_directory`), comment stripping, pattern loading, and report generation. See image below for directory of the tool.
  
  ![image](https://github.com/user-attachments/assets/e379a980-cde8-443d-8f5e-9d4350b445f1)

  ![image](https://github.com/user-attachments/assets/f3954a6e-3d0f-40fb-a4b7-aa9e3fb074f0)

* **Interactive CLI**: Menu-driven interface for scanning code, loading custom patterns, reviewing results, and exporting reports without complex flags.
* **Configurable Patterns**: JSON-based pattern files allow easy extension to additional privacy regulations (GDPR, CCPA, HIPAA, LGPD, etc.).
* **Multi-Language Support**: Automatic detection of file types by extension (`.py`, `.c`, `.cpp`, `.cc`, `.h`, `.hpp`, `.java`, `.js`) to apply comprehensive privacy checks.
* **Comment Suppression**: Inline (`//`) and full-line comment (`#`) removal logic ensures accurate matching by ignoring non-code text.
* **Reporting Options**: Generates numbered console listings, JSON output, and plain-text export for integration with code reviews, CI/CD pipelines, or dashboards.

## Usage Guide

Run the scanner:

```bash
python3 privacy_compliance_scanner.py
```

Choose an option:
```bash
===== Privacy Compliance Scanner ======
1) Scan code directory
2) Load custom patterns from JSON
3) View last scan report
4) Save report to JSON file
5) Save report to TXT file
6) Exit
```
Example:

Run as seen in the images below:

![image](https://github.com/user-attachments/assets/37250175-087f-467a-8a5c-757572aa0586)

![image](https://github.com/user-attachments/assets/04b99f2f-e0d9-4c66-93f9-c28aceaa3294)

![image](https://github.com/user-attachments/assets/9bd6d58e-19d2-416e-a884-3f4f321617e1)

![image](https://github.com/user-attachments/assets/398b21ae-8e57-43da-8f26-9fdf845af1dc)

## Configuration and Patterns

Default patterns cover GDPR and CCPA categories. To add or override the default patterns:

1. Create a `patterns.json` with your custom rules:

   ```json
   [
     { "pattern": "\\b(patient_id|mrn|medical_record_number|record_number)\\b", "description": "PHI: medical record number" },
     { "pattern": "\\b(ssn|social_security_number)\\b", "description": "PHI: Social Security Number"}
   ]
   ```
2. In the menu, choose option 2 **Load custom patterns from JSON** and enter the path to your JSON file. It will scan using the custom patterns as shown below.
   
   ![image](https://github.com/user-attachments/assets/2346f00c-3233-4799-88d6-c387903cba65)

   ![image](https://github.com/user-attachments/assets/15e5b2c0-208d-47b2-b960-9c45e717a360)

   ![image](https://github.com/user-attachments/assets/3d93693c-e3ba-4311-b5d7-d90493223dbe)

## Repository Resources

* **Code**: `privacy_compliance_scanner.py`
* **Documentation**: `README.md`
* **Demo Video**: [https://youtu.be/VIDEO\_ID](https://youtu.be/VIDEO_ID)

## Resources

1. “General Data Protection Regulation (GDPR) – legal text,” General Data Protection Regulation (GDPR), Apr. 22, 2024. Available: [https://gdpr-info.eu/](https://gdpr-info.eu/)
2. “California Consumer Privacy Act (CCPA),” State of California - Department of Justice - Office of the Attorney General, Jan. 28, 2025. Available: [https://oag.ca.gov/privacy/ccpa](https://oag.ca.gov/privacy/ccpa)
3. O. for C. Rights, “The HIPAA privacy rule,” HHS.gov, Sep. 27, 2024. Available: [https://www.hhs.gov/hipaa/for-professionals/privacy/index.html](https://www.hhs.gov/hipaa/for-professionals/privacy/index.html)
4. “Brazilian General Data Protection Law (LGPD, English translation),” Oct. 01, 2020. Available: [https://iapp.org/resources/article/brazilian-data-protection-law-lgpd-english-translation/](https://iapp.org/resources/article/brazilian-data-protection-law-lgpd-english-translation/)
5. “re — Regular expression operations,” Python Documentation. Available: [https://docs.python.org/3/library/re.html](https://docs.python.org/3/library/re.html)
6. Atlassian, “Continuous integration vs. delivery vs. deployment | Atlassian,” Atlassian. Available: [https://www.atlassian.com/continuous-delivery/principles/continuous-integration-vs-delivery-vs-deployment](https://www.atlassian.com/continuous-delivery/principles/continuous-integration-vs-delivery-vs-deployment)
7. “Privacy is an afterthought in the software lifecycle. That needs to change. - Stack Overflow,” Jul. 19, 2021. Available: [https://stackoverflow.blog/2021/07/19/privacy-is-an-afterthought-in-the-software-lifecycle-that-needs-to-change/](https://stackoverflow.blog/2021/07/19/privacy-is-an-afterthought-in-the-software-lifecycle-that-needs-to-change/)
8. M. Tahaei, K. Vaniea, and A. Rashid, “Embedding privacy into design through software developers: Challenges and solutions,” IEEE Security & Privacy, vol. 21, no. 1, pp. 49–57, Sep. 2022. Available: [https://doi.org/10.1109/msec.2022.3204364](https://doi.org/10.1109/msec.2022.3204364)
