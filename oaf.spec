Summary:	OAF - Objects activated by factories library
Summary(ko):	±×³ð¿ë °´Ã¼ È°¼º ±¸Á¶
Summary(pl):	Biblioteka OAF
Summary(pt_BR):	Sistema de ativação de objetos para o GNOME
Summary(ru):	OAF - ÓÉÓÔÅÍÁ ÁËÔÉ×ÁÃÉÉ ÏÂßÅËÔÏ× GNOME
Summary(uk):	OAF - ÓÉÓÔÅÍÁ ÁËÔÉ×ÁÃ¦§ ÏÂ'¤ËÔ¦× GNOME
Name:		oaf
Version:	0.6.10
Release:	6
License:	GPL
Group:		X11/Libraries
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/oaf/0.6/%{name}-%{version}.tar.bz2
# Source0-md5: ed9aa2ceb70bba34034b3134b22d2729
Patch0:		%{name}-default-search-path.patch
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
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	liboaf0

%define         _sysconfdir     /etc/X11/GNOME

%description
Objects activated by factories library for GNOME. It uses ORBit.

%description -l pl
Obiekty aktywowane przez agentów dla GNOME. U¿ywa ORBit-a.

%description -l pt_BR
Sistema de ativação de objetos para o GNOME. Usa o ORBit.

%description -l ru
OAF (Object Activation Framework) ÐÒÅÄÏÓÔÁ×ÌÑÅÔ ÍÅÈÁÎÉÚÍ ÁËÔÉ×ÁÃÉÉ ÄÌÑ
ËÏÍÐÏÎÅÎÔÏ× GNOME. üÔÏ ÚÁÍÅÎÁ GOAD ÄÌÑ ÐÌÁÔÆÏÒÍÙ GNOME 2.

%description -l uk
OAF (Object Activation Framework) ÎÁÄÁ¤ ÍÅÈÁÎ¦ÚÍ ÁËÔÉ×ÁÃ¦§ ÄÌÑ
ËÏÍÐÏÎÅÎÔ¦× GNOME. ãÅ ÚÁÍ¦ÎÁ GOAD ÄÌÑ ÐÌÁÔÆÏÒÍÉ GNOME 2.

%package devel
Summary:	Header files etc to develop oaf applications
Summary(ko):	OAF¸¦ À§ÇÑ ¶óÀÌºê·¯¸®¿Í Çì´õ ÆÄÀÏ
Summary(pl):	Pliki nag³ówkowe i inne do oaf
Summary(pt_BR):	Bibliotecas e arquivos de inclusão para o OAF
Summary(ru):	æÁÊÌÙ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ ÐÒÏÇÒÁÍÍ Ó ÉÓÐÏÌØÚÏ×ÁÎÉÅÍ OAF
Summary(uk):	æÁÊÌÉ ÄÌÑ ÒÏÚÒÏÂËÉ ÐÒÏÇÒÁÍ Ú ×ÉËÏÒÉÓÔÁÎÎÑÍ OAF
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Requires:	popt-devel
Obsoletes:	liboaf0-devel

%description devel
Header files etc you can use to develop oaf applications.

%description devel -l pl
Pakiet ten zawiera pliki nag³ówkowe i inne do oaf niezbêdne przy
tworzeniu aplikacji opartych o t± bibliotekê.

%description devel -l pt_BR
Bibliotecas e arquivos de inclusão para o OAF.

%description devel -l ru
üÔÏÔ ÐÁËÅÔ ÓÏÄÅÒÖÉÔ ÆÁÊÌÙ, ÎÅÏÂÈÏÄÉÍÙÅ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ ÐÒÏÇÒÁÍÍ,
ÉÓÐÏÌØÚÕÀÝÉÈ OAF.

%description devel -l uk
ãÅÊ ÐÁËÅÔ Í¦ÓÔÉÔØ ÆÁÊÌÉ, ÎÅÏÂÈ¦ÄÎ¦ ÄÌÑ ÒÏÚÒÏÂËÉ ÐÒÏÇÒÁÍ, ÑË¦
×ÉËÏÒÉÓÔÏ×ÕÀÔØ OAF.

%package static
Summary:	Static oaf libraries
Summary(es):	Libraries estáticas for OAF
Summary(pl):	Biblioteka statyczna oaf
Summary(pt_BR):	Bibliotecas estáticas para o OAF
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static oaf libraries.

%description static -l es
Libraries estáticas for OAF.

%description static -l pl
Biblioteka statyczna oaf.

%description static -l pt_BR
Bibliotecas estáticas para o OAF.

%prep
%setup -q
%patch -p1

%build
sed -e s/AM_GNU_OAF_GETTEXT/AM_GNU_GETTEXT/ configure.in > configure.in.tmp
mv -f configure.in.tmp configure.in
rm -f missing aclocal.m4
xml-i18n-toolize --copy --force
%{__libtoolize}
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__automake}
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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
/usr/bin/scrollkeeper-update

%postun
/sbin/ldconfig
/usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO oaf-config.xml.sample
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
%{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/*.sh
%{_includedir}/liboaf
%{_aclocaldir}/oaf.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
