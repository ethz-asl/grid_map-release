Name:           ros-indigo-grid-map-rviz-plugin
Version:        1.4.1
Release:        0%{?dist}
Summary:        ROS grid_map_rviz_plugin package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       qt5-qtbase
Requires:       qt5-qtbase-gui
Requires:       ros-indigo-grid-map-msgs
Requires:       ros-indigo-grid-map-ros
Requires:       ros-indigo-rviz
BuildRequires:  qt5-qtbase-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-grid-map-msgs
BuildRequires:  ros-indigo-grid-map-ros
BuildRequires:  ros-indigo-rviz

%description
RViz plugin for displaying grid_map messages.

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
* Sun Oct 23 2016 Philipp Krüsi <kruesip@ethz.ch> - 1.4.1-0
- Autogenerated by Bloom

* Mon Aug 22 2016 Philipp Krüsi <kruesip@ethz.ch> - 1.4.0-0
- Autogenerated by Bloom

