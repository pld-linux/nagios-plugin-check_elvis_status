%define		plugin	check_elvis_status
%define		php_min_version 5.2.0
Summary:	Nagios plugin to check Elvis DAM status
Name:		nagios-plugin-%{plugin}
Version:	0.3
Release:	1
License:	GPL v2
Group:		Networking
Source0:	https://github.com/glensc/nagios-plugin-check_elvis_status/archive/v%{version}/%{plugin}-%{version}.tar.gz
# Source0-md5:	14d04b1629a4082aa7cd94eccc897bbb
URL:		https://github.com/glensc/nagios-plugin-check_elvis_status
Requires:	nagios-common
Requires:	nagios-plugins-libs
Requires:	php(core) >= %{php_min_version}
Requires:	php(json)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/nagios/plugins
%define		plugindir	%{_prefix}/lib/nagios/plugins

%description
Nagios plugin to check Elvis DAM status via admin /server-status json
data.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{plugindir}}
install -p %{plugin}.php $RPM_BUILD_ROOT%{plugindir}/%{plugin}
cp -p %{plugin}.cfg $RPM_BUILD_ROOT%{_sysconfdir}/%{plugin}.cfg

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{plugin}.cfg
%attr(755,root,root) %{plugindir}/%{plugin}
