%define		pname	glib-java
Summary:	Java interface for Glib library
Summary(pl.UTF-8):	Wrapper Javy dla biblioteki Glib
Name:		java-glib
Version:	0.4.2
Release:	5
License:	GPL v2
Group:		Libraries/Java
Source0:	http://ftp.gnome.org/pub/GNOME/sources/glib-java/0.4/%{pname}-%{version}.tar.bz2
# Source0-md5:	8820119f7d44f8890cd56007c264a16a
URL:		http://java-gnome.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc-java >= 5:3.3.2
BuildRequires:	glib2-devel >= 1:2.12.7
BuildRequires:	jar
BuildRequires:	libtool
BuildRequires:	zip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Java interface for the Glib library.

%description -l pl.UTF-8
Wrapper Javy dla biblioteki Glib.

%package devel
Summary:	Header files for java-glib library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki java-glib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.12.7

%description devel
Header files for java-glib library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki java-glib.

%prep
%setup -q -n %{pname}-%{version}

%build
%{__libtoolize}
%{__aclocal} -I macros
%{__automake}
%{__autoconf}
%configure \
	GCJFLAGS="%{rpmcflags} -fPIC" \
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
