#
# Conditional build:
# _without_gnome	- without gnome extensions packages
#
Summary:	GNOME Structured File library
Summary(pl):	Biblioteka plików strukturalnych dla GNOME
Name:		libgsf
Version:	1.8.0
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/libgsf/1.8/libgsf-%{version}.tar.bz2
# Source0-md5:	104723ba800e47798819b4b94b269f74
URL:		http://www.gnumeric.org/
%{!?_without_gnome:BuildRequires:	ORBit2-devel}
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.0.0
%{!?_without_gnome:BuildRequires:	gnome-vfs2-devel}
BuildRequires:	gtk-doc >= 0.9
%{!?_without_gnome:BuildRequires:	libbonobo-devel >= 2.0.0}
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Requires:	%{name} = %{version}
Requires:	glib2-devel
Requires:	gtk-doc-common
Requires:	libxml2-devel

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
Requires:	%{name}-devel = %{version}

%description static
Package contains static libraries.

%description static -l pl
Statyczne biblioteki libgsf.

%package gnome
Summary:	GNOME specific extensions to libgsf
Summary(pl):	Rozszerzenia GNOME do biblioteki libgsf
Group:		Libraries
Requires:	%{name} = %{version}

%description gnome
GNOME specific extensions to libgsf.

%description gnome -l pl
Rozszerzenia GNOME do biblioteki libgsf.

%package gnome-devel
Summary:	libgsf-gnome header files
Summary(pl):	Pliki nag³ówkowe libgsf-gnome
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}
Requires:	%{name}-gnome = %{version}
Requires:	gnome-vfs2-devel
Requires:	libbonobo-devel

%description gnome-devel
libgsf-gnome header files.

%description gnome-devel -l pl
Pliki nag³ówkowe libgsf-gnome.

%package gnome-static
Summary:	Static libgsf-gnome library
Summary(pl):	Statyczna biblioteka libgsf-gnome
Group:		Development/Libraries
Requires:	%{name}-gnome-devel = %{version}

%description gnome-static
Static libgsf-gnome library.

%description gnome-static -l pl
Statyczna biblioteka libgsf-gnome.

%prep
%setup -q

%build
rm -f missing acinclude.m4
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}/%{name} \
	%{?_without_gnome:--without-gnome}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post   gnome -p /sbin/ldconfig
%postun gnome -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README NEWS
%attr(755,root,root) %{_libdir}/libgsf-?.so.*.*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libgsf-?.la
%attr(755,root,root) %{_libdir}/libgsf-?.so
%dir %{_includedir}/libgsf-1
%{_includedir}/libgsf-1/gsf
%{_pkgconfigdir}/libgsf-?.pc
%{_gtkdocdir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/libgsf-?.a

%if 0%{!?_without_gnome:1}
%files gnome
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgsf-gnome-?.so.*.*

%files gnome-devel
%defattr(644,root,root,755)
%{_libdir}/libgsf-gnome-?.la
%attr(755,root,root) %{_libdir}/libgsf-gnome-?.so
%{_includedir}/libgsf-1/gsf-gnome
%{_pkgconfigdir}/libgsf-gnome-?.pc

%files gnome-static
%defattr(644,root,root,755)
%{_libdir}/libgsf-gnome-?.a
%endif
