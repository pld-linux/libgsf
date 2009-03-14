#
# Conditional build:
%bcond_without	apidocs		# disable gtk-doc
%bcond_without	bonobo		# without bonobo support in GNOME extension
%bcond_without	gnome		# without GNOME extensions packages
%bcond_with	gnomevfs	# use gnome-vfs instead of gio in GNOME extension
%bcond_without	static_libs	# don't build static libraries
#
%if %{without gnome}
%undefine	with_bonobo
%undefine	with_gnomevfs
%endif
Summary:	GNOME Structured File library
Summary(pl.UTF-8):	Biblioteka plików strukturalnych dla GNOME
Name:		libgsf
Version:	1.14.9
Release:	7
License:	LGPL v2.1
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgsf/1.14/%{name}-%{version}.tar.bz2
# Source0-md5:	422a8461927b863780d3579991a915a5
Patch0:		%{name}-no_GConf2_macros.patch
Patch1:		%{name}-gio.patch
URL:		http://www.gnumeric.org/
BuildRequires:	GConf2-devel >= 2.14.0
BuildRequires:	ORBit2-devel >= 1:2.14.3
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake >= 1:1.7.1
BuildRequires:	bzip2-devel
BuildRequires:	gettext-devel
# gio-2.0
BuildRequires:	glib2-devel >= 1:2.16.0
%{?with_gnomevfs:BuildRequires:	gnome-vfs2-devel >= 2.16.1}
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.7}
%{?with_apidocs:BuildRequires:	gtk-doc-automake}
BuildRequires:	intltool
%{?with_bonobo:BuildRequires:	libbonobo-devel >= 2.0.0}
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	pkgconfig
BuildRequires:	python-pygobject-devel >= 2.10.0
# for pygtk-codegen-2.0
BuildRequires:	python-pygtk-devel >= 2:2.10.2
BuildRequires:	rpm-pythonprov
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
Requires:	glib2-devel >= 1:2.16.0
Requires:	libxml2-devel >= 1:2.6.26

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

%description static
Package contains static libraries.

%description static -l pl.UTF-8
Statyczne biblioteki libgsf.

%package apidocs
Summary:	libgsf API documentation
Summary(pl.UTF-8):	Dokumentacja API libgsf
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libgsf API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API libgsf.

%package gnome
Summary:	GNOME specific extensions to libgsf
Summary(pl.UTF-8):	Rozszerzenia GNOME do biblioteki libgsf
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description gnome
GNOME specific extensions to libgsf.

%description gnome -l pl.UTF-8
Rozszerzenia GNOME do biblioteki libgsf.

%package gnome-devel
Summary:	libgsf-gnome header files
Summary(pl.UTF-8):	Pliki nagłówkowe libgsf-gnome
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-gnome = %{version}-%{release}
%{?with_bonobo:Requires:	gnome-vfs2-devel >= 2.16.1}
%{?with_gnomevfs:Requires:	libbonobo-devel >= 2.0.0}

%description gnome-devel
libgsf-gnome header files.

%description gnome-devel -l pl.UTF-8
Pliki nagłówkowe libgsf-gnome.

%package gnome-static
Summary:	Static libgsf-gnome library
Summary(pl.UTF-8):	Statyczna biblioteka libgsf-gnome
Group:		Development/Libraries
Requires:	%{name}-gnome-devel = %{version}-%{release}

%description gnome-static
Static libgsf-gnome library.

%description gnome-static -l pl.UTF-8
Statyczna biblioteka libgsf-gnome.

%package -n gsf-office-thumbnailer
Summary:	Simple document thumbnailer
Summary(pl.UTF-8):	Prosty generator miniatur dokumentów
Group:		X11/Applications
Requires(post,preun):   GConf2
Requires:	%{name}-gnome = %{version}-%{release}

%description -n gsf-office-thumbnailer
Simple document thumbnailer.

%description -n gsf-office-thumbnailer -l pl.UTF-8
Prosty program tworzący miniaturki dokumentów.

%package -n python-gsf
Summary:	Python gsf module
Summary(pl.UTF-8):	Moduł gsf dla Pythona
Group:		Libraries
%pyrequires_eq	python-libs
Requires:	%{name} = %{version}-%{release}
Requires:	python-pygobject >= 2.10.0

%description -n python-gsf
Python gsf library.

%description -n python-gsf -l pl.UTF-8
Biblioteka gsf dla Pythona.

%package -n python-gsf-gnome
Summary:	Python gsf-gnome module
Summary(pl.UTF-8):	Moduł gsf-gnome dla Pythona
Group:		Libraries
%pyrequires_eq	python-libs
Requires:	python-gsf = %{version}-%{release}

%description -n python-gsf-gnome
Python gsf-gnome library.

%description -n python-gsf-gnome -l pl.UTF-8
Biblioteka gsf-gnome dla Pythona.

%prep
%setup -q
%{!?with_gnome:%patch0 -p1}
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static} \
	%{?with_apidocs:--enable-gtk-doc} \
	--with-html-dir=%{_gtkdocdir} \
	%{!?with_gnomevfs:--with-gio} \
%if %{with gnome}
	%{!?with_bonobo:--without-bonobo} \
	--with-gnome-vfs
%else
	--without-bonobo \
	--without-gnome-vfs
%endif
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_includedir}/%{name}-1/gsf-win32
rm -f $RPM_BUILD_ROOT%{py_sitedir}/gsf/*.{la,a}
rm -f $RPM_BUILD_ROOT%{py_sitescriptdir}/gsf/*.py

# used by gsf-gnome/gsf-{input,output}-gnomevfs.h
cp gsf-config.h $RPM_BUILD_ROOT%{_includedir}/%{name}-1

%find_lang %{name}

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

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README NEWS
%attr(755,root,root) %{_bindir}/gsf
%attr(755,root,root) %{_bindir}/gsf-vba-dump
%attr(755,root,root) %{_libdir}/libgsf-1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgsf-1.so.114
%{_mandir}/man1/gsf.1*
%{_mandir}/man1/gsf-vba-dump.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgsf-1.so
%{_libdir}/libgsf-1.la
%dir %{_includedir}/libgsf-1
%{_includedir}/libgsf-1/*.h
%{_includedir}/libgsf-1/gsf
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

%if %{with gnome}
%files gnome
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgsf-gnome-1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgsf-gnome-1.so.114

%files gnome-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgsf-gnome-?.so
%{_libdir}/libgsf-gnome-1.la
%{_includedir}/libgsf-1/gsf-gnome
%{_pkgconfigdir}/libgsf-gnome-1.pc

%if %{with static_libs}
%files gnome-static
%defattr(644,root,root,755)
%{_libdir}/libgsf-gnome-1.a
%endif

%files -n gsf-office-thumbnailer
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gsf-office-thumbnailer
%{_sysconfdir}/gconf/schemas/gsf-office-thumbnailer.schemas
%{_mandir}/man1/gsf-office-thumbnailer.1*
%endif

%files -n python-gsf
%defattr(644,root,root,755)
%dir %{py_sitedir}/gsf
%attr(755,root,root) %{py_sitedir}/gsf/_gsfmodule.so
%dir %{py_sitescriptdir}/gsf
%{py_sitescriptdir}/gsf/*.py[co]

%if %{with gnome}
%files -n python-gsf-gnome
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gsf/gnomemodule.so
%endif
