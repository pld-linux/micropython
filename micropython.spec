#
# Conditional build:
%bcond_without	tests		# build without tests

Summary:	Implementation of Python 3 with very low memory footprint
Name:		micropython
Version:	1.10
Release:	1
License:	MIT
Group:		Development/Languages/Python
Source0:	http://micropython.org/resources/source/%{name}-%{version}.tar.xz
# Source0-md5:	d16db23dd070064ed491f31e4fd3b540
URL:		http://micropython.org/
BuildRequires:	libffi-devel
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
%{__make} -C ports/unix \
	CC="%{__cc}" \
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
