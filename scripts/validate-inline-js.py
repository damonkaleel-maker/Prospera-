#!/usr/bin/env python3
"""Syntax-check inline JavaScript in the Android WebView HTML asset."""
from html.parser import HTMLParser
from pathlib import Path
import subprocess
import sys
import tempfile

HTML_FILE = Path("app/src/main/assets/index.html")

class ScriptExtractor(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.scripts = []
        self.current = None
        self.current_type = ""

    def handle_starttag(self, tag, attrs):
        if tag.lower() != "script":
            return
        attrs = dict(attrs)
        script_type = (attrs.get("type") or "").strip().lower()
        if attrs.get("src"):
            self.current = None
            return
        if script_type and script_type not in ("text/javascript", "application/javascript", "module", "text/ecmascript", "application/ecmascript"):
            self.current = None
            return
        self.current = []
        self.current_type = script_type

    def handle_data(self, data):
        if self.current is not None:
            self.current.append(data)

    def handle_endtag(self, tag):
        if tag.lower() == "script" and self.current is not None:
            code = "".join(self.current)
            if code.strip():
                self.scripts.append(code)
            self.current = None

def main():
    if not HTML_FILE.is_file():
        print(f"ERROR: required app asset not found: {HTML_FILE}", file=sys.stderr)
        return 1
    html = HTML_FILE.read_text(encoding="utf-8")
    parser = ScriptExtractor()
    parser.feed(html)
    if not parser.scripts:
        print("ERROR: no inline JavaScript blocks found to validate", file=sys.stderr)
        return 1
    node = subprocess.run(["node", "--version"], capture_output=True, text=True)
    if node.returncode:
        print("ERROR: Node.js is required for JavaScript syntax validation", file=sys.stderr)
        return 1
    with tempfile.TemporaryDirectory() as temp_dir:
        for index, code in enumerate(parser.scripts, start=1):
            path = Path(temp_dir) / f"inline-script-{index}.js"
            path.write_text(code, encoding="utf-8")
            result = subprocess.run(["node", "--check", str(path)], text=True, capture_output=True)
            if result.returncode:
                print(f"FAILED: inline JavaScript block {index}", file=sys.stderr)
                print(result.stdout, file=sys.stderr)
                print(result.stderr, file=sys.stderr)
                return result.returncode
    print(f"PASS: JavaScript syntax validated in {len(parser.scripts)} inline script block(s) using {node.stdout.strip()}.")
    print("NOTE: syntax validation does not replace functional tests on Android.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
