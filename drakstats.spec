%define version 0.23.1
%define name drakstats
%define release %mkrel 2

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
