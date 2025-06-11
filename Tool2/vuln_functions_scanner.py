"""
vuln_functions_scanner.py version 1.0

Scans C/C++, Java, Python, C#, and Perl source files for vulnerable functions/methods.
Patterns are loaded from per-language JSON files in the 'patterns/' directory.
Supports updating those JSON files by appending new patterns without duplicates.
Strips out both line comments and block comments before scanning to avoid false positives in commented code.
"""

import os, re, json, sys, argparse

# Directory where per-language JSON pattern files live
PATTERNS_DIR = os.path.join(os.path.dirname(__file__), "patterns")

# Map language keys to (pattern file name, list of file extensions)
LANGUAGE_CONFIG = {
    "c_cpp":  ("c_cpp_patterns.json",   [".c", ".cpp", ".cc", ".h", ".hpp"]),
    "java":   ("java_patterns.json",    [".java"]),
    "python": ("python_patterns.json",  [".py"]),
    "csharp": ("csharp_patterns.json",  [".cs"]),
    "perl":   ("perl_patterns.json",    [".pl"]),
}

# Blank out block comments or docstrings to preserve line numbers
def remove_block_comments(content, ext):
    def blank(m): return "\n" * m.group(0).count("\n")
    if ext in [".c",".cpp",".cc",".h",".hpp",".java",".cs"]:
        return re.sub(r"/\*.*?\*/", blank, content, flags=re.DOTALL)
    if ext == ".py":
        return re.sub(r'("""[\s\S]*?"""|\'\'\'[\s\S]*?\'\'\')', blank, content, flags=re.DOTALL)
    if ext == ".pl":
        content = re.sub(r'(?m)^=[A-Za-z]+\b.*?^=cut\s*$\n?', blank, content, flags=re.DOTALL)
        return re.sub(r'(<<[\'"]?(\w+)[\'"]?\n[\s\S]*?\n\2)', blank, content, flags=re.MULTILINE)
    return content

# Determine line-comment delimiter based on file extension
def get_comment_delimiter(path):
    ext = os.path.splitext(path)[1].lower()
    if ext in [".py",".pl"]: return "#"
    if ext in [".c",".cpp",".cc",".h",".hpp",".java",".cs"]: return "//"
    return None

# Strip comments from a line
def strip_comments(line, delimiter):
    if not delimiter: return line
    return line.split(delimiter, 1)[0]

# Load and pre-compile regex patterns for a given language
def load_language_patterns(lang):
    if lang not in LANGUAGE_CONFIG:
        print(f"[warning] Unknown language '{lang}'.")
        return None
    filename, extensions = LANGUAGE_CONFIG[lang]
    path = os.path.join(PATTERNS_DIR, filename)
    if not os.path.isfile(path):
        print(f"[warning] Missing pattern file: {path}")
        return None
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"[warning] Failed to read {path}: {e}")
        return None
    if not isinstance(data, list):
        print(f"[warning] {path} does not contain a JSON list.")
        return None
    loaded = []
    for entry in data:
        if not (isinstance(entry, dict) and "pattern" in entry and "description" in entry):
            print(f"[warning] Skipping invalid entry in {path}: {entry}")
            continue
        try:
            regex = re.compile(entry["pattern"], re.IGNORECASE)
        except re.error as e:
            print(f"[warning] Invalid regex '{entry['pattern']}': {e}")
            continue
        for ext in extensions:
            loaded.append({
                "regex": regex,
                "description": entry["description"],
                "extension": ext,
            })
    return loaded

# Append entries from a custom JSON into an existing pattern file
def update_language_patterns(lang, custom_json_path):
    if lang not in LANGUAGE_CONFIG:
        print(f"[error] Unknown language '{lang}'."); return
    filename, _ = LANGUAGE_CONFIG[lang]
    dest = os.path.join(PATTERNS_DIR, filename)
    if not os.path.isfile(dest):
        print(f"[error] Pattern file not found: {dest}"); return
    try:
        existing = json.load(open(dest, encoding="utf-8"))
    except Exception as e:
        print(f"[error] Cannot read {dest}: {e}"); return
    if not isinstance(existing, list):
        print(f"[error] {dest} is not a JSON list."); return
    existing_patterns = {
        entry.get("pattern")
        for entry in existing
        if isinstance(entry, dict) and "pattern" in entry
    }
    try:
        custom = json.load(open(custom_json_path, encoding="utf-8"))
    except Exception as e:
        print(f"[error] Cannot load custom JSON: {e}"); return
    if not isinstance(custom, list):
        print(f"[error] Custom JSON must be a list."); return
    combined = existing.copy()
    added = 0
    for entry in custom:
        if not (isinstance(entry, dict)
                and "pattern" in entry
                and "description" in entry):
            print(f"[warning] Skipping invalid custom entry: {entry}")
            continue
        pat = entry["pattern"]
        if pat in existing_patterns:
            continue
        combined.append(entry)
        existing_patterns.add(pat)
        added += 1
    try:
        with open(dest, "w", encoding="utf-8") as f:
            json.dump(combined, f, indent=2)
        print(f"[info] Updated '{lang}' patterns: {added} new entr{'y' if added == 1 else 'ies'}.")
    except Exception as e:
        print(f"[error] Writing {dest}: {e}")

# Find all files under a directory matching the given extensions
def gather_source_files(directory, extensions):
    files = []
    for root, _, names in os.walk(directory):
        for name in names:
            if any(name.lower().endswith(ext) for ext in extensions):
                files.append(os.path.join(root, name))
    return files

# Scan one file, remove block comments, strip line comments, and apply regexes
def scan_file(path, patterns):
    ext = os.path.splitext(path)[1].lower()
    try:
        raw = open(path, encoding="utf-8", errors="ignore").read()
    except Exception as e:
        print(f"[error] Opening {path}: {e}")
        return []
    cleaned = remove_block_comments(raw, ext)
    delimiter = get_comment_delimiter(path)
    findings = []
    for lineno, raw_line in enumerate(cleaned.splitlines(), start=1):
        code = strip_comments(raw_line, delimiter)
        if not code.strip():
            continue
        for pat in patterns:
            if pat["extension"] != ext:
                continue
            if pat["regex"].search(code):
                findings.append({
                    "file": path,
                    "line": lineno,
                    "snippet": code.strip(),
                    "description": pat["description"],
                })
    return findings

# Print a human-readable report to the console
def generate_report(sources, findings, display):
    if not display:
        return
    print("\n===== Scan Summary =====")
    print(f"Total files scanned: {len(sources)}")
    for s in sources:
        print(f"  {s}")
    print("\n===== Findings =====")
    if not findings:
        print("No vulnerable functions or methods found.")
        return
    total = len(findings)
    counts = {}
    for f in findings:
        counts.setdefault(f["file"], 0)
        counts[f["file"]] += 1
    print(f"Total occurrences: {total}")
    print("Occurrences by file:")
    for path, cnt in counts.items():
        print(f"  {path}: {cnt} occurrence{'s' if cnt != 1 else ''}")
    print("\nDetails:")
    for idx, f in enumerate(findings, start=1):
        print(f"{idx}. {f['file']}:{f['line']}  [{f['description']}]  {f['snippet']}")

# Save a JSON report to a file
def save_report_json(sources, findings, output_path):
    report = {"scanned_files": sources, "findings": findings}
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2)
        print(f"[info] JSON report written to: {output_path}")
    except Exception as e:
        print(f"[error] Writing JSON report: {e}")

# Save a TXT report to a file
def save_report_txt(sources, findings, output_path):
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write("===== Scan Summary =====\n")
            f.write(f"Total files scanned: {len(sources)}\n")
            for s in sources:
                f.write(f"  {s}\n")
            f.write("\n===== Findings =====\n")
            if not findings:
                f.write("No vulnerable functions or methods found.\n")
                return
            total = len(findings)
            counts = {}
            for item in findings:
                counts.setdefault(item["file"], 0)
                counts[item["file"]] += 1
            f.write(f"Total occurrences: {total}\n")
            f.write("Occurrences by file:\n")
            for path, cnt in counts.items():
                f.write(f"  {path}: {cnt} occurrence{'s' if cnt != 1 else ''}\n")
            f.write("\nDetails:\n")
            for idx, item in enumerate(findings, start=1):
                f.write(
                    f"{idx}. {item['file']}:{item['line']}  "
                    f"[{item['description']}]  {item['snippet']}\n"
                )
        print(f"[info] TXT report written to: {output_path}")
    except Exception as e:
        print(f"[error] Writing TXT report: {e}")

# Parse command-line arguments
def parse_args():
    parser = argparse.ArgumentParser(
        description="Scan for vulnerable functions across multiple languages."
    )
    parser.add_argument("--update-patterns", nargs=2, metavar=("LANG","FILE"),
                        help="Append patterns from FILE into patterns/<LANG>_patterns.json")
    parser.add_argument("--lang","-l", nargs="+", choices=list(LANGUAGE_CONFIG.keys()),
                        help="Languages to scan")
    parser.add_argument("--dir","-d", help="Directory to scan")
    parser.add_argument("--display", action="store_true", help="Print to console")
    parser.add_argument("--no-display", action="store_true", help="Suppress console")
    parser.add_argument("--output-json","-o", help="Write JSON report")
    parser.add_argument("--output-txt","-t", help="Write TXT report")
    return parser.parse_args()

# Main entrypoint for handling update or scanning workflow
def main():
    args = parse_args()
    if args.update_patterns:
        lang, path = args.update_patterns
        update_language_patterns(lang, path)
        sys.exit(0)
    if not args.lang or not args.dir:
        print("Error: both --lang and --dir are required for scanning.")
        sys.exit(1)
    all_patterns = []
    extensions_to_scan = set()
    for lang in args.lang:
        patterns = load_language_patterns(lang)
        if patterns is None:
            sys.exit(1)
        all_patterns.extend(patterns)
        _, exts = LANGUAGE_CONFIG[lang]
        extensions_to_scan.update(exts)
    code_dir = args.dir
    if not os.path.isdir(code_dir):
        print(f"Error: '{code_dir}' is not a valid directory.")
        sys.exit(1)
    sources = gather_source_files(code_dir, extensions_to_scan)
    if not sources:
        print(f"No source files with extensions {sorted(extensions_to_scan)} found.")
        sys.exit(0)
    findings = []
    for src in sources:
        findings.extend(scan_file(src, all_patterns))
    display = args.display and not args.no_display
    generate_report(sources, findings, display)
    if args.output_json:
        save_report_json(sources, findings, args.output_json)
    if args.output_txt:
        save_report_txt(sources, findings, args.output_txt)

if __name__ == "__main__":
    main()