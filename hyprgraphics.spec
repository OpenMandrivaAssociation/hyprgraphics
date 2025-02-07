%define libname %mklibname hyprgraphics
%define devname %mklibname -d hyprgraphics

Name:           hyprgraphics
Version:        0.1.2
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

%description
Hyprgraphics is a small C++ library with graphics / resource related utilities used across the hypr* ecosystem.

%package -n %{libname}
Summary:        Shared library for %{name}
Provides:       hyprgraphics = %{EVRD}

%description -n %{libname}
This package contains the shared library files.

%package -n %{devname}
Summary:        Development files for %{name}
Requires:	      %{libname} = %{EVRD}
Provides:       hyprgraphics-devel = %{EVRD}

%description -n %{devname}
This package contains development files for %{name}.

%prep
%autosetup -p1
 
%build
%cmake
%make_build
 
%install
%make_install -C build

%files -n %{libname}
%{_libdir}/libhyprgraphics.so.0*

%files -n %{devname}
%{_includedir}/hyprgraphics/
%{_libdir}/libhyprgraphics.so
%{_libdir}/pkgconfig/hyprgraphics.pc
