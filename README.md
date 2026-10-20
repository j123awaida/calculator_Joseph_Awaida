# Lab 6 Automatic Builds with PyBuilder and Make

Joseph Awaida

This project implements the graded calculator exercise and includes the optional Makefile workflow. The calculator supports addition, subtraction, multiplication, division, modulus, exponentiation, and square root. Division and modulus reject a zero divisor with ValueError; square root rejects negative inputs. Modulus follows Python's remainder convention, including negative operands. Power follows Python's exponentiation rules.

## Setup and run

Use Python 3.10 or later (validated with Python 3.13).

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pyb run_unit_tests
pyb publish
```

On Windows activate using `.venv\Scripts\activate` instead. PyBuilder installs its plugin dependencies automatically, so the initial build needs internet access.

To run the same tests without PyBuilder:

```sh
python -m unittest tests.unittest.calculator_Joseph_Awaida.test_calculator_Joseph_Awaida -v
```

## Build process

`build.py` loads the core, unittest, dependency installation, and distribution plugins. It explicitly sets the source and test directories and changes the test filename pattern to `test_*`, matching the lab's filenames. This prevents a misleading successful build that discovers zero tests. `pyb run_unit_tests` discovers and runs 10 test methods. `pyb publish` runs the build lifecycle, tests the project, prepares the distribution, and creates source and wheel archives under `target/dist/`.

The module-level `name`, `version`, and `default_task` settings are PyBuilder metadata. The default `pyb` command publishes the project.

## Optional Makefile

Activate the virtual environment first. Make requires GNU Make or a compatible implementation.

| Command | Purpose |
| --- | --- |
| `make install_deps` or `make install` | Install the pinned developer tools from requirements.txt. |
| `make test` | Run calculator tests through PyBuilder. |
| `make lint` | Check source, tests, and build.py with flake8. |
| `make build` or `make package` | Test and create the package through PyBuilder publish. |
| `make clean` | Remove generated PyBuilder build outputs. |
| `make all` | Run clean, dependency installation, tests, lint, and packaging in order. |

Make gives repeated tasks short, consistent commands. The all recipe invokes each stage sequentially so cleanup cannot race with a build even if parallel make is requested. The Python and PyBuilder executables can be overridden, for example `make test PYB=.venv/bin/pyb`.

## Submission

The repository contains the complete calculator sources, unit tests, build.py, requirements.txt, Makefile, and documentation. `evidence/` contains the actual successful build log showing the project base directory and build duration. The lab also requests a terminal screenshot: run `pyb run_unit_tests` and capture the successful build summary in your terminal. Submit a text file containing the repository URL, as directed by the course submission instructions, and grant repository access to NourSN2004, HusseinMoukalled, and RanimTahmoush.

PyBuilder reference: https://pybuilder.io/documentation/tutorial
