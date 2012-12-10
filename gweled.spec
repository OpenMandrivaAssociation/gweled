%define name gweled
%define version 0.9.1
%define release %mkrel 2

Summary: Clone of Bejeweled, align 3 crystals in a row to make them disappear
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://launchpad.net/%name/trunk/%version/+download/%{name}-%{version}.tar.gz
#open without mode will cause a build error
Patch0: gweled-0.9.1-fix-open.patch
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
%apply_patches

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



%changelog
* Thu Apr 05 2012 GÃ¶tz Waschk <waschk@mandriva.org> 0.9.1-2mdv2012.0
+ Revision: 789301
- yearly rebuild

* Mon Apr 04 2011 GÃ¶tz Waschk <waschk@mandriva.org> 0.9.1-1
+ Revision: 650193
- fix build
- update to new version 0.9.1

* Sat Jul 10 2010 GÃ¶tz Waschk <waschk@mandriva.org> 0.8-1mdv2011.0
+ Revision: 550279
- new version
- new URL
- drop all patches
- update file list

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 0.7-8mdv2010.1
+ Revision: 437840
- rebuild

* Thu Apr 02 2009 GÃ¶tz Waschk <waschk@mandriva.org> 0.7-7mdv2009.1
+ Revision: 363464
- rediff patch 2
- update patch 3 for bug 49427 (menu category)

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Thu Aug 14 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.7-6mdv2009.0
+ Revision: 271848
- fix localstatedir
- update license

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Thu Jan 31 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.7-5mdv2008.1
+ Revision: 160647
- fix desktop entry
- fix installation

  + Thierry Vignaud <tv@mandriva.org>
    - drop old menu
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot


* Wed Jan 31 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.7-4mdv2007.0
+ Revision: 115648
- Import gweled

* Wed Jan 31 2007 Götz Waschk <waschk@mandriva.org> 0.7-4mdv2007.1
- port fixes from debian
- build with -export-dynamic

* Thu Aug 03 2006 Götz Waschk <waschk@mandriva.org> 0.7-3mdv2007.0
- xdg menu

* Thu Oct 06 2005 Götz Waschk <waschk@mandriva.org> 0.7-2mdk
- fix buildrequires

* Tue Oct 04 2005 Götz Waschk <waschk@mandriva.org> 0.7-1mdk
- fix file list
- drop patch
- New release 0.7

* Wed Dec 01 2004 Götz Waschk <waschk@linux-mandrake.com> 0.6-1mdk
- fix score dir
- New release 0.6

* Wed Sep 01 2004 Götz Waschk <waschk@linux-mandrake.com> 0.5-1mdk
- add source URL
- New release 0.5

* Sat Apr 10 2004 Götz Waschk <waschk@linux-mandrake.com> 0.4-2mdk
- rebuild for new croco

* Thu Feb 12 2004 Götz Waschk <waschk@linux-mandrake.com> 0.4-1mdk
- add new files
- fix buildrequires
- new version

