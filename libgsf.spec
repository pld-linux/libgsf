Summary:	GNOME Structured File library
Name:		libgsf
Version:	1.3.0
Release:	1
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.gnome.org/pub/GNOME/unstable/sources/libgsf/libgsf-%{version}.tar.bz2
Patch0:		%{name}-am.patch
URL:		http://www.gnumeric.org
BuildRequires:	glib2-devel >= 2.0.0
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library for reading and writing structured files (eg MS OLE and Zip)

%package devel
Summary:	Support files necessary to compile applications with libgsf.
Group:		Development/Libraries
Requires:	libgsf = %{version}

%description devel
Headers, and support files necessary to compile applications using libgsf.

%package static
Summary:	libgsf static libraries.
Group:		Development/Libraries
Requires:	libgsf-devel = %{version}

%description static
Package contains static libraries.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing acinclude.m4
%{__libtoolize}
%{__gettextize}
aclocal -I m4
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -r $RPM_BUILD_ROOT

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

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
