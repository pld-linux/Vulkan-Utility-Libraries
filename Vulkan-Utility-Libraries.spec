%define	api_version	1.4.309.0
%define	gitref		vulkan-sdk-%{api_version}

Summary:	Vulkan Utility Libraries
Summary(pl.UTF-8):	Biblioteki narzędziowe projektu Vulkan
Name:		Vulkan-Utility-Libraries
Version:	%{api_version}
Release:	1
License:	Apache v2.0
Group:		Development/Libraries
#Source0Download: https://github.com/KhronosGroup/Vulkan-Utility-Libraries/releases
Source0:	https://github.com/KhronosGroup/Vulkan-Utility-Libraries/archive/%{gitref}/%{name}-%{gitref}.tar.gz
# Source0-md5:	39650f99048e010f80dc07c3478b3415
URL:		https://github.com/KhronosGroup/Vulkan-Utility-Libraries
BuildRequires:	Vulkan-Headers >= %{api_version}
BuildRequires:	cmake >= 3.22.1
BuildRequires:	libstdc++-devel >= 6:7
BuildRequires:	python3 >= 1:3.8
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# don't work with static libraries
%undefine	_debugsource_packages

%description
This subproject was created to share code across various Vulkan
repositories, solving long standing issues for Vulkan SDK developers
and users.

%description -l pl.UTF-8
Ten podprojekt ma na celu współdzielenie kodu między różnymi
repozytoriami projektu Vulkan.

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

%files
%defattr(644,root,root,755)
%doc LICENSE.md README.md docs/layer_configuration.md
%{_libdir}/libVulkanLayerSettings.a
%{_libdir}/libVulkanSafeStruct.a
%{_includedir}/vulkan/layer
%{_includedir}/vulkan/utility
%{_includedir}/vulkan/vk_enum_string_helper.h
%{_libdir}/cmake/VulkanUtilityLibraries
