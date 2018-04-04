#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		module	smmap
Summary:	A pure git implementation of a sliding window memory map manager
# Name must match the python module/package name (as in 'import' statement)
Name:		python-%{module}
Version:	2.0.3
Release:	1
License:	BSD
Group:		Development/Languages/Python
Source0:	https://github.com/gitpython-developers/smmap/archive/v%{version}/%{module}-%{version}.tar.gz
# Source0-md5:	87427acfb9d65867544d34a12434e502
URL:		https://github.com/Byron/smmap
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A pure git implementation of a sliding window memory map manager.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%{?with_tests:%{__python} setup.py test}

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/smmap/test

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/smmap
%{py_sitescriptdir}/smmap/*.py[co]
%{py_sitescriptdir}/smmap2-*.egg-info
