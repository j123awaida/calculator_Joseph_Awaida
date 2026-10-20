# Build evidence

`build-screenshot.png` is an unedited screenshot of actual PyBuilder command output in GitHub Actions. It shows 10 passing tests, BUILD SUCCESSFUL, the calculator_Joseph_Awaida base directory, the build completion time, and elapsed time.

The screenshot comes from the Test and package calculator step of this successful run:
https://github.com/j123awaida/calculator_Joseph_Awaida/actions/runs/39384047831

`build.log` records the successful local PyBuilder publish command. `make.log` records successful local Makefile test, lint, and build commands. The local and GitHub runs use separate machines, so their paths and durations differ.
