#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v18
# autospec commit: f35655a
#
Name     : ell
Version  : 0.69
Release  : 59
URL      : https://mirrors.kernel.org/pub/linux/libs/ell/ell-0.69.tar.gz
Source0  : https://mirrors.kernel.org/pub/linux/libs/ell/ell-0.69.tar.gz
Summary  : Embedded Linux library
Group    : Development/Tools
License  : LGPL-2.1
Requires: ell-lib = %{version}-%{release}
Requires: ell-license = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : file
BuildRequires : pkgconfig(glib-2.0)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
Requires: ell = %{version}-%{release}

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
%setup -q -n ell-0.69
cd %{_builddir}/ell-0.69
pushd ..
cp -a ell-0.69 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1725891709
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static
make  %{?_smp_mflags}
popd
%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1725891709
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ell
cp %{_builddir}/ell-%{version}/COPYING %{buildroot}/usr/share/package-licenses/ell/32c7c5556c56cdbb2d507e27d28d081595a35a9b || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/ell/acd.h
/usr/include/ell/base64.h
/usr/include/ell/cert.h
/usr/include/ell/checksum.h
/usr/include/ell/cipher.h
/usr/include/ell/cleanup.h
/usr/include/ell/dbus-client.h
/usr/include/ell/dbus-service.h
/usr/include/ell/dbus.h
/usr/include/ell/dhcp.h
/usr/include/ell/dhcp6.h
/usr/include/ell/dir.h
/usr/include/ell/ecc.h
/usr/include/ell/ecdh.h
/usr/include/ell/ell.h
/usr/include/ell/file.h
/usr/include/ell/genl.h
/usr/include/ell/gpio.h
/usr/include/ell/hashmap.h
/usr/include/ell/hwdb.h
/usr/include/ell/icmp6.h
/usr/include/ell/idle.h
/usr/include/ell/io.h
/usr/include/ell/key.h
/usr/include/ell/log.h
/usr/include/ell/main.h
/usr/include/ell/minheap.h
/usr/include/ell/net.h
/usr/include/ell/netconfig.h
/usr/include/ell/netlink.h
/usr/include/ell/notifylist.h
/usr/include/ell/path.h
/usr/include/ell/pem.h
/usr/include/ell/queue.h
/usr/include/ell/random.h
/usr/include/ell/ringbuf.h
/usr/include/ell/rtnl.h
/usr/include/ell/settings.h
/usr/include/ell/signal.h
/usr/include/ell/string.h
/usr/include/ell/strv.h
/usr/include/ell/sysctl.h
/usr/include/ell/test.h
/usr/include/ell/tester.h
/usr/include/ell/time.h
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
/V3/usr/lib64/libell.so.0.0.2
/usr/lib64/libell.so.0
/usr/lib64/libell.so.0.0.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ell/32c7c5556c56cdbb2d507e27d28d081595a35a9b
