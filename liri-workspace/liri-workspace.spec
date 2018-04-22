%global snapdate @DATE@
%global snaphash @HASH@

%define modulename workspace

Name:           liri-%{modulename}
Summary:        Liri workspace, applications and plugins
Version:        @VERSION@
Release:        0.1%{?snaphash:.%{snapdate}git%(echo %{snaphash} | cut -c -13)}%{?dist}
License:        GPLv3+
URL:            http://liri.io
Source0:        https://github.com/lirios/%{modulename}/%{?snaphash:archive}%{!?snaphash:releases/download}/%{?snaphash}%{!?snaphash:v%{version}}/%{name}-%{?snaphash}%{!?snaphash:%{version}}.tar.gz

BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5QuickControls2)
BuildRequires:  cmake(GreenIslandClient)
BuildRequires:  cmake(Vibe)
%if 0%{?fedora} >= 23
BuildRequires:  cmake(Qt5GStreamer)
%endif
%if 0%{?fedora} < 23
BuildRequires:  qt5-gstreamer-devel
%endif
BuildRequires:  pkgconfig(gio-2.0) >= 2.31.0
BuildRequires:  pkgconfig(dbus-1)

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  desktop-file-utils

Requires:       fluid

Requires:       dejavu-sans-fonts
Requires:       dejavu-serif-fonts
Requires:       dejavu-sans-mono-fonts
Requires:       google-droid-sans-fonts
Requires:       google-noto-sans-fonts
Requires:       google-noto-serif-fonts


%description
Liri runtime components.


%prep
%setup -q -n %{?snaphash:%{modulename}-%{snaphash}}%{!?snaphash:%{name}-%{version}}


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

%find_lang %{name} --all-name --with-qt


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/io.liri.*.desktop


%posttrans
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :


%postun
if [ $1 -eq 0 ]; then
  glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi


%files -f %{name}.lang
%license LICENSE.GPLv3
%doc AUTHORS.md README.md
%{_bindir}/*
%{_sysconfdir}/xdg/autostart/*.desktop
%{_datadir}/applications/*.desktop
%{_sysconfdir}/xdg/menus/*
%{_datadir}/desktop-directories/*
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/liri-workspace/translations/*.qm
%{_kf5_qtplugindir}/platformthemes/liriplatformtheme.so
