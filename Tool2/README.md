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
* Verify the `patterns/` directory contains these files:

   * `c_cpp_patterns.json`
   * `java_patterns.json`
   * `python_patterns.json`
   * `csharp_patterns.json`
   * `perl_patterns.json`

## Usage

```bash
# Update patterns for C/C++
python3 vuln_functions_scanner.py --update-patterns c_cpp new_c_cpp_patterns.json

# Scan C/C++ and Python code, display, and save reports
python vuln_functions_scanner.py \
  --lang c_cpp python \
  --dir /path/to/code \
  --display \
  --output-json findings.json \
  --output-txt findings.txt
```

## Resources

1. **Common C Vulnerabilities** (Medium)
   [https://medium.com/@capturethebugs/common-c-vulnerabilities-56ffad22581e](https://medium.com/@capturethebugs/common-c-vulnerabilities-56ffad22581e)
2. **Unsafe C Functions and Their Replacements** (Stack Overflow)
   [https://stackoverflow.com/questions/26558197/unsafe-c-functions-and-the-replacement](https://stackoverflow.com/questions/26558197/unsafe-c-functions-and-the-replacement)
3. **Buffer Overflow** (OWASP)
   [https://owasp.org/www-community/vulnerabilities/Buffer\_Overflow](https://owasp.org/www-community/vulnerabilities/Buffer_Overflow)
4. **Exploitable Java Functions** (Stack Overflow)
   [https://stackoverflow.com/questions/4339611/exploitable-java-functions](https://stackoverflow.com/questions/4339611/exploitable-java-functions)
5. **The Dangers of Inherently Dangerous Functions – Understanding CWE-242** (Medium)
   [https://medium.com/@tommy.adeoye/the-dangers-of-inherently-dangerous-functions-understanding-cwe-242-and-how-to-avoid-it-in-java-12a5d2ab4f65](https://medium.com/@tommy.adeoye/the-dangers-of-inherently-dangerous-functions-understanding-cwe-242-and-how-to-avoid-it-in-java-12a5d2ab4f65)
6. **Unsafe C# Functions: Secure Coding Practices** (Simeon on Security)
   [https://simeononsecurity.com/articles/unsafe-c-sharp-functions-secure-coding-practices](https://simeononsecurity.com/articles/unsafe-c-sharp-functions-secure-coding-practices)
7. **C++ Applications Vulnerability Cheat Sheet** (DZone)
   [https://dzone.com/articles/c-applications-vulnerability-cheatsheet](https://dzone.com/articles/c-applications-vulnerability-cheatsheet)
8. **C# Unsafe Code and Pointers** (Medium)
   [https://medium.com/@lexitrainerph/c-unsafe-code-and-pointers-a-deep-dive-from-foundations-to-advanced-uses-82c5cd0769dc](https://medium.com/@lexitrainerph/c-unsafe-code-and-pointers-a-deep-dive-from-foundations-to-advanced-uses-82c5cd0769dc)
9. **Python Security Documentation** (Python Security)
   [https://python-security.readthedocs.io/security.html](https://python-security.readthedocs.io/security.html)
10. **Code Injection in Python: Prevention Examples** (Snyk Blog)
    [https://snyk.io/blog/code-injection-python-prevention-examples](https://snyk.io/blog/code-injection-python-prevention-examples)
11. **Python Security Pitfalls** (Codiga Blog)
    [https://www.codiga.io/blog/python-security-pitfalls/](https://www.codiga.io/blog/python-security-pitfalls/)
12. **Perl Security (perlsec)** (Perl Documentation)
    [https://perldoc.perl.org/perlsec](https://perldoc.perl.org/perlsec)
13. **Perl Documentation (perlpod)** (Perl Documentation)
    [https://perldoc.perl.org/perlpod](https://perldoc.perl.org/perlpod)
14. **Common CGI Security Pitfalls** (CGI Security)
    [https://www.cgisecurity.com/lib/sips.html](https://www.cgisecurity.com/lib/sips.html)
15. **OWASP Cheat Sheet Series** (OWASP)
    [https://cheatsheetseries.owasp.org/index.html](https://cheatsheetseries.owasp.org/index.html)
16. **CWE-676: Use of Potentially Dangerous Function** (MITRE)
    [https://cwe.mitre.org/data/definitions/676.html](https://cwe.mitre.org/data/definitions/676.html)
17. **OWASP Top Ten** (OWASP)
    [https://owasp.org/www-project-top-ten/](https://owasp.org/www-project-top-ten/)
18. **CWE-699: Development Concepts** (MITRE)
    [https://cwe.mitre.org/data/definitions/699.html](https://cwe.mitre.org/data/definitions/699.html)
19. **Python Regular Expressions HOWTO** (Python Docs)
    [https://docs.python.org/3/howto/regex.html](https://docs.python.org/3/howto/regex.html)
20. **Python Regular Expressions Library** (Python Docs)
    [https://docs.python.org/3/library/re.html](https://docs.python.org/3/library/re.html)
