Name:           hyprgraphics
Version:        0.1.1
Release:        1
Summary:        Hyprland graphics / resource utilities 
License:        GPL3.0
Group:          Hyprland
URL:            https://github.com/hyprwm/hyprgraphics
Source0:        https://github.com/hyprwm/hyprlang/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  pkgconfig(libunwind-llvm)
BuildRequires:  pkgconfig(hyprutils)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libjxl)
BuildRequires:  pkgconfig(libmagic)

Provides:       hyprgraphics-devel

%description
Hyprgraphics is a small C++ library with graphics / resource related utilities used across the hypr* ecosystem.

%prep
%autosetup -p1
 
%build
%cmake
%make_build
 
%install
%make_install -C build

%files
