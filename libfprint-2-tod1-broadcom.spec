Name:           libfprint-2-tod1-broadcom
Version:        0.0.3
Release:        3%{?dist}
Summary:        Broadcom driver module for libfprint-2 for various Dell laptops
License:        NonFree
Group:          Hardware/Mobile
%global branch jammy
URL:            https://git.launchpad.net/~oem-solutions-engineers/libfprint-2-tod1-broadcom/+git/libfprint-2-tod1-broadcom/
BuildRequires:  git
BuildRequires:  pkgconfig(udev)
ExclusiveArch:  x86_64
Supplements:    modalias(usb:v0A5Cp5840d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0A5Cp5842d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0A5Cp5843d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0A5Cp5844d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0A5Cp5845d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0A5Cp5864d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0A5Cp5865d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0A5Cp5866d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0A5Cp5867d*dc*dsc*dp*ic*isc*ip*)

%description
This is user space driver for Broadcom fingerprint module. Proprietary driver for the fingerprint reader on the various Dell laptops - direct from Dell's Ubuntu repo.

%prep
git clone -b %{branch} %{url}
cd libfprint-2-tod1-broadcom

%build

%install
cd libfprint-2-tod1-broadcom
install -dm 0755 %{buildroot}%{_udevrulesdir} %{buildroot}%{_libdir}/libfprint-2/tod-1 %{buildroot}%{_sharedstatedir}/fprint/fw/ %{buildroot}%{_sharedstatedir}/fprint/.broadcomCv3plusFW/
install -m 0644 lib/udev/rules.d/60-libfprint-2-device-broadcom.rules %{buildroot}%{_udevrulesdir}/60-libfprint-2-device-broadcom.rules
install -m 0644 lib/udev/rules.d/60-libfprint-2-device-broadcom.rules %{buildroot}%{_udevrulesdir}/60-libfprint-2-device-broadcom-cv3plus.rules
install -m 0644 var/lib/fprint/fw/cv3/* %{buildroot}%{_sharedstatedir}/fprint/fw/
install -m 0644 var/lib/fprint/fw/cv3plus/* %{buildroot}%{_sharedstatedir}/fprint/.broadcomCv3plusFW/
install -m 0755 usr/lib/x86_64-linux-gnu/libfprint-2/tod-1/libfprint-2-tod-1-broadcom.so %{buildroot}%{_libdir}/libfprint-2/tod-1/libfprint-2-tod-1-broadcom.so
install -m 0755 usr/lib/x86_64-linux-gnu/libfprint-2/tod-1/libfprint-2-tod-1-broadcom.so %{buildroot}%{_libdir}/libfprint-2/tod-1/libfprint-2-tod-1-broadcom-cv3plus.so

%files
%attr(644, -, -) %license libfprint-2-tod1-broadcom/LICENCE.broadcom
%{_udevrulesdir}/60-libfprint-2-device-broadcom.rules
%{_udevrulesdir}/60-libfprint-2-device-broadcom-cv3plus.rules
%{_libdir}/libfprint-2/tod-1/libfprint-2-tod-1-broadcom.so
%{_libdir}/libfprint-2/tod-1/libfprint-2-tod-1-broadcom-cv3plus.so
%{_sharedstatedir}/fprint/fw/*
%{_sharedstatedir}/fprint/.broadcomCv3plusFW/*

%changelog
* Sat Jul 13 2024 Stevie Galluscio <galluscio.stevie@gmail.com> - 0.0.3
- Add more support for CV3plus

* Wed Jul 10 2024 Stevie Galluscio <galluscio.stevie@gmail.com> - 0.0.2
- Update git branch to jammy for new fw and openssl 3 compatibility from CV3 updates

* Sun Nov 19 2023 Chris Harvey <chris@chrisnharvey.com> - 0.0.1
- First release
