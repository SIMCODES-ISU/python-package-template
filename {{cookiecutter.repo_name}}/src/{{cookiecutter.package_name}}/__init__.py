from importlib.metadata import PackageNotFoundError, version  # pragma: no cover

# Dynamically fetch version of the package
try:
    # Replace '__package__' if pyproject.toml:project.name and the package
    # directory under src/ are renamed to no longer match
    __version__ = version(__package__)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"
finally:
    del version, PackageNotFoundError
