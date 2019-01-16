#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ell
Version  : 0.17
Release  : 6
URL      : https://mirrors.kernel.org/pub/linux/libs/ell/ell-0.17.tar.xz
Source0  : https://mirrors.kernel.org/pub/linux/libs/ell/ell-0.17.tar.xz
Summary  : Embedded Linux library
Group    : Development/Tools
License  : LGPL-2.1
Requires: ell-lib = %{version}-%{release}
Requires: ell-license = %{version}-%{release}
BuildRequires : pkgconfig(glib-2.0)

%description
ELL - Embedded Linux library
****************************
Compilation and installation
============================

%package dev
Summary: dev components for the ell package.
Group: Development
Requires: ell-lib = %{version}-%{release}
Provides: ell-devel = %{version}-%{release}

%description dev
dev components for the ell package.


%package lib
Summary: lib components for the ell package.
Group: Libraries
Requires: ell-license = %{version}-%{release}

%description lib
lib components for the ell package.


%package license
Summary: license components for the ell package.
Group: Default

%description license
license components for the ell package.


%prep
%setup -q -n ell-0.17

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1547652136
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1547652136
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ell
cp COPYING %{buildroot}/usr/share/package-licenses/ell/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/ell/base64.h
/usr/include/ell/cert.h
/usr/include/ell/checksum.h
/usr/include/ell/cipher.h
/usr/include/ell/dbus-client.h
/usr/include/ell/dbus-service.h
/usr/include/ell/dbus.h
/usr/include/ell/dhcp.h
/usr/include/ell/dir.h
/usr/include/ell/ecc.h
/usr/include/ell/ecdh.h
/usr/include/ell/ell.h
/usr/include/ell/file.h
/usr/include/ell/genl.h
/usr/include/ell/hashmap.h
/usr/include/ell/hwdb.h
/usr/include/ell/idle.h
/usr/include/ell/io.h
/usr/include/ell/key.h
/usr/include/ell/log.h
/usr/include/ell/main.h
/usr/include/ell/net.h
/usr/include/ell/netlink.h
/usr/include/ell/pem.h
/usr/include/ell/pkcs5.h
/usr/include/ell/plugin.h
/usr/include/ell/queue.h
/usr/include/ell/random.h
/usr/include/ell/ringbuf.h
/usr/include/ell/settings.h
/usr/include/ell/signal.h
/usr/include/ell/string.h
/usr/include/ell/strv.h
/usr/include/ell/test.h
/usr/include/ell/timeout.h
/usr/include/ell/tls.h
/usr/include/ell/uintset.h
/usr/include/ell/utf8.h
/usr/include/ell/util.h
/usr/include/ell/uuid.h
/usr/lib64/libell.so
/usr/lib64/pkgconfig/ell.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libell.so.0
/usr/lib64/libell.so.0.0.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ell/COPYING
