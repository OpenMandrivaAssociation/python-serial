Name:			python-serial
Version:		3.5
Release:		1

Summary:	Python serial port extension
License:	Python license
Group:          Development/Python
URL:		https://pyserial.sourceforge.net
Source0:	https://github.com/pyserial/pyserial/releases/download/v%{version}/pyserial-%{version}.tar.gz

BuildArch:	noarch
BuildSystem:	python
BuildRequires:	dos2unix

Obsoletes:	python2-serial < %{EVRD}
Obsoletes:	pyserial < %{version}-%{release}
Provides:	pyserial = %{version}-%{release}

%description
This module encapsulates the access for the serial port.
It provides backends for Python running on Windows, Linux, BSD (possibly any 
POSIX compilant system) and Jython. The module named "serial" automatically 
selects the appropriate backend.

%files
%doc CHANGES.rst LICENSE.txt PKG-INFO README.rst examples
%{_bindir}/pyserial-miniterm
%{_bindir}/pyserial-ports
%{py_puresitedir}/serial
%{py_puresitedir}/pyserial-%{version}-py%{py_ver}.egg-info
