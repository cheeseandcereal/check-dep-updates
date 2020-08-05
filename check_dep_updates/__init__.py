#!/usr/bin/env python3
from typing import Tuple, List
import sys
import pathlib
import argparse

__author__ = "Adam Crowder"
__version__ = "0.1.0"


def exit_failure(message: str) -> None:
    print(message, file=sys.stderr)
    sys.exit(1)


try:
    from pip._vendor import requests
    from pip._vendor.packaging import version
except ImportError:
    exit_failure("Unable to import vendored dependencies from pip. Is pip installed?")


def get_current_package_version(package: str, include_prerelease: bool = False) -> version.Version:
    r = requests.get(f"https://pypi.org/pypi/{package}/json")
    ver_return = version.parse("0")
    if r.status_code == 200:
        for release in r.json().get("releases", []):
            ver = version.parse(release)
            if include_prerelease or not ver.is_prerelease:
                ver_return = max(ver_return, ver)
    else:
        print(f"Warning: Invalid response from pypi for package {package} | Status code {r.status_code}")
    return ver_return


def get_packages(requirements_file_path: pathlib.Path) -> List[Tuple[str, str]]:
    packages = []
    with open(str(requirements_file_path), "r") as f:
        for line in f:
            line = line.rstrip()
            if line:
                package = ""
                if "==" in line:
                    index = line.find("==")
                    package = line[:index]
                    version = line[index + 2 :]
                elif ">=" in line:
                    index = line.find(">=")
                    package = line[:index]
                    version = line[index + 2 :]
                if package:
                    if "[" in package:
                        package = package[: package.find("[")]
                    packages.append((package, version))
    return packages


def main() -> None:
    parser = argparse.ArgumentParser(description="Check a pip requirements file for updated packages")
    parser.add_argument("-f", "--file", help="Provide alternative file for checking", action="store", default="requirements.txt")
    flags = parser.parse_args()
    requirements_file = pathlib.Path(flags.file)
    if not requirements_file.exists():
        exit_failure("{} file not found".format(requirements_file))
    for package in get_packages(requirements_file):
        pkg_name = package[0]
        pkg_version = package[1]
        latest_version = str(get_current_package_version(pkg_name))
        if latest_version != "0" and latest_version != pkg_version:
            print(f"Newer version of {pkg_name}: {latest_version}")
    print("Done")


if __name__ == "__main__":
    main()
