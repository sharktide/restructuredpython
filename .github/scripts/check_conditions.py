import os
import subprocess
import sys

def main():
    # Get the GitHub actor (user who triggered the PR)
    actor = os.getenv("GITHUB_ACTOR")
    if actor == "github/sharktide":
        print("✅ Approved: User is github/sharktide.")
        sys.exit(0)

    # Get changed files in the PR
    result = subprocess.run(
        ["git", "diff", "--name-only", "origin/${GITHUB_BASE_REF}..origin/${GITHUB_HEAD_REF}"],
        capture_output=True,
        text=True,
        check=True,
    )
    changed_files = result.stdout.splitlines()

    if "pyproject.toml" in changed_files:
        print("❌ Failed: pyproject.toml is modified and the user is not github/sharktide.")
        sys.exit(1)

    print("✅ Approved: No restricted changes.")
    sys.exit(0)

if __name__ == "__main__":
    main()
