# Check Dependency Updates

This is a tool used for checking dependency versions in [`requirements.txt`](https://pip.pypa.io/en/stable/user_guide/#requirements-files) style files.
Inspired by tools such as [npm-check-updates](https://www.npmjs.com/package/npm-check-updates).

Note this is a very simple tool. This is in contrast to tools like [pur](https://github.com/alanhamlett/pip-update-requirements) or [pip-upgrader](https://github.com/simion/pip-upgrader) etc, as if you have pip installed, this does not require any other dependencies, as it uses pip's native vendored dependencies.

This allows this tool to be 'portable' in the sense where you can just take the single python file and use it on any machine with pip installed.
