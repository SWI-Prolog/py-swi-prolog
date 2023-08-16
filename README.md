# Build SWI-Prolog as Python package

This  repository builds  SWI-Prolog  as a  Python  package.  This  has
several  advantages.  The  Python  package  infrastructure provides  a
widely used cross platform way to install packages.  Having SWI-Prolog
as a Python package allows  installing `janus_swi` with a single `pip`
command.

This package does not contain  SWI-Prolog itself.  It uses `GitPython`
to clone  SWI-Prolog into  `swipl-src` and  `cmake_build_extension` to
build it using CMake.

## Installed artefacts

  - Python package `swipl` that provides `swipl.swipl()` and
    `swipl.swipl_ld()`.
  - Executables, currently named `py-swipl` and `py-swipl-ld`.

## Status

This should be considered a proof of concept

## Remaining issues

  - Get version from SWI-Prolog repo
  - Perform a shallow clone to get the source
  - Deal with dependencies.  As is, it is assumed all dependencies
    are present.  How do we deal with external libraries such as
	gmp, odbc, etc?
  - Deal with PGO installation
  - Windows build?
	- Microsoft Visual C++ is problematic
  - Can/should we deal with _variants_, e.g., no GMP for big ints,
    select packages, etc.
