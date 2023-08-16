import os
import cmake_build_extension
import setuptools
import git

packages = [
    "PDT",
    "RDF",
    "archive",
    "bdb",
    "chr",
    "clib",
    "clpqr",
    "cpp",
    "cql",
    "http",
    "inclpr",
    "libedit",
    "ltx2htm",
    "mqi",
    "nlp",
    "odbc",
    "paxos",
    "pcre",
    "pengines",
    "pldoc",
    "plunit",
    "protobufs",
    "readline",
    "redis",
    "semweb",
    "sgml",
    "ssl",
    "stomp",
    "sweep",
    "swipy",
    "table",
    "tipc",
    "utf8proc",
    "xpce",
    "yaml",
    "zlib",
]

def updateSrc():
    repo = git.Repo("swipl-src")
    repo.remotes.origin.pull()
    for pkg in packages:
        repo.git.execute(command=['git', 'submodule', 'update', '--init',
                                  os.path.join("packages", pkg)])

# Broken, see https://github.com/gitpython-developers/GitPython/issues/944
#       repo.submodule(sm).update(init=True)

def download():
    if os.path.isdir("swipl-src"):
        pass
    else:
        from git.repo.base import Repo
        Repo.clone_from("https://github.com/SWI-Prolog/swipl-devel.git", "swipl-src")

download()
updateSrc()

if "CIBUILDWHEEL" in os.environ and os.environ["CIBUILDWHEEL"] == "1":
    CIBW_CMAKE_OPTIONS = ["-DCMAKE_INSTALL_LIBDIR=lib"]
else:
    CIBW_CMAKE_OPTIONS = []

setuptools.setup(
    cmdclass=dict(build_ext=cmake_build_extension.BuildExtension),
    ext_modules=[
        cmake_build_extension.CMakeExtension(
            name="BuildAndInstall",
            install_prefix="swipl",
            expose_binaries=["bin/swipl"],
            cmake_configure_options=[
                f"-DSWIPL_PACKAGE_LIST={';'.join(packages)}",
            ]
            + CIBW_CMAKE_OPTIONS,
        ),
    ],
)
