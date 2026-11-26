#!/usr/bin/env python3
"""Compare a folder with its backup copy and report what is missing or different.

Usage:
    python3 backup_checker.py SOURCE BACKUP [--checksum]

Checks every file in SOURCE against BACKUP. By default files are compared
by size; with --checksum they are compared by content as well.
"""

import argparse
import hashlib
import sys
from pathlib import Path


def collect(root):
    """Return {relative path: Path} for every file under root."""
    files = {}
    for path in sorted(root.rglob("*")):
        if path.is_file():
            files[str(path.relative_to(root))] = path
    return files


def total_size(files):
    """Return (file count, total bytes) for a {name: Path} mapping."""
    return len(files), sum(p.stat().st_size for p in files.values())


def file_hash(path):
    """Return the SHA-256 hash of a file's contents."""
    digest = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", help="the original folder")
    parser.add_argument("backup", help="the backup copy to check")
    parser.add_argument("--checksum", action="store_true",
                        help="also compare file contents, not just sizes")
    args = parser.parse_args(argv)

    source = Path(args.source)
    backup = Path(args.backup)
    if not source.is_dir():
        print(f"Error: {args.source} is not a directory.", file=sys.stderr)
        return 1
    if not backup.is_dir():
        print(f"Error: {args.backup} is not a directory.", file=sys.stderr)
        return 1

    src_files = collect(source)
    bak_files = collect(backup)
    src_count, src_bytes = total_size(src_files)
    bak_count, bak_bytes = total_size(bak_files)

    missing = sorted(set(src_files) - set(bak_files))
    extra = sorted(set(bak_files) - set(src_files))
    differ = []
    for name in sorted(set(src_files) & set(bak_files)):
        src_path = src_files[name]
        bak_path = bak_files[name]
        if src_path.stat().st_size != bak_path.stat().st_size:
            differ.append((name, "different size"))
        elif args.checksum and file_hash(src_path) != file_hash(bak_path):
            differ.append((name, "same size, different content"))

    print(f"Source: {source.resolve()}")
    print(f"Backup: {backup.resolve()}")
    print(f"\nFiles in source: {src_count} ({src_bytes} bytes)")
    print(f"Files in backup: {bak_count} ({bak_bytes} bytes)")

    print(f"\nMissing in backup ({len(missing)}):")
    if missing:
        for name in missing:
            print(f"  {name}")
    else:
        print("  (none)")

    print(f"\nDifferent ({len(differ)}):")
    if differ:
        for name, reason in differ:
            print(f"  {name} — {reason}")
    else:
        print("  (none)")

    print(f"\nOnly in backup ({len(extra)}):")
    if extra:
        for name in extra:
            print(f"  {name}")
    else:
        print("  (none)")

    problems = len(missing) + len(differ)
    if problems == 0:
        print("\nOK — the backup covers every file in the source.")
        return 0
    print(f"\nBackup needs attention: {len(missing)} missing, {len(differ)} different.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
