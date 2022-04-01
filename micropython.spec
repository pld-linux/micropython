#
# Conditional build:
%bcond_without	tests		# build without tests

Summary:	Implementation of Python 3 with very low memory footprint
Name:		micropython
Version:	1.18
Release:	1
License:	MIT
Group:		Development/Languages/Python
Source0:	http://micropython.org/resources/source/%{name}-%{version}.tar.xz
# Source0-md5:	134dcca4c286b8be9d2cc738809b7246
URL:		http://micropython.org/
BuildRequires:	libffi-devel
BuildRequires:	mbedtls-devel
BuildRequires:	pkgconfig
BuildRequires:	python
BuildRequires:	python-modules
%if %{with tests}
BuildRequires:	python3
BuildRequires:	python3-modules
%endif
BuildRequires:	readline-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Implementation of Python 3 with very low memory footprint.

%prep
%setup -q

%build

# add -I/where/jni.h (do we have a method to get this dir?) is and MICROPY_PY_JNI=1 to make below

%{__make} -C ports/unix \
	CC="%{__cc}" \
	CFLAGS_EXTRA="%{rpmcppflags} %{rpmcflags} -Wno-error=maybe-uninitialized" \
	LDFLAGS_EXTRA="%{rpmldflags}" \
	MICROPY_SSL_MBEDTLS=1 \
	STRIP=true \
	V=1

%{?with_tests:%{__make} -C ports/unix test}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
cp -a ports/unix/micropython $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/micropython
