Name:			python-serial
Version:		2.4
Release:		%mkrel 1

Summary:	Python serial port extension
License:	Python
Group:          Development/Python
URL:		http://pyserial.sourceforge.net
Source0:	http://downloads.sourceforge.net/pyserial/pyserial-%{version}.tar.gz

BuildArch:	noarch
# at least python 2.2 needed, current is 2.5
%define minversion 2.2
BuildRequires:	libpython-devel >= %minversion
BuildRoot:	%{_tmppath}/%{name}-%{version}

Requires:	python
Obsoletes:	pyserial < %{version}-%{release}
Provides:	pyserial = %{version}-%{release}

%description
This module encapsulates the access for the serial port.
It provides backends for Python running on Windows, Linux, BSD (possibly any 
POSIX compilant system) and Jython. The module named "serial" automatically 
selects the appropriate backend.

%prep
%setup -q -n pyserial-%{version}

%build
#perl -pi -e 's/\r\n/\n/;' * examples/* serial/*
chmod 755 examples/*.py
perl -pi -e "s/#! python/#!\/usr\/bin\/env python/" serial/serialutil.py\
 serial/serialcli.py
perl -pi -e "s/#!jython/#!\/usr\/bin\/env jython/" serial/serialjava.py
#python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root %{buildroot} --record=INSTALLED_FILES


%clean
rm -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc CHANGES.txt LICENSE.txt PKG-INFO README.txt examples
