# Vulnerable Function Scanner

A lightweight, multi-language command-line tool that quickly detects dangerous functions and methods in source code.

## Overview

This tool scans C/C++, Java, Python, C#, and Perl projects for known unsafe functions (e.g. `gets()`, `eval()`, `Runtime.exec()`). Patterns are stored in per-language JSON files under `patterns/`, and you can easily append new rules at runtime without modifying the Python script.

## Key Features

* **Multi-Language Support**: Scan `.c`, `.cpp`, `.h`, `.java`, `.py`, `.cs`, and `.pl` files in a single pass.
* **Configurable Patterns**: Store vulnerability rules in JSON; update via `--update-patterns`.
* **Comment Stripping**: Automatically remove line (`//`, `#`) and block comments (C `/*...*/`, Python docstrings, Perl POD/here-docs) so only executable code is tested.
* **Flexible Reporting**: View results on the console (`--display`), and save them as JSON (`--output-json`) or text (`--output-txt`).

## Requirements & Design
* **Environment**: Python 3.6 or higher, using standard library modules (`os`, `re`, `json`, `sys`, `argparse`).
* **Configurable Patterns**: Each language has its own JSON file under `patterns/` directory. Verify the this directory contains following files:
   * `c_cpp_patterns.json`
   * `java_patterns.json`
   * `python_patterns.json`
   * `csharp_patterns.json`
   * `perl_patterns.json`

## Usage

```bash
# Scan Python and show results
python vuln_functions_scanner.py --lang python --dir ./my_code --display

# Scan C/C++ only, suppress console output, save JSON
python vuln_functions_scanner.py --lang c_cpp --dir ./my_code --no-display --output-json c_cpp_findings.json

# Scan Java, Csharp, Python, Perl and save JSON & TXT
python vuln_functions_scanner.py --lang  java csharp python perl --dir ./my_code --display --output-json findings.json --output-txt findings.txt

# Append new C/C++ patterns
python vuln_functions_scanner.py --update-patterns c_cpp custom_c_cpp.json
```

## Repository Resources

* **Code**: `privacy_compliance_scanner.py`
* **Documentation**: `README.md`
* **Demo Video**: [https://youtu.be/L5NGIU4xIbc](https://youtu.be/L5NGIU4xIbc)

## Resources

1.	"Common C Vulnerabilities," Medium, Available: https://medium.com/@capturethebugs/common-c-vulnerabilities-56ffad22581e
2.	"Unsafe C Functions and Their Replacements," Stack Overflow, Available: https://stackoverflow.com/questions/26558197/unsafe-c-functions-and-the-replacement
3.	"Buffer Overflow," OWASP, Available: https://owasp.org/www-community/vulnerabilities/Buffer_Overflow
4.	"Exploitable Java Functions," Stack Overflow, Available: https://stackoverflow.com/questions/4339611/exploitable-java-functions
5.	"The Dangers of Inherently Dangerous Functions - Understanding CWE-242," Medium, Available: https://medium.com/@tommy.adeoye/the-dangers-of-inherently-dangerous-functions-understanding-cwe-242-and-how-to-avoid-it-in-java-12a5d2ab4f65
6.	"Unsafe C# Functions: Secure Coding Practices," Simeon on Security, Available: https://simeononsecurity.com/articles/unsafe-c-sharp-functions-secure-coding-practices
7.	"C++ Applications Vulnerability Cheat Sheet," DZone, Available: https://dzone.com/articles/c-applications-vulnerability-cheatsheet
8.	"C# Unsafe Code and Pointers," Medium, Available: https://medium.com/@lexitrainerph/c-unsafe-code-and-pointers-a-deep-dive-from-foundations-to-advanced-uses-82c5cd0769dc
9.	"Python Security Documentation," Python Security, Available: https://python-security.readthedocs.io/security.html
10.	"Code Injection in Python: Prevention Examples," Snyk Blog, Available: https://snyk.io/blog/code-injection-python-prevention-examples
11.	"Python Security Pitfalls," Codiga Blog, Available: https://www.codiga.io/blog/python-security-pitfalls/
12.	"Perl Security (perlsec)," Perl Documentation, Available: https://perldoc.perl.org/perlsec
13.	"Perl Documentation (perlpod)," Perl Documentation, Available: https://perldoc.perl.org/perlpod
14.	"Common CGI Security Pitfalls," CGI Security, Available: https://www.cgisecurity.com/lib/sips.html
15.	"OWASP Cheat Sheet Series," OWASP, Available: https://cheatsheetseries.owasp.org/index.html
16.	"CWE-676: Use of Potentially Dangerous Function," MITRE, Available: https://cwe.mitre.org/data/definitions/676.html
17.	"OWASP Top Ten," OWASP, Available: https://owasp.org/www-project-top-ten/
18.	"CWE-699: Development Concepts," MITRE, Available: https://cwe.mitre.org/data/definitions/699.html
19.	"Python Regular Expressions HOWTO," Python Documentation, Available: https://docs.python.org/3/howto/regex.html
20.	"Python Regular Expressions Library," Python Documentation, Available: https://docs.python.org/3/library/re.html
