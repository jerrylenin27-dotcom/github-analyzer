# GitHub Language Counter

Counts how many public repos a GitHub user has in each programming language.

## How to run

1. Install requests: `pip install requests`
2. Set your GitHub token: `export GITHUB_TOKEN="your-token-here"`
3. Run: `python analyzer.py USERNAME`

## Example

```
python analyzer.py octocat
```

Output:

```
Unknown 5
Ruby 1
CSS 1
HTML 1
```

## Notes

- Create your own GitHub token and store it in the `GITHUB_TOKEN` environment variable. It is never stored in the code.
- Repos with no language set on GitHub are counted as `Unknown`.
- Without a token, GitHub allows 60 requests per hour. With one, the limit is 5,000.