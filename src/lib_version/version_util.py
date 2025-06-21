import importlib.metadata


class VersionUtil:
    @staticmethod
    def get_version(package_name: str = "lib-version") -> str:
        try:
            return importlib.metadata.version(package_name)
        except importlib.metadata.PackageNotFoundError:
            return "unknown"
