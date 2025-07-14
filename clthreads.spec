Summary:	Kokkini Zita clthreads library
Summary(pl.UTF-8):	Biblioteka Kokkini Zita clthreads
Name:		clthreads
Version:	2.4.2
Release:	1
# as specified in source files (included COPYING is LGPL v2.1)
License:	GPL v2+
Group:		Libraries
Source0:	http://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	6c82e4edece2db2de9451b6afe702a86
Patch0:		makefile.patch
URL:		http://kokkinizita.linuxaudio.org/linuxaudio/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
clthreads library, used by Kokkini Zita Linux Audio projects.

%description -l pl.UTF-8
Biblioteka clthreads, używana przez projekty Kokkini Zita Linux Audio.

%package devel
Summary:	Header files for %{name} library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for %{name} library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki %{name}.

%prep
%setup -q
%patch -P0 -p1

%build
CXX="%{__cxx}" \
CPPFLAGS="%{rpmcxxflags} %{rpmcppflags}" \
LDFLAGS="%{rpmldflags}" \
%{__make} -C source

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}

%{__make} -C source install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	LIBDIR=%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_libdir}/libclthreads.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclthreads.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclthreads.so
%{_includedir}/clthreads.h
