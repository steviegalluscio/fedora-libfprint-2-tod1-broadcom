Name:           libfprint-2-tod1-broadcom-cv3plus
Version:        0.0.1
Release:        1%{?dist}
Summary:        Broadcom driver module (CV3+) for libfprint-2 for various Dell laptops
License:        NonFree
Group:          Hardware/Mobile
%global branch jammy
URL:            https://git.launchpad.net/~oem-solutions-engineers/libfprint-2-tod1-broadcom/+git/libfprint-2-tod1-broadcom/
BuildRequires:  git
BuildRequires:  pkgconfig(udev)
ExclusiveArch:  x86_64
Supplements:    modalias(usb:v0A5Cp5864d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0A5Cp5865d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0A5Cp5866d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0A5Cp5867d*dc*dsc*dp*ic*isc*ip*)

%description
Firmwares and shared libraries for Broadcom fingerprint TOD driver (CV3+) used on various Dell laptops.

%prep
git clone -b %{branch} %{url}
cd libfprint-2-tod1-broadcom

%build

%install
cd libfprint-2-tod1-broadcom
install -dm 0755 %{buildroot}%{_udevrulesdir} %{buildroot}%{_libdir}/libfprint-2/tod-1 %{buildroot}%{_sharedstatedir}/fprint/fw/
install -m 0644 lib/udev/rules.d/60-libfprint-2-device-broadcom-cv3plus.rules %{buildroot}%{_udevrulesdir}/60-libfprint-2-device-broadcom-cv3plus.rules
install -m 0644 var/lib/fprint/fw/cv3plus/* %{buildroot}%{_sharedstatedir}/fprint/fw/
install -m 0755 usr/lib/x86_64-linux-gnu/libfprint-2/tod-1/libfprint-2-tod-1-broadcom-cv3plus.so %{buildroot}%{_libdir}/libfprint-2/tod-1/libfprint-2-tod-1-broadcom-cv3plus.so

%files
%attr(644, -, -) %license libfprint-2-tod1-broadcom/LICENCE.broadcom
%{_udevrulesdir}/60-libfprint-2-device-broadcom-cv3plus.rules
%{_libdir}/libfprint-2/tod-1/libfprint-2-tod-1-broadcom-cv3plus.so
%{_sharedstatedir}/fprint/fw/*

%changelog
* Sat Jul 13 2024 Stevie Galluscio <galluscio.stevie@gmail.com> - 0.0.1
- Separated from CV3
