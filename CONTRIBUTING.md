# Contributing

This is primarily a portfolio project, but improvements are welcome.

## Development workflow

1. Create a branch for the change.
2. Keep AWS-specific values out of source control.
3. Run the local test suite.
4. Verify documentation and examples use placeholders.
5. Open a pull request with a concise explanation of the change.

## Local checks

```bash
python -m pip install -r requirements-dev.txt
python -m compileall lambda tests
pytest -q
```

## AWS changes

Do not test destructive EC2 operations against production resources. Use a dedicated lab instance and the automation tag.
