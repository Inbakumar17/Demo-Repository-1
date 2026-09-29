# Python Open Source Challenge

Welcome! Each issue file contains an existing, intentionally incomplete Python program and checks. Your task is to understand the code, repair the TODOs, run the checks, and contribute a focused Pull Request. Work only on the issue assigned to you.

## Contribution workflow

1. Fork the repository.
2. Clone your fork.
3. Select your assigned issue.
4. Create a branch for your change.
5. Open the matching `issue N.py` file.
6. Understand the existing code and find its TODO comments.
7. Repair the code without replacing the program from scratch.
8. Run the file with Python and make all built-in checks pass.
9. Commit your changes.
10. Push your branch.
11. Create a Pull Request describing the repair.
12. Respond to maintainer review; once approved, the change can be merged.

You may use ChatGPT, GitHub Copilot, or other AI tools. You are responsible for understanding the changes they suggest, testing them locally, and validating that they meet the issue requirements.

## Run an issue

Issue filenames contain spaces, so quote the path when running a file, for example:

```sh
python "issue 1.py"
```

The starter checks are expected to fail until the incomplete implementation is repaired. A successful repair prints `All checks passed!`.
