# google-cloud-tools

Open-source tools and reusable skills for using Google Cloud carefully. Small, practical things that help you check what your cloud spend is doing and verify that your backups are real — built in the open, free for everyone to use.

## What's inside

### Skills (`skills/`)

Reusable skill packs you can drop into your AI coding setup. Each skill is a single folder with a `SKILL.md` that tells the AI exactly how to do one job well.

| Skill | What it does |
| --- | --- |
| [gcp-cost-check](skills/gcp-cost-check/) | A checklist for reviewing Google Cloud spend — biggest services, idle resources, budget alerts, and what to ask before paying. |

### Tools (`tools/`)

Small command-line tools you can run right away. No setup, no dependencies beyond Python 3.

| Tool | What it does |
| --- | --- |
| [backup-checker](tools/backup-checker/) | Compares a folder with its backup copy and reports files missing in the backup, files that differ, and a total file/size summary. |

## Quick start

```bash
git clone https://github.com/ahfarhan001-dot/google-cloud-tools.git
cd google-cloud-tools

# Check a backup against its source folder
python3 tools/backup-checker/backup_checker.py /path/to/source /path/to/backup
```

Skills are plain Markdown — copy a skill folder into your AI tool's skills directory and it just works.

## About this project

This is a new project, started in November 2026. It is small and growing — there are no download counts or user numbers to show yet, and none are claimed here.

## Roadmap

- More skills: gcp-security-check, cloud-storage-guide
- More tools: cost-report reader, old-snapshot finder
- Every addition stays small, documented, and dependency-free where possible

## Contributing

Found a bug or want to add a skill or tool? Open an issue or a pull request on GitHub. Keep it small, keep it documented, keep it working.

## License

MIT — see [LICENSE](LICENSE).
