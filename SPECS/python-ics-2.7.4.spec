##########################
#  User-modifiable configs
##########################

#  Is the resulting package and the installed binary named "python" or
#  "python2"?
#WARNING: Commenting out doesn't work.  Last line is what's used.
%define config_binsuffix none
%define config_binsuffix 2.7

#  Build tkinter?  "auto" enables it if /usr/bin/wish exists.
#WARNING: Commenting out doesn't work.  Last line is what's used.
%define config_tkinter yes
%define config_tkinter yes

#  Use pymalloc?  The last line (commented or not) determines wether
#  pymalloc is used.
#WARNING: Commenting out doesn't work.  Last line is what's used.
%define config_pymalloc no
%define config_pymalloc no

#  Enable IPV6?
#WARNING: Commenting out doesn't work.  Last line is what's used.
%define config_ipv6 yes
%define config_ipv6 no

#  Build shared libraries or .a library?
#WARNING: Commenting out doesn't work.  Last line is what's used.
%define config_sharedlib no
%define config_sharedlib yes

#  Location of the HTML directory.
%define config_htmldir /var/www/html/python

#################################
#  End of user-modifiable configs
#################################

%define name python-ics
#--start constants--
%define version 2.7.4
%define libvers 2.7
#--end constants--
%define release 3
#%define __prefix /usr/local

#  kludge to get around rpm <percent>define weirdness
%define ipv6 %(if [ "%{config_ipv6}" = yes ]; then echo --enable-ipv6; else echo --disable-ipv6; fi)
%define pymalloc %(if [ "%{config_pymalloc}" = yes ]; then echo --with-pymalloc; else echo --without-pymalloc; fi)
%define binsuffix %(if [ "%{config_binsuffix}" = none ]; then echo ; else echo "%{config_binsuffix}"; fi)
%define include_tkinter %(if [ \\( "%{config_tkinter}" = auto -a -f /usr/bin/wish \\) -o "%{config_tkinter}" = yes ]; then echo 1; else echo 0; fi)
#%define libdirname %(( uname -m | egrep -q '_64$' && [ -d /usr/lib64 ] && echo lib64 ) || echo lib)
%define libdirname lib
%define sharedlib %(if [ "%{config_sharedlib}" = yes ]; then echo --enable-shared; else echo ; fi)
%define include_sharedlib %(if [ "%{config_sharedlib}" = yes ]; then echo 1; else echo 0; fi)

#  detect if documentation is available
%define include_docs %(if [ -f "%{_sourcedir}/html-%{version}.tar.bz2" ]; then echo 1; else echo 0; fi)

Summary: An interpreted, interactive, object-oriented programming language.
Name: %{name}
Version: %{version}
Release: %{release}
License: PSF
Group: Development/Languages
Source: Python-%{version}.tar.bz2
%if %{include_docs}
Source1: html-%{version}.tar.bz2
%endif
Source2: python-gdb.py
Source3: python-ics.conf
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: expat-devel
BuildRequires: db4-devel
BuildRequires: gdbm-devel
BuildRequires: sqlite-devel
BuildRequires: tk-devel tcl-devel
BuildRequires: readline-devel zlib-devel bzip2-devel openssl-devel
Autoreq: no
Prefix: %{__prefix}
Packager: Sean Reifschneider <jafo-rpms@tummy.com>

%description
Python is an interpreted, interactive, object-oriented programming
language.  It incorporates modules, exceptions, dynamic typing, very high
level dynamic data types, and classes. Python combines remarkable power
with very clear syntax. It has interfaces to many system calls and
libraries, as well as to various window systems, and is extensible in C or
C++. It is also usable as an extension language for applications that need
a programmable interface.  Finally, Python is portable: it runs on many
brands of UNIX, on PCs under Windows, MS-DOS, and OS/2, and on the
Mac.

# %package devel
# Summary: The libraries and header files needed for Python extension development.
# Requires: python-ics
# Group: Development/Libraries

# %description devel
# The Python programming language's interpreter can be extended with
# dynamically loaded extensions and can be embedded in other programs.
# This package contains the header files and libraries needed to do
# these types of tasks.

# Install python-devel if you want to develop Python extensions.  The
# python package will also need to be installed.  You'll probably also
# want to install the python-docs package, which contains Python
# documentation.

%if %{include_tkinter}
%package tkinter
Summary: A graphical user interface for the Python scripting language.
Group: Development/Languages
Requires(req): python%{binsuffix} = %{version}-%{release}

%description tkinter
The Tkinter (Tk interface) program is an graphical user interface for
the Python scripting language.

You should install the tkinter package if you'd like to use a graphical
user interface for Python programming.
%endif

%package tools
Summary: A collection of development tools included with Python.
Group: Development/Tools
Requires(req): python >= %{version}

%description tools
The Python package includes several development tools that are used
to build python programs.  This package contains a selection of those
tools, including the IDLE Python IDE.

Install python-tools if you want to use these tools to develop
Python programs.  You will also need to install the python and
tkinter packages.

%if %{include_docs}
%package docs
Summary: Python-related documentation.
Group: Development/Documentation

%description docs
Documentation relating to the Python programming language in HTML and info
formats.
%endif

%changelog
* Mon Dec 20 2004 Sean Reifschneider <jafo-rpms@tummy.com> [2.4-2pydotorg]
- Changing the idle wrapper so that it passes arguments to idle.

* Tue Oct 19 2004 Sean Reifschneider <jafo-rpms@tummy.com> [2.4b1-1pydotorg]
- Updating to 2.4.

* Thu Jul 22 2004 Sean Reifschneider <jafo-rpms@tummy.com> [2.3.4-3pydotorg]
- Paul Tiemann fixes for %{prefix}.
- Adding permission changes for directory as suggested by reimeika.ca
- Adding code to detect when it should be using lib64.
- Adding a define for the location of /var/www/html for docs.

* Thu May 27 2004 Sean Reifschneider <jafo-rpms@tummy.com> [2.3.4-2pydotorg]
- Including changes from Ian Holsman to build under Red Hat 7.3.
- Fixing some problems with the /usr/local path change.

* Sat Mar 27 2004 Sean Reifschneider <jafo-rpms@tummy.com> [2.3.2-3pydotorg]
- Being more agressive about finding the paths to fix for
  #!/usr/local/bin/python.

* Sat Feb 07 2004 Sean Reifschneider <jafo-rpms@tummy.com> [2.3.3-2pydotorg]
- Adding code to remove "#!/usr/local/bin/python" from particular files and
  causing the RPM build to terminate if there are any unexpected files
  which have that line in them.

* Mon Oct 13 2003 Sean Reifschneider <jafo-rpms@tummy.com> [2.3.2-1pydotorg]
- Adding code to detect wether documentation is available to build.

* Fri Sep 19 2003 Sean Reifschneider <jafo-rpms@tummy.com> [2.3.1-1pydotorg]
- Updating to the 2.3.1 release.

* Mon Feb 24 2003 Sean Reifschneider <jafo-rpms@tummy.com> [2.3b1-1pydotorg]
- Updating to 2.3b1 release.

* Mon Feb 17 2003 Sean Reifschneider <jafo-rpms@tummy.com> [2.3a1-1]
- Updating to 2.3 release.

* Sun Dec 23 2001 Sean Reifschneider <jafo-rpms@tummy.com>
[Release 2.2-2]
- Added -docs package.
- Added "auto" config_tkinter setting which only enables tk if
  /usr/bin/wish exists.

* Sat Dec 22 2001 Sean Reifschneider <jafo-rpms@tummy.com>
[Release 2.2-1]
- Updated to 2.2.
- Changed the extension to "2" from "2.2".

* Tue Nov 18 2001 Sean Reifschneider <jafo-rpms@tummy.com>
[Release 2.2c1-1]
- Updated to 2.2c1.

* Thu Nov  1 2001 Sean Reifschneider <jafo-rpms@tummy.com>
[Release 2.2b1-3]
- Changed the way the sed for fixing the #! in pydoc works.

* Wed Oct  24 2001 Sean Reifschneider <jafo-rpms@tummy.com>
[Release 2.2b1-2]
- Fixed missing "email" package, thanks to anonymous report on sourceforge.
- Fixed missing "compiler" package.

* Mon Oct 22 2001 Sean Reifschneider <jafo-rpms@tummy.com>
[Release 2.2b1-1]
- Updated to 2.2b1.

* Mon Oct  9 2001 Sean Reifschneider <jafo-rpms@tummy.com>
[Release 2.2a4-4]
- otto@balinor.mat.unimi.it mentioned that the license file is missing.

* Sun Sep 30 2001 Sean Reifschneider <jafo-rpms@tummy.com>
[Release 2.2a4-3]
- Ignacio Vazquez-Abrams pointed out that I had a spruious double-quote in
  the spec files.  Thanks.

* Wed Jul 25 2001 Sean Reifschneider <jafo-rpms@tummy.com>
[Release 2.2a1-1]
- Updated to 2.2a1 release.
- Changed idle and pydoc to use binsuffix macro

#######
#  PREP
#######
%prep
%setup -n Python-%{version}

########
#  BUILD
########
%build
echo "Setting for ipv6: %{ipv6}"
echo "Setting for pymalloc: %{pymalloc}"
echo "Setting for binsuffix: %{binsuffix}"
echo "Setting for include_tkinter: %{include_tkinter}"
echo "Setting for libdirname: %{libdirname}"
echo "Setting for sharedlib: %{sharedlib}"
echo "Setting for include_sharedlib: %{include_sharedlib}"
#./configure --enable-unicode=ucs4 %{sharedlib} %{ipv6} %{pymalloc} --prefix=%{__prefix}
./configure %{sharedlib} --with-pydebug --prefix=%{__prefix}
make

##########
#  INSTALL
##########
%install
#  set the install path
[ -d "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%global pybasever 2.7
%global py_SOVERSION 1.0
%global py_INSTSONAME libpython%{pybasever}.so.%{py_SOVERSION}
%global dir_holding_gdb_py /usr/lib/debug/%{__prefix}/%{libdirname}
%global path_of_gdb_py %{dir_holding_gdb_py}/%{py_INSTSONAME}.debug-gdb.py
mkdir -p %{buildroot}%{dir_holding_gdb_py}
cp %{SOURCE2} %{buildroot}%{path_of_gdb_py}
mkdir -p %{buildroot}/etc/ld.so.conf.d
cp %{SOURCE3} %{buildroot}/etc/ld.so.conf.d

# Manually byte-compile the file, in case find-debuginfo.sh is run before
# brp-python-bytecompile, so that the .pyc/.pyo files are properly listed in
# the debuginfo manifest:
LD_LIBRARY_PATH=. ./python -c "import compileall; import sys; compileall.compile_dir('%{buildroot}%{dir_holding_gdb_py}', ddir='%{dir_holding_gdb_py}')"

LD_LIBRARY_PATH=. ./python -O -c "import compileall; import sys; compileall.compile_dir('%{buildroot}%{dir_holding_gdb_py}', ddir='%{dir_holding_gdb_py}')"

########
#   POST
########
%post
/sbin/ldconfig


########
#  CLEAN
########
%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

########
#  FILES
########
%files
%defattr(-,root,root)
%doc Misc/README Misc/cheatsheet Misc/Porting
%doc LICENSE Misc/ACKS Misc/HISTORY Misc/NEWS
%{__prefix}/share/man/man1/*

%{__prefix}/bin/*

%{__prefix}/include/python%{libvers}/*
%{__prefix}/%{libdirname}/pkgconfig/*
%{__prefix}/%{libdirname}/python%{libvers}/*
/usr/lib/debug%{__prefix}/%{libdirname}/libpython*.py*
/etc/ld.so.conf.d/python-ics.conf

%attr(755,root,root) %dir %{__prefix}/include/python%{libvers}
%attr(755,root,root) %dir %{__prefix}/%{libdirname}/python%{libvers}/
%if %{include_sharedlib}
%{__prefix}/%{libdirname}/libpython*
%endif

# %files devel
# %defattr(-,root,root)
%{__prefix}/include/python%{libvers}/*.h

%if %{include_docs}
%files docs
%defattr(-,root,root)
%{config_htmldir}/*
%endif
