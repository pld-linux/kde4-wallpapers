# TODO:
%define		orgname		kde-wallpapers
%define		_state		stable
%define		qtver		4.8.3

Summary:	KDE 4 wallpapers
Summary(pl.UTF-8):	Tapety KDE 4
Name:		kde4-wallpapers
Version:	4.10.4
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	4825dcf46d6cde97e89d20f4fe849d17
URL:		http://www.kde.org/
Obsoletes:	kde4-kdebase-workspace-wallpapers
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains KDE wallpapers.

%description -l pl.UTF-8
Ten pakiet zawiera tapety KDE.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	-DLIBEXEC_INSTALL_DIR=%{_libdir}/kde4/libexec \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/wallpapers/Ariya
%{_datadir}/wallpapers/Auros
%{_datadir}/wallpapers/Autumn
%{_datadir}/wallpapers/Azul
%{_datadir}/wallpapers/Blue_Wood
%{_datadir}/wallpapers/Castilla_Sky
%{_datadir}/wallpapers/Elarun
%{_datadir}/wallpapers/Flores
%{_datadir}/wallpapers/Flying_Field
%{_datadir}/wallpapers/Fog_on_the_West_Lake
%{_datadir}/wallpapers/Grass
%{_datadir}/wallpapers/Hanami
%{_datadir}/wallpapers/Horos
%{_datadir}/wallpapers/Media_Life
%{_datadir}/wallpapers/Prato
