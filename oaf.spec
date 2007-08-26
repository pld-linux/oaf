Summary:	OAF - Objects activated by factories library
Summary(ko.UTF-8):	그놈용 객체 활성 구조
Summary(pl.UTF-8):	Biblioteka OAF
Summary(pt_BR.UTF-8):	Sistema de ativação de objetos para o GNOME
Summary(ru.UTF-8):	OAF - система активации объектов GNOME
Summary(uk.UTF-8):	OAF - система активації об'єктів GNOME
Name:		oaf
Version:	0.6.10
Release:	9
License:	LGPL v2+ (library), GPL v2+ (programs)
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/oaf/0.6/%{name}-%{version}.tar.bz2
# Source0-md5:	ed9aa2ceb70bba34034b3134b22d2729
Patch0:		%{name}-default-search-path.patch
Patch1:		%{name}-am18.patch
Patch2:		%{name}-locale-names.patch
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
BuildRequires:	sed >= 4.0
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	scrollkeeper
Obsoletes:	liboaf0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _sysconfdir     /etc/X11/GNOME

%description
Objects activated by factories library for GNOME. It uses ORBit.

%description -l pl.UTF-8
Obiekty aktywowane przez agentów dla GNOME. Używa ORBit-a.

%description -l pt_BR.UTF-8
Sistema de ativação de objetos para o GNOME. Usa o ORBit.

%description -l ru.UTF-8
OAF (Object Activation Framework) предоставляет механизм активации для
компонентов GNOME. Это замена GOAD для платформы GNOME 2.

%description -l uk.UTF-8
OAF (Object Activation Framework) надає механізм активації для
компонентів GNOME. Це заміна GOAD для платформи GNOME 2.

%package devel
Summary:	Header files etc to develop oaf applications
Summary(ko.UTF-8):	OAF를 위한 라이브러리와 헤더 파일
Summary(pl.UTF-8):	Pliki nagłówkowe i inne do oaf
Summary(pt_BR.UTF-8):	Bibliotecas e arquivos de inclusão para o OAF
Summary(ru.UTF-8):	Файлы для разработки программ с использованием OAF
Summary(uk.UTF-8):	Файли для розробки програм з використанням OAF
License:	LGPL v2+
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	ORBit-devel >= 0.5.1
Requires:	glib-devel >= 1.2.0
Requires:	popt-devel >= 1.5
Obsoletes:	liboaf0-devel

%description devel
Header files etc you can use to develop oaf applications.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe i inne do oaf niezbędne przy
tworzeniu aplikacji opartych o tą bibliotekę.

%description devel -l pt_BR.UTF-8
Bibliotecas e arquivos de inclusão para o OAF.

%description devel -l ru.UTF-8
Этот пакет содержит файлы, необходимые для разработки программ,
использующих OAF.

%description devel -l uk.UTF-8
Цей пакет містить файли, необхідні для розробки програм, які
використовують OAF.

%package static
Summary:	Static oaf libraries
Summary(es.UTF-8):	Libraries estáticas for OAF
Summary(pl.UTF-8):	Biblioteka statyczna oaf
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para o OAF
License:	LGPL v2+
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static oaf libraries.

%description static -l es.UTF-8
Libraries estáticas for OAF.

%description static -l pl.UTF-8
Biblioteka statyczna oaf.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para o OAF.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

mv -f po/{no,nb}.po

%build
sed -i s/AM_GNU_OAF_GETTEXT/AM_GNU_GETTEXT/ configure.in
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
%attr(755,root,root) %{_bindir}/oaf-[!c]*
%attr(755,root,root) %{_bindir}/oaf-client
%attr(755,root,root) %{_bindir}/oafd
%attr(755,root,root) %{_libdir}/lib*.so.*.*
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
