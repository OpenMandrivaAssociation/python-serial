%define oname		serial
%define pname		py%{oname}
%define version		2.2
%define pyversion	2.5
#at least python 2.2 needed, but current is 2.5
%define release		%mkrel 3

Summary:	Python serial port extension
Name:		python-%{oname}
Version:	%{version}
Release:	%{release}
Source0:	%{pname}-%{version}.tar.bz2
License:	GPL
Group:		Development/Python
URL:		http://pyserial.sourceforge.net
BuildRoot:	%{_tmppath}/%{pname}-buildroot
BuildRequires:	libpython-devel >= %pyversion
BuildArch:      noarch
Requires:	python
Obsoletes:	pyserial
Provides:	pyserial

%description
This module encapsulates the access for the serial port.
It provides backends for Python running on Windows, Linux, BSD (possibly any 
POSIX compilant system) and Jython. The module named "serial" automatically 
selects the appropriate backend.

%prep
%setup -q -n %{pname}-%{version}

%build
perl -pi -e 's/\r\n/\n/;' * examples/* serial/*
chmod 755 examples/*.py
perl -pi -e "s/#! python/#!\/usr\/bin\/env python/" serial/serialutil.py
perl -pi -e "s/#!jython/#!\/usr\/bin\/env jython/" serial/serialjava.py
#python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root %{buildroot}


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES.txt LICENSE.txt PKG-INFO README.txt examples
%attr(0755,root,root) %py_puresitedir/%oname
%py_puresitedir/py%oname-%version-py%pyversion.egg-info
%ifarch x86_64
%attr(0755,root,root) %py_platsitedir/%oname
%endif



