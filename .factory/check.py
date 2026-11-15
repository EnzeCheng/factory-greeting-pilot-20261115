from pathlib import Path

if Path("docs/example.txt").read_bytes() != Path(".factory/expected.txt").read_bytes():
    raise SystemExit("Expected the approved greeting with one final LF.")
print("Greeting matches.")
