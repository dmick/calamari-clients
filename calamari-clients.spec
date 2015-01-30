#
# Calamari clients Spec File
#

%define version 1.2.1.1
%define revision 57-g18ed41e
%define rpm_revision 57_g18ed41e

#################################################################################
# common
#################################################################################
Name:		calamari-clients
Version: 	%{version}
Release: 	1local%{?dist}
Summary:	Calamari GUI front-end components
Requires: 	calamari-server
License: 	MIT
Group:   	System/Filesystems
URL:     	http://ceph.com/
Source0: 	%{name}_%{version}.tar.xz
#Patch0:		0001-Use-locally-installed-bower-and-grunt.patch
BuildRequires:	nodejs
BuildRequires:	git
BuildRequires:	rubygems
BuildRequires:	ruby-devel
#BuildRequires:	libpng-devel

%description
Contains the JavaScript GUI content for the Calamari frontend components
 (dashboard, login screens, administration screens)

%prep
%setup -q -n %{name}-%{version}
#%patch0 -p1
# Install compass locally
cd vendor/cache
gem install compass
cd ../../

%install
make DESTDIR="$RPM_BUILD_ROOT" REAL_BUILD=y VERSION="%{version}" REVISION="%{revision}" RPM_REVISION="%{rpm_revision}" install

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"

%files -n calamari-clients
/opt/calamari/webapp/content

%changelog
