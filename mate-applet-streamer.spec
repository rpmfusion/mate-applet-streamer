Name:           mate-applet-streamer
Version:        0.4.0
Release:        8%{?dist}
Summary:        MATE online radio streamer applet
License:        GPLv2+
URL:            http://www.zavedil.com/online-radio-applet
Source:         http://www.zavedil.com/wp-content/uploads/2017/07/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  libnotify-devel
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  gstreamer1-plugins-base-tools
BuildRequires:  gtk3-devel
BuildRequires:  sqlite-devel
BuildRequires:  mate-panel-devel

# for GStreamer with nonfree codecs
Requires:       gstreamer1-plugins-bad-freeworld
Requires:       gstreamer1-plugins-ugly

%description
This is a MATE panel applet to let you play your favorite online radio station
from your system tray or panel with a single click.
Icecast directory listing in included.

%prep
%autosetup

%build
%configure \
    --libdir=%{_prefix}/lib \
    --enable-gtk=3 \
    --enable-notify \
    --enable-gstreamer=1.0

%{make_build} V=1

%install
%{make_install}

# Do not install doc files: they are handled as rpm doc files.
rm -rf %{buildroot}%{_docdir}
rm -rf %{buildroot}%{_datadir}/glib-2.0/schemas/gschemas.compiled

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS BUGS ChangeLog README TODO
%license COPYING
%{_libexecdir}/streamer_applet
%{_prefix}/lib/bonobo/servers/StreamerAppletFactory.server
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.StreamerApplet.gschema.xml
%{_datadir}/mate-panel/applets/org.mate.applets.StreamerApplet.mate-panel-applet
%{_datadir}/dbus-1/services/org.mate.panel.applet.StreamerApplet.service
%{_datadir}/streamer_applet/
%{_datadir}/pixmaps/applet_streamer*.png
%{_datadir}/icons/hicolor/*/apps/applet_streamer.png


%changelog
* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 03 2019 Leigh Scott <leigh123linux@gmail.com> - 0.4.0-6
- Rebuild for new gstreamer1 version
- Remove Group tag
- Remove scriptlets

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 22 2017 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.4.0-1
- test 0.4.0 release

* Sun Mar 19 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.3.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Dec 18 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.3.10-2
- build for gtk3

* Sat Jan 16 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.3.10-1
- update to 0.3.10 release

* Tue Dec 22 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.3.2-1
- update to 0.3.2 release
- add gesettings schema file

* Sun Aug 31 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.2.3.1
- update to 0.2.3 release
- missing text in buttons for gtk3 build is fixed

* Sun Aug 23 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.2.2-1
- update to 0.2.2 release
- use --libdir=%{_prefix}/lib for bonobo server, fix bz (#3721)
- remove non needed BR gstreamer1-plugins-base-tools

* Wed Dec 31 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.1.3-1
- update to 0.1.3 release
- fix rpmmfusion bz (#3389)

* Tue Dec 02 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.1.2-2
- bump version

* Mon Dec 01 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.1.2-1
- update to 0.1.2 release

* Mon Sep 01 2014 Sérgio Basto <sergio@serjux.com> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 09 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.1.0-2
- fix build

* Wed Jul 09 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.1.0-1
- update to 0.1.0

* Sat Dec 28 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.0.5-1
- update to 0.0.5

* Tue Nov 05 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.0.4-3
- bump version again

* Tue Nov 05 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.0.4-2
- bump version

* Tue Nov 05 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.0.4-1
- update to 0.0.4

* Tue Sep 17 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.0.1-3
- rebuild against new source
- remove PackageKit-glib-devel BR
- add sqlite-devel BR

* Tue Sep 17 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.0.1-2
- initial build for rpmfusion free

* Sun Sep 1 2013 Assen Totin <assen.totin@gmail.com> - 0.0.1-1
- Release 0.0.1
