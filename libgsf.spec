#
# Conditional build:
%bcond_without	apidocs		# disable gtk-doc
%bcond_without	static_libs	# don't build static libraries

Summary:	GNOME Structured File library
Summary(pl.UTF-8):	Biblioteka plików strukturalnych dla GNOME
Name:		libgsf
Version:	1.14.47
Release:	1
License:	LGPL v2.1
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgsf/1.14/%{name}-%{version}.tar.xz
# Source0-md5:	20bf9933128210d7a9f920a34198d22f
URL:		https://github.com/GNOME/libgsf
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake >= 1:1.7.1
BuildRequires:	bzip2-devel
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gdk-pixbuf2-devel >= 2.0
BuildRequires:	gettext-tools >= 0.19.6
BuildRequires:	glib2-devel >= 1:2.36.0
BuildRequires:	gobject-introspection-devel >= 1.0.0
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.12}
%{?with_apidocs:BuildRequires:	gtk-doc-automake >= 1.12}
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires:	glib2 >= 1:2.36.0
Requires:	libxml2 >= 1:2.6.26
Obsoletes:	libgsf-gnome
Obsoletes:	python-gsf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library for reading and writing structured files (e.g. MS OLE and
Zip).

%description -l pl.UTF-8
Biblioteka do odczytu i zapisu plików strukturalnych (np. MS OLE lub
Zip).

%package devel
Summary:	Support files necessary to compile applications with libgsf
Summary(pl.UTF-8):	Pliki do kompilowania aplikacji używających libgsf
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	bzip2-devel
Requires:	glib2-devel >= 1:2.36.0
Requires:	libxml2-devel >= 1:2.6.26
Obsoletes:	libgsf-gnome-devel

%description devel
Headers, and support files necessary to compile applications using
libgsf.

%description devel -l pl.UTF-8
Pliki nagłówkowe i inne potrzebne do kompilowania aplikacji
używających libgsf.

%package static
Summary:	libgsf static libraries
Summary(pl.UTF-8):	Statyczne biblioteki libgsf
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libgsf-gnome-static

%description static
Package contains static libraries.

%description static -l pl.UTF-8
Statyczne biblioteki libgsf.

%package apidocs
Summary:	libgsf API documentation
Summary(pl.UTF-8):	Dokumentacja API libgsf
Group:		Documentation
Requires:	gtk-doc-common
BuildArch:	noarch

%description apidocs
libgsf API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API libgsf.

%package -n gsf-office-thumbnailer
Summary:	Simple document thumbnailer
Summary(pl.UTF-8):	Prosty generator miniatur dokumentów
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description -n gsf-office-thumbnailer
Simple document thumbnailer.

%description -n gsf-office-thumbnailer -l pl.UTF-8
Prosty program tworzący miniaturki dokumentów.

%prep
%setup -q

%build
%{?with_apidocs:%{__gtkdocize}}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	%{!?with_static_libs:--disable-static} \
	%{?with_apidocs:--enable-gtk-doc} \
	--enable-introspection \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgsf-1.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README NEWS
%attr(755,root,root) %{_bindir}/gsf
%attr(755,root,root) %{_bindir}/gsf-vba-dump
%attr(755,root,root) %{_libdir}/libgsf-1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgsf-1.so.114
%{_libdir}/girepository-1.0/Gsf-1.typelib
%{_mandir}/man1/gsf.1*
%{_mandir}/man1/gsf-vba-dump.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgsf-1.so
%dir %{_includedir}/libgsf-1
%{_includedir}/libgsf-1/gsf
%{_datadir}/gir-1.0/Gsf-1.gir
%{_pkgconfigdir}/libgsf-1.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgsf-1.a
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gsf
%endif

%files -n gsf-office-thumbnailer
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gsf-office-thumbnailer
%{_datadir}/thumbnailers/gsf-office.thumbnailer
%{_mandir}/man1/gsf-office-thumbnailer.1*
