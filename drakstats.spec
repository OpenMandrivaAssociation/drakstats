Summary:	The Mandriva Linux installed rpm gathering tool
Name:		drakstats
Version:	0.23.2
Release:	9
License:	GPLv2
Group:		System/Configuration/Packaging
Url:		http://wiki.mandriva.com/en/Tools/DrakStats
#cvs source
# http://www.mandrivalinux.com/en/cvs.php3
Source0:	%{name}-%{version}.tar.bz2
BuildArch:	noarch

BuildRequires:	perl-MDK-Common-devel
Requires:	drakxtools
Requires:	perl-libwww-perl
Requires:	perl-SOAP-Lite
Requires:	perl-URPM
Requires:	rpmstats

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
make PREFIX=%{buildroot} install

#menu
mkdir -p %{buildroot}%{_datadir}/applications/
cat > %{buildroot}%{_datadir}/applications/mandriva-drakstats.desktop << EOF
[Desktop Entry]
Name=Packages Stats
Comment=Mandriva Linux packages stats
Exec=/usr/sbin/%{name}
Icon=drakstats
Type=Application
Categories=X-MandrivaLinux-CrossDesktop;GTK;System;PackageManager;
EOF

#install lang
%find_lang %{name}

%files -f %{name}.lang
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
