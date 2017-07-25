Name:           ros-indigo-grid-map-demos
Version:        1.5.2
Release:        0%{?dist}
Summary:        ROS grid_map_demos package

Group:          Development/Libraries
License:        BSD
URL:            http://github.com/ethz-asl/grid_map
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-cv-bridge
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-grid-map-cv
Requires:       ros-indigo-grid-map-loader
Requires:       ros-indigo-grid-map-msgs
Requires:       ros-indigo-grid-map-octomap
Requires:       ros-indigo-grid-map-ros
Requires:       ros-indigo-grid-map-rviz-plugin
Requires:       ros-indigo-grid-map-visualization
Requires:       ros-indigo-octomap-msgs
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cv-bridge
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-grid-map-cv
BuildRequires:  ros-indigo-grid-map-loader
BuildRequires:  ros-indigo-grid-map-msgs
BuildRequires:  ros-indigo-grid-map-octomap
BuildRequires:  ros-indigo-grid-map-ros
BuildRequires:  ros-indigo-grid-map-rviz-plugin
BuildRequires:  ros-indigo-grid-map-visualization
BuildRequires:  ros-indigo-octomap-msgs
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sensor-msgs

%description
Demo nodes to demonstrate the usage of the grid map library.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Tue Jul 25 2017 Péter Fankhauser <pfankhauser@ethz.ch> - 1.5.2-0
- Autogenerated by Bloom

* Tue Jul 25 2017 Péter Fankhauser <pfankhauser@ethz.ch> - 1.5.1-0
- Autogenerated by Bloom

* Tue Jul 18 2017 Péter Fankhauser <pfankhauser@ethz.ch> - 1.5.0-0
- Autogenerated by Bloom

* Tue Jan 24 2017 Péter Fankhauser <pfankhauser@ethz.ch> - 1.4.2-0
- Autogenerated by Bloom

* Sun Oct 23 2016 Péter Fankhauser <pfankhauser@ethz.ch> - 1.4.1-0
- Autogenerated by Bloom

* Mon Aug 22 2016 Péter Fankhauser <pfankhauser@ethz.ch> - 1.4.0-0
- Autogenerated by Bloom

* Tue May 10 2016 Péter Fankhauser <pfankhauser@ethz.ch> - 1.3.1-0
- Autogenerated by Bloom

* Tue Apr 26 2016 Péter Fankhauser <pfankhauser@ethz.ch> - 1.3.0-0
- Autogenerated by Bloom

* Thu Mar 03 2016 Péter Fankhauser <pfankhauser@ethz.ch> - 1.2.0-0
- Autogenerated by Bloom

* Mon Jan 11 2016 Péter Fankhauser <pfankhauser@ethz.ch> - 1.1.3-0
- Autogenerated by Bloom

* Mon Jan 11 2016 Péter Fankhauser <pfankhauser@ethz.ch> - 1.1.2-0
- Autogenerated by Bloom

* Mon Jan 11 2016 Péter Fankhauser <pfankhauser@ethz.ch> - 1.1.1-0
- Autogenerated by Bloom

* Fri Jan 08 2016 Péter Fankhauser <pfankhauser@ethz.ch> - 1.1.0-0
- Autogenerated by Bloom

