# Building RPM

This project falls in the [non-crate Rust project](https://docs.fedoraproject.org/en-US/packaging-guidelines/Rust/#_non_crate_rust_projects) category by Fedora packaging guidelines.

## Dependencies

Dependencies are sourced from the Fedora repos to the best extent possible, and the unresolved crates are specced with `rust2rpm` and built alongside the main program.

## To use

`mock` is not a hard requirement but highly recommended. Without it, you will most likely need an RPM-based system for dependency resolution when building.

`build_rpm.sh` should provide a decent starting point that can be tweaked as you see fit.
