# TODO:
# - split libgsf and libgsf-gnome
Summary:	GNOME Structured File library
Summary(pl):	Biblioteka plików strukturalnych dla GNOME
Name:		libgsf
Version:	1.5.0
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	ftp://ftp.gnome.org/pub/gnome/sources/libgsf/1.5/libgsf-%{version}.tar.bz2
Patch0:		%{name}-am.patch
URL:		http://www.gnumeric.org/
BuildRequires:	ORBit2-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	gnome-vfs2-devel
BuildRequires:	libbonobo-devel >= 2.0.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_gtkdocdir	%{_defaultdocdir}/gtk-doc/html

%description
A library for reading and writing structured files (e.g. MS OLE and
Zip).

%description -l pl
Biblioteka do odczytu i zapisu plików strukturalnych (np. MS OLE lub
Zip).

%package devel
Summary:	Support files necessary to compile applications with libgsf
Summary(pl):	Pliki do kompilowania aplikacji u¿ywaj±cych libgsf
Group:		Development/Libraries
Requires:	libgsf = %{version}

%description devel
Headers, and support files necessary to compile applications using
libgsf.

%description devel -l pl
Pliki nag³ówkowe i inne potrzebne do kompilowania aplikacji
u¿ywaj±cych libgsf.

%package static
Summary:	libgsf static libraries
Summary(pl):	Statyczne biblioteki libgsf
Group:		Development/Libraries
Requires:	libgsf-devel = %{version}

%description static
Package contains static libraries.

%description static -l pl
Statyczne biblioteki libgsf.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing acinclude.m4
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-gtk-doc 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DOC_DIR=%{_gtkdocdir}/\$\(DOC_MODULE\) \
	pkgconfigdir=%{_pkgconfigdir} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README NEWS
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.??
%{_includedir}/libgsf-1
%{_pkgconfigdir}/*.pc
%{_gtkdocdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
