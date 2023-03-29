name = "jsoncpp"

authors = [
    "jsoncpp"
]

version = "0.7.0.sse.1.0.0"

description = \
    """
    Json parser
    """

with scope("config") as c:
    # Determine location to release: internal (int) vs external (ext)

    # NOTE: Modify this variable to reflect the current package situation
    release_as = "ext"

    # The `c` variable here is actually rezconfig.py
    # `release_packages_path` is a variable defined inside rezconfig.py

    import os
    if release_as == "int":
        c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_INT"]
    elif release_as == "ext":
        c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_EXT"]

    #c.build_thread_count = "physical_cores"

requires = [
]

private_build_requires = [
]

variants = [
    ["platform-linux", "arch-x86_64", "os-centos-7"],
]

uuid = "repository.jsoncpp"

def pre_build_commands():
    command("source /opt/rh/devtoolset-6/enable")

def commands():
    # NOTE: REZ package versions can have ".sse." to separate the external
    # version from the internal modification version.
    split_versions = str(version).split(".sse.")
    external_version = split_versions[0]
    internal_version = None
    if len(split_versions) == 2:
        internal_version = split_versions[1]

    env.JSONCPP_VERSION = external_version
    env.JSONCPP_PACKAGE_VERSION = external_version
    if internal_version:
        env.JSONCPP_PACKAGE_VERSION = internal_version

    env.JSONCPP_ROOT.append("{root}")
    env.JSONCPP_LOCATION.append("{root}")

    env.JSONCPP_INCLUDE_DIR = "{root}/include"
    env.JSONCPP_LIBRARY_DIR = "{root}/lib64"

    env.PATH.append("{root}/lib64")
    env.LD_LIBRARY_PATH.append("{root}/lib64")
