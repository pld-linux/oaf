Summary:	OAF - Objects activated by factories library
Name:		oaf
Version:	0.5.1
Release:	1
License:	GPL
Group:		X11/Libraries
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Source0:	ftp://ftp.gnome.org/pub/GNOME/unstable/sources/oaf/%{name}-%{version}.tar.gz
BuildRequires:	ORBit-devel >= 0.5.1
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	glib-devel >= 1.2.0
BuildRequires:	libxml-devel
BuildRequires:	popt-devel >= 1.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Objects activated by factories library.

%package devel
Summary:	Header files etc to develop oaf applications
Summary(pl):	Pliki nag³ówkowe i inne do oaf
Group:		X11/Development/Libraries
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files etc you can use to develop oaf applications.

%description -l pl devel
Pakiet ten zaziewra pliki nag³ówkowe i inne do oaf niezbêdne przy
tworzeniu aplikacji opartych o t± bibliotekê.

%package static
Summary:	Static oaf libraries
Summary(pl):	Biblioteka statyczna oaf
Group:		X11/Development/Libraries
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static oaf libraries.

%description -l pl static
Biblioteka statyczna oaf.

%prep
%setup -q

%build
gettextize --copy --force
LDFLAGS="-s"; export LDFLAGS
%configure \
	--enable-static \
	--enable-more-warnings=no
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf AUTHORS ChangeLog NEWS README TODO

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_bindir}/oaf-client
%attr(755,root,root) %{_bindir}/oaf-run-query
%attr(755,root,root) %{_bindir}/oafd
%{_datadir}/oaf

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/oaf-config
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/*.sh
%{_includedir}/liboaf
%{_aclocaldir}/oaf.m4
%{_datadir}/idl/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
