#
# Conditional build:
%bcond_without	gnome	# without GNOME extensions packages
#
Summary:	GNOME Structured File library
Summary(pl):	Biblioteka plików strukturalnych dla GNOME
Name:		libgsf
Version:	1.12.3
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/libgsf/1.12/%{name}-%{version}.tar.bz2
# Source0-md5:	34b51119d5cbae30be0357ab246e93de
URL:		http://www.gnumeric.org/
%{?with_gnome:BuildRequires:	ORBit2-devel >= 2.8.1}
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	glib2-devel >= 1:2.6.0
%{?with_gnome:BuildRequires:	gnome-vfs2-devel >= 2.4.0}
BuildRequires:	gtk-doc >= 1.0
%{?with_gnome:BuildRequires:	libbonobo-devel >= 2.4.0}
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.4.16
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Requires:	%{name} = %{version}-%{release}
Requires:	bzip2-devel
Requires:	glib2-devel >= 1:2.6.0
Requires:	gtk-doc-common >= 1.0
Requires:	libxml2-devel >= 2.4.16

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
Requires:	%{name}-devel = %{version}-%{release}

%description static
Package contains static libraries.

%description static -l pl
Statyczne biblioteki libgsf.

%package gnome
Summary:	GNOME specific extensions to libgsf
Summary(pl):	Rozszerzenia GNOME do biblioteki libgsf
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description gnome
GNOME specific extensions to libgsf.

%description gnome -l pl
Rozszerzenia GNOME do biblioteki libgsf.

%package gnome-devel
Summary:	libgsf-gnome header files
Summary(pl):	Pliki nag³ówkowe libgsf-gnome
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-gnome = %{version}-%{release}
Requires:	gnome-vfs2-devel >= 2.4.0
Requires:	libbonobo-devel >= 2.4.0

%description gnome-devel
libgsf-gnome header files.

%description gnome-devel -l pl
Pliki nag³ówkowe libgsf-gnome.

%package gnome-static
Summary:	Static libgsf-gnome library
Summary(pl):	Statyczna biblioteka libgsf-gnome
Group:		Development/Libraries
Requires:	%{name}-gnome-devel = %{version}-%{release}

%description gnome-static
Static libgsf-gnome library.

%description gnome-static -l pl
Statyczna biblioteka libgsf-gnome.

%package -n gsf-office-thumbnailer
Summary:	Simple document thumbnailer
Summary(pl):	Prosty generator miniatur dokumentów
Group:		X11/Applications
Requires(post,preun):   GConf2
Requires:	%{name}-gnome = %{version}-%{release}

%description -n gsf-office-thumbnailer
Simple document thumbnailer.

%description -n gsf-office-thumbnailer -l pl
Prosty program tworz±cy miniaturki dokumentów.

%prep
%setup -q

%build
rm -f acinclude.m4
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}/%{name} \
	%{!?with_gnome:--without-gnome}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_includedir}/%{name}-1/gsf-win32

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post   gnome -p /sbin/ldconfig
%postun gnome -p /sbin/ldconfig

%post -n gsf-office-thumbnailer
%gconf_schema_install gsf-office-thumbnailer.schemas

%preun -n gsf-office-thumbnailer
%gconf_schema_uninstall gsf-office-thumbnailer.schemas

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

%if %{with gnome}
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

%files -n gsf-office-thumbnailer
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gsf-office-thumbnailer
%{_sysconfdir}/gconf/schemas/gsf-office-thumbnailer.schemas
%{_mandir}/man1/gsf-office-thumbnailer.1.gz
