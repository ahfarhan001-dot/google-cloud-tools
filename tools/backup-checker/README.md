# backup-checker

Compare a folder with its backup copy and report what is missing or different: files missing in the backup, files that differ in size (or in content, with `--checksum`), files that exist only in the backup, and a total file/size summary for both sides.

## Usage

```bash
# Compare a folder with its backup (by size)
python3 backup_checker.py /path/to/source /path/to/backup

# Compare by content as well (slower, but catches same-size changes)
python3 backup_checker.py /path/to/source /path/to/backup --checksum
```

Requires Python 3.8 or newer. No extra packages.

## Example output

```
Source: /home/user/photos
Backup: /media/drive/photos-backup

Files in source: 120 (8432100 bytes)
Files in backup: 118 (8400000 bytes)

Missing in backup (2):
  2026-11-24.jpg
  notes/todo.txt

Different (0):
  (none)

Only in backup (0):
  (none)

Backup needs attention: 2 missing, 0 different.
```

## Notes

- Both sides are only read, never changed.
- The exit code is `0` when the backup covers every file in the source, and `1` when something is missing or different — so it can be used in a script or a scheduled check.
- Size comparison is fast but cannot catch a file that changed without changing size; use `--checksum` when that matters.
- Hidden files and folders are included in the check.
