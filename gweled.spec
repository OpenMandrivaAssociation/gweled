%define name gweled
%define version 0.7
%define release %mkrel 8

Summary: Clone of Bejeweled, align 3 crystals in a row to make them disappear
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://sebdelestaing.free.fr/gweled/Release/%{name}-%{version}.tar.bz2
# gw debian patches:
# gw fix double free
Patch: gweled-0.7-fix-double-free.patch
# gw don't load mikmod's disk writer output driver
Patch1: gweled-0.7-mikmod-disable-disk-writers.patch
# gw use gint instead of gchar for the board
Patch2: gweled-ppc.diff
Patch3: gweled-0.7-desktopentry.patch
License: GPLv2+
Group: Games/Puzzles
URL: http://sebdelestaing.free.fr/gweled/
BuildRequires: librsvg-devel
BuildRequires: libgnomeui2-devel
BuildRequires: libglade2.0-devel
BuildRequires: libmikmod-devel
BuildRequires: imagemagick
BuildRoot: %{_tmppath}/%{name}-buildroot

%description
Gweled is a Gnome version of a popular PalmOS/Windows/Java game called
"Bejeweled" or "Diamond Mine". The aim of the game is to make
alignment of 3 or more gems, both vertically or horizontally by
swapping adjacent gems. The game ends when there are no possible moves
left.

%prep
%setup -q
%patch -p1 -b .double-free
%patch1 -p1 -b .disk-writer
%patch2 -p1 -b .ppc
%patch3 -p1 -b .xdg

%build
export LDFLAGS="-export-dynamic"
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

#icons
mkdir -p %buildroot/{%_liconsdir,%_miconsdir}
ln -s %_datadir/pixmaps/%name.png %buildroot/%_liconsdir
convert -scale 32x32 %name.png %buildroot/%_iconsdir/%name.png
convert -scale 16x16 %name.png %buildroot/%_miconsdir/%name.png

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%postun
%clean_menus
%endif

%files
%defattr(-,root,root)
%doc NEWS AUTHORS
%attr(2555, root, games) %_bindir/%name
%_datadir/applications/%name.desktop
%_datadir/sounds/%name
%_datadir/pixmaps/%name.png
%_datadir/pixmaps/%name
%_datadir/%name
%attr(664, games, games) %_localstatedir/games/%name.easy.scores
%_iconsdir/%name.png
%_liconsdir/%name.png
%_miconsdir/%name.png


