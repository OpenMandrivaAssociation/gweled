%define name gweled
%define version 0.9.1
%define release %mkrel 1

Summary: Clone of Bejeweled, align 3 crystals in a row to make them disappear
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://launchpad.net/%name/trunk/%version/+download/%{name}-%{version}.tar.gz
License: GPLv2+
Group: Games/Puzzles
URL: https://launchpad.net/gweled
BuildRequires: librsvg-devel
BuildRequires: gtk+2-devel
BuildRequires: libmikmod-devel
BuildRequires: intltool
BuildRoot: %{_tmppath}/%{name}-buildroot

%description
Gweled is a Gnome version of a popular PalmOS/Windows/Java game called
"Bejeweled" or "Diamond Mine". The aim of the game is to make
alignment of 3 or more gems, both vertically or horizontally by
swapping adjacent gems. The game ends when there are no possible moves
left.

%prep
%setup -q

%build
export LDFLAGS="-export-dynamic"
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc NEWS AUTHORS
%attr(2555, root, games) %_bindir/%name
%_datadir/applications/%name.desktop
%_datadir/sounds/%name
%_datadir/%name
%_datadir/pixmaps/%name
%_datadir/icons/hicolor/*/apps/%name.*
%attr(664, games, games) %_localstatedir/games/%name.*.scores

