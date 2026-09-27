#!/usr/bin/env python3
"""Create a distributable ZIP package of the reporting suite.

This script bundles all essential files into a shareable archive suitable for
stakeholder distribution, backup, or offline review.
"""
import shutil
import subprocess
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUTPUT_ZIP = ROOT / f"trillionbg-sportybet-reporting-{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"

FILES_TO_INCLUDE = [
    "README.md",
    "INVESTOR_BRIEF.md",
    "scripts/alert_action_csv_generation.py",
    "tests/test_csv_generation.py",
    "exports/Settlement_Ledger.csv",
    "exports/Operational_Dashboard.csv",
    "exports/Risk_Compliance.csv",
    "exports/Alert_Action_Report.json",
    ".github/workflows/csv-alert-action.yml",
    "LICENSE",
]


def create_zip() -> None:
    print(f"🔄 Creating ZIP package: {OUTPUT_ZIP}")

    try:
        with shutil.ZipFile(OUTPUT_ZIP, "w", shutil.ZIP_DEFLATED) as zf:
            for file_path in FILES_TO_INCLUDE:
                full_path = ROOT / file_path
                if full_path.exists():
                    arcname = f"trillionbg-sportybet-reporting/{file_path}"
                    zf.write(full_path, arcname=arcname)
                    print(f"  ✓ Added: {file_path}")
                else:
                    print(f"  ⚠ Skipped (not found): {file_path}")

        print(f"\n✅ ZIP package created successfully: {OUTPUT_ZIP}")
        print(f"📦 Size: {OUTPUT_ZIP.stat().st_size / 1024:.1f} KB")
        print(f"\n📤 Ready to share with stakeholders.")

    except Exception as e:
        print(f"❌ Error creating ZIP: {e}")
        raise


if __name__ == "__main__":
    create_zip()
