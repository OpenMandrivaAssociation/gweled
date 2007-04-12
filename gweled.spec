%define name gweled
%define version 0.7
%define release %mkrel 4

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
License: GPL
Group: Games/Puzzles
URL: http://sebdelestaing.free.fr/gweled/
BuildRequires: librsvg-devel
BuildRequires: libgnomeui2-devel
BuildRequires: libglade2.0-devel
BuildRequires: libmikmod-devel
BuildRequires: ImageMagick
BuildRequires: desktop-file-utils
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
%patch2 -p0 -b .ppc


%build
export LDFLAGS="-export-dynamic"
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
install -d %buildroot{%_menudir,%_liconsdir,%_miconsdir,%_iconsdir}
cat << EOF > $RPM_BUILD_ROOT/%{_menudir}/%name
?package(%name):command="%name" \
icon="%name.png" needs="X11" section="More Applications/Games/Puzzles" \
title="Gweled" longtitle="Clone of Bejeweled" xdg="true"
EOF

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-MoreApplications-Games-Puzzles" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*


#icons
ln -s %_datadir/pixmaps/%name.png %buildroot/%_liconsdir
convert -scale 32x32 %name.png %buildroot/%_iconsdir/%name.png
convert -scale 16x16 %name.png %buildroot/%_miconsdir/%name.png

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus

%postun
%clean_menus

%files
%defattr(-,root,root)
%doc NEWS AUTHORS
%attr(2555, root, games) %_bindir/%name
%_datadir/applications/%name.desktop
%_datadir/sounds/%name
%_datadir/pixmaps/%name.png
%_datadir/pixmaps/%name
%_datadir/%name
%attr(664, games, games) %_var/lib/games/%name.easy.scores
%_iconsdir/%name.png
%_liconsdir/%name.png
%_miconsdir/%name.png
%_menudir/%name


