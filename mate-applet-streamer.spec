Name:           mate-applet-streamer
Version:        0.3.10
Release:        1%{?dist}
Summary:        MATE online radio streamer applet
Group:          Applications/System
License:        GPLv2+
URL:            http://www.zavedil.com/online-radio-applet
Source:         http://www.zavedil.com/wp-content/uploads/2016/01/%{name}-%{version}.tar.gz

BuildRequires:  libnotify-devel
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  gstreamer1-plugins-base-tools
BuildRequires:  gtk2-devel
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
%setup -q

%build
%configure \
    --libdir=%{_prefix}/lib \
    --enable-gtk=2 \
    --enable-notify \
    --enable-gstreamer=1.0

make %{?_smp_mflags} V=1

%install
%{make_install}

# Do not install doc files: they are handled as rpm doc files.
rm -rf ${RPM_BUILD_ROOT}%{_docdir}
rm -rf ${RPM_BUILD_ROOT}%{_datadir}/glib-2.0/schemas/gschemas.compiled

%find_lang %{name}


%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :


%files -f %{name}.lang
%doc AUTHORS BUGS COPYING ChangeLog README TODO
%{_libexecdir}/streamer_applet
%{_prefix}/lib/bonobo/servers/StreamerAppletFactory.server
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.StreamerApplet.gschema.xml
%{_datadir}/mate-panel/applets/org.mate.applets.StreamerApplet.mate-panel-applet
%{_datadir}/dbus-1/services/org.mate.panel.applet.StreamerApplet.service
%dir %{_datadir}/streamer_applet
%{_datadir}/streamer_applet/streamer.sqlite
%{_datadir}/pixmaps/applet_streamer*.png
%{_datadir}/icons/hicolor/*/apps/applet_streamer.png


%changelog
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
