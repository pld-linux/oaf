Summary:	OAF - Objects activated by factories library
Summary(pl):	Biblioteka OAF
Summary(pt_BR):	Sistema de ativação de objetos para o GNOME
Name:		oaf
Version:	0.6.8
Release:	3
License:	GPL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt_BR):	X11/Bibliotecas
Group(ru):	X11/âÉÂÌÉÏÔÅËÉ
Group(uk):	X11/â¦ÂÌ¦ÏÔÅËÉ
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/oaf/%{name}-%{version}.tar.bz2
BuildRequires:	ORBit-devel >= 0.5.1
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	gtk-doc
BuildRequires:	glib-devel >= 1.2.0
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	libwrap-devel
BuildRequires:	libxml-devel
BuildRequires:	popt-devel >= 1.5
BuildRequires:	scrollkeeper
Prereq:		/sbin/ldconfig
Prereq:		scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	liboaf0

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define         _sysconfdir     /etc/X11/GNOME

%description
Objects activated by factories library for GNOME. It uses ORBit.

%description -l pl
Obiekty aktywowane przez agentów dla GNOME. U¿ywa ORBit-a.

%description -l pt_BR
Sistema de ativação de objetos para o GNOME. Usa o ORBit.

%package devel
Summary:	Header files etc to develop oaf applications
Summary(pl):	Pliki nag³ówkowe i inne do oaf
Summary(pt_BR):	Bibliotecas e arquivos de inclusão para o OAF
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(uk):	X11/òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name} = %{version}
Requires:	popt-devel
Obsoletes:	liboaf0-devel

%description devel
Header files etc you can use to develop oaf applications.

%description -l pl devel
Pakiet ten zawiera pliki nag³ówkowe i inne do oaf niezbêdne przy
tworzeniu aplikacji opartych o t± bibliotekê.

%description -l pt_BR devel
Bibliotecas e arquivos de inclusão para o OAF.

%package static
Summary:	Static oaf libraries
Summary(es):	Libraries estáticas for OAF
Summary(pl):	Biblioteka statyczna oaf
Summary(pt_BR):	Bibliotecas estáticas para o OAF
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(uk):	X11/òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name}-devel = %{version}

%description static
Static oaf libraries.

%description -l es static
Libraries estáticas for OAF.

%description -l pl static
Biblioteka statyczna oaf.

%description -l pt_BR static
Bibliotecas estáticas para o OAF.

%prep
%setup -q

%build
sed -e s/AM_GNOME_GETTEXT/AM_GNU_GETTEXT/ configure.in > configure.in.tmp
mv -f configure.in.tmp configure.in
rm -f missing
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

%find_lang %{name}

%post
/sbin/ldconfig
/usr/bin/scrollkeeper-update

%postun
/sbin/ldconfig
/usr/bin/scrollkeeper-update

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_bindir}/oaf-[^c]*
%attr(755,root,root) %{_bindir}/oaf-client
%attr(755,root,root) %{_bindir}/oafd
%{_datadir}/oaf
%{_datadir}/idl/*
%{_mandir}/man1/*
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

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
