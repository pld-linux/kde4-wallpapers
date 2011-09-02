# TODO:
%define		orgname		kde-wallpapers
%define		_state		stable
%define		qtver		4.7.4

Summary:	KDE 4 wallpapers
Summary(pl.UTF-8):	Tapety KDE 4
Name:		kde4-wallpapers
Version:	4.7.1
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	643eade621034d84803db793089a9c24
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
%{_datadir}/wallpapers/Air
%{_datadir}/wallpapers/Aghi
%{_datadir}/wallpapers/Evening
%{_datadir}/wallpapers/Fields_of_Peace
%{_datadir}/wallpapers/Finally_Summer_in_Germany
%{_datadir}/wallpapers/Fresh_Morning
%{_datadir}/wallpapers/Horos
%{_datadir}/wallpapers/Media_Life
%{_datadir}/wallpapers/Plasmalicious
%{_datadir}/wallpapers/Quadros
%{_datadir}/wallpapers/Red_Leaf
%{_datadir}/wallpapers/Autumn
%{_datadir}/wallpapers/Blue_Wood
%{_datadir}/wallpapers/Grass
%{_datadir}/wallpapers/Hanami
