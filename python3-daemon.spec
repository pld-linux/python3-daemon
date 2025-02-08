#
# Conditional build:
%bcond_with	tests	# do not perform "make test"
# Disabled tests as pidlockfile is not anymore in the lastest python-lockfile

%define 	module	daemon
Summary:	Library to implement a well-behaved Unix daemon process
Name:		python3-%{module}
Version:	3.1.2
Release:	1
License:	Python
Group:		Development/Languages
Source0:	https://pypi.debian.net/python-daemon/python_%{module}-%{version}.tar.gz
# Source0-md5:	d42ee28735506ea1cb51c348530d6d94
URL:		http://pypi.python.org/pypi/python-daemon/
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	sed >= 4.0
%if %{with tests}
BuildRequires:	python3-lockfile
#BuildRequires:	python3-minimock
%endif
Requires:	python3-lockfile
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library implements the well-behaved daemon specification of PEP
3143, "Standard daemon process library".

%prep
%setup -q -n python_daemon-%{version}

%build
%py3_build_pyproject \
	--skip-dependency-check

# Test suite requires minimock and lockfile
%if %{with tests}
PYTHONPATH=$(pwd) nosetests-%{py_ver}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.* README ChangeLog
%{py3_sitescriptdir}/daemon
%{py3_sitescriptdir}/python_daemon-%{version}.dist-info
