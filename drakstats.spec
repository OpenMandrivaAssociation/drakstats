%define version 0.23.2
%define name drakstats
%define release %mkrel 4

Summary:	The Mandriva Linux installed rpm gathering tool
Name:		%{name}
Version:	%{version}
Release:	%{release}
#cvs source
# http://www.mandrivalinux.com/en/cvs.php3
Source0:	%{name}-%{version}.tar.bz2
License:	GPL
URL:		http://wiki.mandriva.com/en/Tools/DrakStats
Group:		System/Configuration/Packaging
Requires:	drakxtools >= 10.2, rpmstats >= 0.4-1mdk, perl-SOAP-Lite, perl-URPM
Requires:	perl-libwww-perl
BuildArch:	noarch
BuildRequires: perl-MDK-Common-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
Drakstats is a GUI frontend to rpmstats which retrieves statistics about
installed rpm packages and give users the CHOICE to send it to a remote
server for global package usage statistics.
The final goal is to help us shape the future package choice of the 
upcoming releases of the distro.
Drakstats is also a handy tool to optimize install based packages by 
helping the user remove unused software.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
make PREFIX=%{buildroot} install

#menu
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-drakstats.desktop << EOF
[Desktop Entry]
Name=Packages Stats
Comment=Mandriva Linux packages stats
Exec=/usr/sbin/%{name}
Icon=drakstats
Type=Application
Categories=X-MandrivaLinux-CrossDesktop;GTK;System;PackageManager;
EOF

#install lang
%{find_lang} %{name}

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_menus}
%{update_icon_cache hicolor}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%{clean_icon_cache hicolor}
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc README NEWS
%{_prefix}/sbin/*
%{_datadir}/%{name}
%{_datadir}/applications/mandriva-*.desktop
%{_miconsdir}/*.png
%{_iconsdir}/*.png
%{_liconsdir}/*.png
%{_iconsdir}/hicolor/16x16/apps/%{name}.png
%{_iconsdir}/hicolor/32x32/apps/%{name}.png
%{_iconsdir}/hicolor/48x48/apps/%{name}.png


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.23.2-3mdv2011.0
+ Revision: 663862
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 0.23.2-2mdv2011.0
+ Revision: 604825
- rebuild

* Wed May 26 2010 Christophe Fergeau <cfergeau@mandriva.com> 0.23.2-1mdv2010.1
+ Revision: 546248
- 0.23.2
- translation updates

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.23.1-3mdv2010.1
+ Revision: 522515
- rebuilt for 2010.1

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.23.1-2mdv2010.0
+ Revision: 413398
- rebuild

* Wed Apr 15 2009 Thierry Vignaud <tv@mandriva.org> 0.23.1-1mdv2009.1
+ Revision: 367434
- translation updates

* Mon Mar 30 2009 Thierry Vignaud <tv@mandriva.org> 0.23-1mdv2009.1
+ Revision: 362303
- translation updates

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.22-4mdv2009.1
+ Revision: 350880
- rebuild

* Tue Sep 30 2008 Thierry Vignaud <tv@mandriva.org> 0.22-3mdv2009.0
+ Revision: 289963
- translation updates

* Thu Sep 25 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.21-3mdv2009.0
+ Revision: 288023
- requires perl-libwww-perl

* Tue Sep 23 2008 Olivier Blin <oblin@mandriva.com> 0.21-2mdv2009.0
+ Revision: 287596
- use System category for menu (thanks to Frederik Himpe, #43118)

* Mon Sep 22 2008 Thierry Vignaud <tv@mandriva.org> 0.21-1mdv2009.0
+ Revision: 286970
- translation updates

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 0.20-1mdv2009.0
+ Revision: 218424
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Thu Apr 03 2008 Thierry Vignaud <tv@mandriva.org> 0.20-1mdv2008.1
+ Revision: 192161
- translation updates

* Tue Mar 25 2008 Thierry Vignaud <tv@mandriva.org> 0.19-1mdv2008.1
+ Revision: 190112
- translation updates

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 0.18-2mdv2008.1
+ Revision: 149352
- rebuild
- drop old menu
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Oct 01 2007 Thierry Vignaud <tv@mandriva.org> 0.18-1mdv2008.0
+ Revision: 94270
- updated translation

* Tue Sep 25 2007 Thierry Vignaud <tv@mandriva.org> 0.17-1mdv2008.0
+ Revision: 92929
- updated translations

* Wed Aug 22 2007 Olivier Blin <oblin@mandriva.com> 0.16-1mdv2008.0
+ Revision: 69088
- 0.16: use maintainers.mandriva.com instead of qa (#32751)

* Mon May 21 2007 Olivier Blin <oblin@mandriva.com> 0.15-1mdv2008.0
+ Revision: 29150
- add NEWS file
- remove COPYING file
- 0.15

* Wed Apr 25 2007 Adam Williamson <awilliamson@mandriva.org> 0.14-1mdv2008.0
+ Revision: 18103
- package fd.o-compliant icons

* Tue Apr 24 2007 Olivier Blin <oblin@mandriva.com> 0.13-1mdv2008.0
+ Revision: 17957
- update url (of course it has a homepage!)
- 0.13: do not crash when sending stats (#29649)
- Import drakstats



* Sat Sep 16 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.12-1mdv2007.0
- use %%mkrel
- XDG menu

* Wed Nov 30 2005 Olivier Blin <oblin@mandriva.com> 0.11-1mdk
- install locales in /usr/share, not /share

* Sat May  7 2005 Daouda LO <daouda@mandriva.com> 0.10-1mdk
- mandriva switch

* Mon Mar 14 2005 Daouda LO <daouda@mandrakesoft.com> 0.10-0.8mdk
- po updates 

* Tue Feb 22 2005 Daouda LO <daouda@mandrakesoft.com> 0.10-0.7mdk
- display warning when noatime is set on / or /usr partition (better check)
- po updates 

* Sat Feb 12 2005 Daouda LO <daouda@mandrakesoft.com> 0.9-0.6mdk
- change description to less scary one (wildman)
- po updates

* Thu Feb 10 2005 Daouda LO <daouda@mandrakesoft.com> 0.9-0.5mdk
- run as root

* Wed Feb  9 2005 Daouda LO <daouda@mandrakesoft.com> 0.9-0.4mdk
- remove unused package through rpmdrake (--search option)
- preload cache file to decrease startup time load 
- Explicitly 'compute stats'
- drakstats is partly useless when noatime set on / or /usr
- po updates

* Sun Jan 23 2005 Daouda LO <daouda@mandrakesoft.com> 0.9-0.3mdk
- po update 

* Sat Jan 22 2005 Daouda LO <daouda@mandrakesoft.com> 0.9-0.2mdk
- added --root option rpmdrake-remove call (Thanx to Moshe Caspi)

* Fri Jan 21 2005 Daouda LO <daouda@mandrakesoft.com> 0.9-0.1mdk
- first mdk package 
