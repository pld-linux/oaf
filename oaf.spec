Summary:	OAF - Objects activated by factories library
Summary(pl):	Biblioteka OAF
Summary(pt_BR):	Sistema de ativaÁ„o de objetos para o GNOME
Name:		oaf
Version:	0.6.7
Release:	1
License:	GPL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt_BR):	X11/Bibliotecas
Group(ru):	X11/‚…¬Ã…œ‘≈À…
Group(uk):	X11/‚¶¬Ã¶œ‘≈À…
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/oaf/%{name}-%{version}.tar.bz2
Patch0:		%{name}-use_AM_GNU_GETTEXT.patch
Patch1:		%{name}-XML_I18N_MERGE_OAF_RULE.patch
BuildRequires:	ORBit-devel >= 0.5.1
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	gtk-doc
BuildRequires:	glib-devel >= 1.2.0
BuildRequires:	libtool
BuildRequires:	libwrap-devel
BuildRequires:	libxml-devel
BuildRequires:	popt-devel >= 1.5
BuildRequires:	xml-i18n-tools >= 0.9-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Objects activated by factories library for GNOME. It uses ORBit.

%description -l pt_BR
Sistema de ativaÁ„o de objetos para o GNOME. Usa o ORBit.

%package devel
Summary:	Header files etc to develop oaf applications
Summary(pl):	Pliki nag≥Ûwkowe i inne do oaf
Summary(pt_BR):	Bibliotecas e arquivos de inclus„o para o OAF
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	X11/Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}
Requires:	popt-devel

%description devel
Header files etc you can use to develop oaf applications.

%description -l pl devel
Pakiet ten zawiera pliki nag≥Ûwkowe i inne do oaf niezbÍdne przy
tworzeniu aplikacji opartych o t± bibliotekÍ.

%description -l pt_BR devel
Bibliotecas e arquivos de inclus„o para o OAF.

%package static
Summary:	Static oaf libraries
Summary(es):	Libraries est·ticas for OAF
Summary(pl):	Biblioteka statyczna oaf
Summary(pt_BR):	Bibliotecas est·ticas para o OAF
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	X11/Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name}-devel = %{version}

%description static
Static oaf libraries.

%description -l es static
Libraries est·ticas for OAF.

%description -l pl static
Biblioteka statyczna oaf.

%description -l pt_BR static
Bibliotecas est·ticas para o OAF.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
xml-i18n-toolize --copy --force
libtoolize --copy --force
gettextize --copy --force
aclocal
autoconf
automake -a -c
%configure \
	--enable-static \
	--disable-gtk-doc \
	--enable-more-warnings=no
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

gzip -9nf AUTHORS ChangeLog NEWS README TODO oaf-config.xml.sample

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_bindir}/oaf-client
%attr(755,root,root) %{_bindir}/oaf-run-query
%attr(755,root,root) %{_bindir}/oaf-slay
%attr(755,root,root) %{_bindir}/oafd
%{_datadir}/oaf
%dir %{_sysconfdir}/oaf
%config(noreplace) %{_sysconfdir}/oaf/*.xml

%files devel
%defattr(644,root,root,755)
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
