rhel6-python2.7-specs
=====================

Spec files for python2.7 for RHEL 6.


Preparing
---------------------------
    Download 'Python-2.7.4.tar.bz2' to /root/rpmbuild/SOURCES
    Copy 'python-gdb.py', 'python-ics.conf' to /root/rpmbuild/SOURCES

Building RPMs for python2.7
---------------------------
    QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -ba /root/rpmbuild/SPECS/python-ics-2.7.4.spec 
