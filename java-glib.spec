%define		pname	glib-java
Summary:	Java interface for Glib library
Summary(pl):	Wrapper Javy dla biblioteki Glib
Name:		java-glib
Version:	0.4.1
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/glib-java/0.4/%{pname}-%{version}.tar.bz2
# Source0-md5:	52b8f86f4689daab0aac4de94191ff1c
URL:		http://java-gnome.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc-java >= 5:3.3.2
BuildRequires:	glib2-devel >= 1:2.12.6
BuildRequires:	libtool
BuildRequires:	zip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Java interface for the Glib library.

%description -l pl
Wrapper Javy dla biblioteki Glib.

%package devel
Summary:	Header files for java-glib library
Summary(pl):	Pliki nag³ówkowe biblioteki java-glib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.12.6

%description devel
Header files for java-glib library.

%description devel -l pl
Pliki nag³ówkowe biblioteki java-glib.

%prep
%setup -q -n %{pname}-%{version}

%build
%{__libtoolize}
%{__aclocal} -I macros
%{__automake}
%{__autoconf}
%configure \
	GCJFLAGS="%{rpmcflags}" \
	--without-javadocs
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_docdir}/%{pname}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/libglib*-0.4.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libglibjava.so
%attr(755,root,root) %{_libdir}/libglibjni.so
%{_libdir}/*.la
%{_datadir}/%{pname}
%{_includedir}/%{pname}
%{_javadir}/*.jar
%{_pkgconfigdir}/*.pc
