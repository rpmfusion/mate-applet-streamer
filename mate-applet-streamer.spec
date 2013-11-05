Name:           mate-applet-streamer
Version:        0.0.4
Release:        1%{?dist}
Summary:        MATE online radio streamer applet
Group:          Applications/System
License:        GPLv2+
URL:            http://www.zavedil.com/online-radio-applet
Source:         http://www.zavedil.com/wp-content/uploads/2013/11/%{name}-%{version}.tar.gz

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
%configure

make %{?_smp_mflags} V=1

%install
%{make_install}

# Do not install doc files: they are handled as rpm doc files.
rm -rf ${RPM_BUILD_ROOT}%{_docdir}

%find_lang %{name}


%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files -f %{name}.lang
%doc AUTHORS BUGS COPYING ChangeLog README TODO
%{_libexecdir}/streamer_applet
%{_libdir}/bonobo/servers/StreamerAppletFactory.server
%{_datadir}/mate-panel/applets/org.mate.applets.StreamerApplet.mate-panel-applet
%{_datadir}/dbus-1/services/org.mate.panel.applet.StreamerApplet.service
%dir %{_datadir}/streamer_applet
%{_datadir}/streamer_applet/streamer.sqlite
%{_datadir}/pixmaps/applet_streamer*.png
%{_datadir}/icons/hicolor/*/apps/applet_streamer.png

%changelog
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
