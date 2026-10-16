%global forgeurl https://github.com/busyoGG/VShot
%bcond check 1

Version:    0.1.10
%forgemeta

Name:       vshot
Release:    1%{?dist}
Summary:    A shortcut tool
License:    GPL-3.0-or-later
URL:        %{forgeurl}
Source0:    %{forgesource}

%global modelbase https://www.modelscope.cn/models/RapidAI/RapidOCR/resolve/v3.9.2/onnx/PP-OCRv6
Source1:    %{modelbase}/det/PP-OCRv6_det_small.onnx
Source2:    %{modelbase}/rec/PP-OCRv6_rec_small.onnx
Source3:    https://github.com/GreatV/oar-ocr/releases/download/v0.7.0/ppocrv6_dict.txt

%description
Strict-freeze Wayland screenshot CLI with Qt interactive overlay and pin server

BuildRequires:  cmake gcc cargo-rpm-macros
Requires:   qt6-qtbase layer-shell-qt onnxruntime libwayland-client

# Vendored dependencies. Fedora either does not ship them, or
# ships them at a version that does not satisfy the constraints.
# Provides:   (crate(avif-serialize/default) >= 0.8.9 with crate(avif-serialize/default) < 0.9.0~)
# Provides:   (crate(oar-ocr) >= 0.9.2 with crate(oar-ocr) < 0.10.0~)
# Provides:   crate(ort) = 2.0.0~rc.13
# Provides:   crate(ort/ndarray) = 2.0.0~rc.13
# Provides:   crate(ort/pkg-config) = 2.0.0~rc.13
# Provides:   crate(ort/std) = 2.0.0~rc.13
# Provides:   crate(ort/tracing) = 2.0.0~rc.13

%prep
%forgesetup
# There seems to be a chicken-and-egg situation that causes this macro to fail to expand... pre-expansion?
%{?cargo_prep}

%generate_buildrequires
%cargo_generate_buildrequires -t

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
cmake -S . -B build-qt \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr
cmake --build build-qt --parallel

%check
%cargo_test

%install
%{__install} -Dpm755 target/rpm/vshot -t %{buildroot}%{_bindir}
%{__install} -Dpm755 build-qt/vshot-qt-ui -t %{buildroot}%{_bindir}
# The OCR models, under the names `src/ocr.rs` looks for.
%{__install} -Dpm644 %{S:1} %{_datadir}/%{name}/models/det.onnx
%{__install} -Dpm644 %{S:2} %{_datadir}/%{name}/models/rec.onnx
%{__install} -Dpm644 %{S:3} %{_datadir}/%{name}/models/dict.txt"
# Authorizes the CLI for KWin's restricted ScreenShot2 D-Bus interface.
%{__install} -Dpm644 vshot.desktop %{_datadir}/applications/%{name}.desktop
# The launcher entry the application menu shows: it opens the settings
# window, which is the one thing vshot can do from a menu (a capture needs
# a destination, so there is nothing sensible to launch bare).
%{__install} -Dpm644 vshot-settings.desktop %{_datadir}/applications/%{name}-settings.desktop
# One scalable icon rather than a size ladder: the shells that read it
# (KDE, GNOME, wlroots launchers) render SVG themselves and ask for the
# size they need, so a ladder would only add files to keep in step.
%{__install} -Dpm644 icons/vshot.svg %{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%files
%{_bindir}/%{name}
%{_bindir}/%{name}-qt-ui
%{_datadir}/%{name}/models/det.onnx
%{_datadir}/%{name}/models/rec.onnx
%{_datadir}/%{name}/models/dict.txt
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-settings.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%license LICENSE
%license LICENSE.dependencies
%license NOTICE

%changelog
%autochangelog
