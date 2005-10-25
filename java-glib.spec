%define		pname	glib-java
Summary:	Java interface for Glib library
Summary(pl):	Wrapper Javy dla biblioteki Glib
Name:		java-glib
Version:	0.2.0
Release:	2
License:	GPL v2
Group:		Libraries
Source0:	http://research.operationaldynamics.com/linux/java-gnome/dist/%{pname}-%{version}.tar.gz
# Source0-md5:	252abc8cdb4980d5b0c79fe05050de2c
URL:		http://java-gnome.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc-java >= 5:3.3.2
BuildRequires:	glib2-devel >= 1:2.8.0
BuildRequires:	libtool
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
Requires:	glib2-devel >= 1:2.8.0

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
	GCJ_JAR=`echo %{_datadir}/java/libgcj*.jar` \
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
%attr(755,root,root) %{_libdir}/libglib*-0.2.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libglibjava.so
%attr(755,root,root) %{_libdir}/libglibjni.so
%{_libdir}/*.la
%{_datadir}/%{pname}
%dir %{_includedir}/%{pname}
%{_includedir}/%{pname}/*.h
%{_javadir}/*.jar
%{_pkgconfigdir}/*.pc
