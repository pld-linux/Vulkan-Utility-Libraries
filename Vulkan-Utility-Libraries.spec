%define	api_version	1.4.363.0
%define	gitref		vulkan-sdk-%{api_version}

Summary:	Vulkan Utility Libraries
Summary(pl.UTF-8):	Biblioteki narzędziowe projektu Vulkan
Name:		Vulkan-Utility-Libraries
Version:	%{api_version}
Release:	1
License:	Apache v2.0
Group:		Libraries
#Source0Download: https://github.com/KhronosGroup/Vulkan-Utility-Libraries/releases
Source0:	https://github.com/KhronosGroup/Vulkan-Utility-Libraries/archive/%{gitref}/%{name}-%{gitref}.tar.gz
# Source0-md5:	2da9264c0c1b5d6bc98352557390bb05
URL:		https://github.com/KhronosGroup/Vulkan-Utility-Libraries
BuildRequires:	Vulkan-Headers >= %{api_version}
BuildRequires:	cmake >= 3.22.1
BuildRequires:	libstdc++-devel >= 6:7
BuildRequires:	python3 >= 1:3.8
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This subproject was created to share code across various Vulkan
repositories, solving long standing issues for Vulkan SDK developers
and users.

%description -l pl.UTF-8
Ten podprojekt ma na celu współdzielenie kodu między różnymi
repozytoriami projektu Vulkan.

%package devel
Summary:	Header files for Vulkan Utility Libraries
Summary(pl.UTF-8):	Pliki nagłówkowe Vulkan Utility Libraries
Group:		Development/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Header files for Vulkan Utility Libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe Vulkan Utility Libraries.

%prep
%setup -q -n %{name}-%{gitref}

%build
%cmake -B build \
	-DBUILD_TESTS=OFF

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE.md README.md docs/layer_configuration.md
%{_libdir}/libVulkanLayerSettings.so
%{_libdir}/libVulkanSafeStruct.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/vulkan/layer
%{_includedir}/vulkan/utility
%{_includedir}/vulkan/vk_enum_string_helper.h
%{_libdir}/cmake/VulkanUtilityLibraries
