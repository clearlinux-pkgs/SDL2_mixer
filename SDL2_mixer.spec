#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x30A59377A7763BE6 (slouken@libsdl.org)
#
Name     : SDL2_mixer
Version  : 2.0.4
Release  : 14
URL      : https://www.libsdl.org/projects/SDL_mixer/release/SDL2_mixer-2.0.4.tar.gz
Source0  : https://www.libsdl.org/projects/SDL_mixer/release/SDL2_mixer-2.0.4.tar.gz
Source99 : https://www.libsdl.org/projects/SDL_mixer/release/SDL2_mixer-2.0.4.tar.gz.sig
Summary  : Vorbis Library Development
Group    : Development/Tools
License  : Artistic-1.0-Perl BSD-3-Clause GFDL-1.2 GPL-2.0 LGPL-2.1 Zlib
Requires: SDL2_mixer-lib = %{version}-%{release}
Requires: SDL2_mixer-license = %{version}-%{release}
BuildRequires : SDL2-dev
BuildRequires : flac-dev
BuildRequires : mpg123-dev
BuildRequires : opus-dev
BuildRequires : opusfile-dev
BuildRequires : pkgconfig(libpulse-simple)
BuildRequires : pkgconfig(ogg)
BuildRequires : pkgconfig(openssl)
BuildRequires : pkgconfig(opus)
BuildRequires : pkgconfig(opusfile)
BuildRequires : pkgconfig(vorbisfile)

%description
Ogg Vorbis is a fully open, non-proprietary, patent-and-royalty-free,
general-purpose compressed audio format for audio and music at fixed 
and variable bitrates from 16 to 128 kbps/channel.

%package dev
Summary: dev components for the SDL2_mixer package.
Group: Development
Requires: SDL2_mixer-lib = %{version}-%{release}
Provides: SDL2_mixer-devel = %{version}-%{release}

%description dev
dev components for the SDL2_mixer package.


%package lib
Summary: lib components for the SDL2_mixer package.
Group: Libraries
Requires: SDL2_mixer-license = %{version}-%{release}

%description lib
lib components for the SDL2_mixer package.


%package license
Summary: license components for the SDL2_mixer package.
Group: Default

%description license
license components for the SDL2_mixer package.


%prep
%setup -q -n SDL2_mixer-2.0.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1541072814
%configure --disable-static
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1541072814
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/SDL2_mixer
cp COPYING.txt %{buildroot}/usr/share/package-licenses/SDL2_mixer/COPYING.txt
cp VisualC/external/lib/x64/LICENSE.FLAC.txt %{buildroot}/usr/share/package-licenses/SDL2_mixer/VisualC_external_lib_x64_LICENSE.FLAC.txt
cp VisualC/external/lib/x64/LICENSE.mpg123.txt %{buildroot}/usr/share/package-licenses/SDL2_mixer/VisualC_external_lib_x64_LICENSE.mpg123.txt
cp VisualC/external/lib/x64/LICENSE.ogg-vorbis.txt %{buildroot}/usr/share/package-licenses/SDL2_mixer/VisualC_external_lib_x64_LICENSE.ogg-vorbis.txt
cp VisualC/external/lib/x64/LICENSE.opus.txt %{buildroot}/usr/share/package-licenses/SDL2_mixer/VisualC_external_lib_x64_LICENSE.opus.txt
cp VisualC/external/lib/x64/LICENSE.opusfile.txt %{buildroot}/usr/share/package-licenses/SDL2_mixer/VisualC_external_lib_x64_LICENSE.opusfile.txt
cp VisualC/external/lib/x86/LICENSE.FLAC.txt %{buildroot}/usr/share/package-licenses/SDL2_mixer/VisualC_external_lib_x86_LICENSE.FLAC.txt
cp VisualC/external/lib/x86/LICENSE.mpg123.txt %{buildroot}/usr/share/package-licenses/SDL2_mixer/VisualC_external_lib_x86_LICENSE.mpg123.txt
cp VisualC/external/lib/x86/LICENSE.ogg-vorbis.txt %{buildroot}/usr/share/package-licenses/SDL2_mixer/VisualC_external_lib_x86_LICENSE.ogg-vorbis.txt
cp VisualC/external/lib/x86/LICENSE.opus.txt %{buildroot}/usr/share/package-licenses/SDL2_mixer/VisualC_external_lib_x86_LICENSE.opus.txt
cp VisualC/external/lib/x86/LICENSE.opusfile.txt %{buildroot}/usr/share/package-licenses/SDL2_mixer/VisualC_external_lib_x86_LICENSE.opusfile.txt
cp Xcode/Frameworks/FLAC.framework/Versions/A/Resources/LICENSE.FLAC.txt %{buildroot}/usr/share/package-licenses/SDL2_mixer/Xcode_Frameworks_FLAC.framework_Versions_A_Resources_LICENSE.FLAC.txt
cp Xcode/Frameworks/Ogg.framework/Versions/A/Resources/LICENSE.ogg-vorbis.txt %{buildroot}/usr/share/package-licenses/SDL2_mixer/Xcode_Frameworks_Ogg.framework_Versions_A_Resources_LICENSE.ogg-vorbis.txt
cp Xcode/Frameworks/Opus.framework/Versions/A/Resources/LICENSE.opus.txt %{buildroot}/usr/share/package-licenses/SDL2_mixer/Xcode_Frameworks_Opus.framework_Versions_A_Resources_LICENSE.opus.txt
cp Xcode/Frameworks/OpusFile.framework/Versions/A/Resources/LICENSE.opusfile.txt %{buildroot}/usr/share/package-licenses/SDL2_mixer/Xcode_Frameworks_OpusFile.framework_Versions_A_Resources_LICENSE.opusfile.txt
cp Xcode/Frameworks/Vorbis.framework/Versions/A/Resources/LICENSE.ogg-vorbis.txt %{buildroot}/usr/share/package-licenses/SDL2_mixer/Xcode_Frameworks_Vorbis.framework_Versions_A_Resources_LICENSE.ogg-vorbis.txt
cp Xcode/Frameworks/mpg123.framework/Versions/A/Resources/LICENSE.mpg123.txt %{buildroot}/usr/share/package-licenses/SDL2_mixer/Xcode_Frameworks_mpg123.framework_Versions_A_Resources_LICENSE.mpg123.txt
cp debian/copyright %{buildroot}/usr/share/package-licenses/SDL2_mixer/debian_copyright
cp external/flac-1.3.2/COPYING.FDL %{buildroot}/usr/share/package-licenses/SDL2_mixer/external_flac-1.3.2_COPYING.FDL
cp external/flac-1.3.2/COPYING.GPL %{buildroot}/usr/share/package-licenses/SDL2_mixer/external_flac-1.3.2_COPYING.GPL
cp external/flac-1.3.2/COPYING.LGPL %{buildroot}/usr/share/package-licenses/SDL2_mixer/external_flac-1.3.2_COPYING.LGPL
cp external/flac-1.3.2/COPYING.Xiph %{buildroot}/usr/share/package-licenses/SDL2_mixer/external_flac-1.3.2_COPYING.Xiph
cp external/flac-1.3.2/doc/html/license.html %{buildroot}/usr/share/package-licenses/SDL2_mixer/external_flac-1.3.2_doc_html_license.html
cp external/libogg-1.3.2/COPYING %{buildroot}/usr/share/package-licenses/SDL2_mixer/external_libogg-1.3.2_COPYING
cp external/libvorbis-1.3.5/COPYING %{buildroot}/usr/share/package-licenses/SDL2_mixer/external_libvorbis-1.3.5_COPYING
cp external/libvorbisidec-1.2.1/COPYING %{buildroot}/usr/share/package-licenses/SDL2_mixer/external_libvorbisidec-1.2.1_COPYING
cp external/mpg123-1.25.6/COPYING %{buildroot}/usr/share/package-licenses/SDL2_mixer/external_mpg123-1.25.6_COPYING
cp external/opus-1.0.3/COPYING %{buildroot}/usr/share/package-licenses/SDL2_mixer/external_opus-1.0.3_COPYING
cp external/opusfile-0.10/COPYING %{buildroot}/usr/share/package-licenses/SDL2_mixer/external_opusfile-0.10_COPYING
cp timidity/COPYING %{buildroot}/usr/share/package-licenses/SDL2_mixer/timidity_COPYING
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/SDL2/SDL_mixer.h
/usr/lib64/libSDL2_mixer.so
/usr/lib64/pkgconfig/SDL2_mixer.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libSDL2_mixer-2.0.so.0
/usr/lib64/libSDL2_mixer-2.0.so.0.2.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/SDL2_mixer/COPYING.txt
/usr/share/package-licenses/SDL2_mixer/VisualC_external_lib_x64_LICENSE.FLAC.txt
/usr/share/package-licenses/SDL2_mixer/VisualC_external_lib_x64_LICENSE.mpg123.txt
/usr/share/package-licenses/SDL2_mixer/VisualC_external_lib_x64_LICENSE.ogg-vorbis.txt
/usr/share/package-licenses/SDL2_mixer/VisualC_external_lib_x64_LICENSE.opus.txt
/usr/share/package-licenses/SDL2_mixer/VisualC_external_lib_x64_LICENSE.opusfile.txt
/usr/share/package-licenses/SDL2_mixer/VisualC_external_lib_x86_LICENSE.FLAC.txt
/usr/share/package-licenses/SDL2_mixer/VisualC_external_lib_x86_LICENSE.mpg123.txt
/usr/share/package-licenses/SDL2_mixer/VisualC_external_lib_x86_LICENSE.ogg-vorbis.txt
/usr/share/package-licenses/SDL2_mixer/VisualC_external_lib_x86_LICENSE.opus.txt
/usr/share/package-licenses/SDL2_mixer/VisualC_external_lib_x86_LICENSE.opusfile.txt
/usr/share/package-licenses/SDL2_mixer/Xcode_Frameworks_FLAC.framework_Versions_A_Resources_LICENSE.FLAC.txt
/usr/share/package-licenses/SDL2_mixer/Xcode_Frameworks_Ogg.framework_Versions_A_Resources_LICENSE.ogg-vorbis.txt
/usr/share/package-licenses/SDL2_mixer/Xcode_Frameworks_Opus.framework_Versions_A_Resources_LICENSE.opus.txt
/usr/share/package-licenses/SDL2_mixer/Xcode_Frameworks_OpusFile.framework_Versions_A_Resources_LICENSE.opusfile.txt
/usr/share/package-licenses/SDL2_mixer/Xcode_Frameworks_Vorbis.framework_Versions_A_Resources_LICENSE.ogg-vorbis.txt
/usr/share/package-licenses/SDL2_mixer/Xcode_Frameworks_mpg123.framework_Versions_A_Resources_LICENSE.mpg123.txt
/usr/share/package-licenses/SDL2_mixer/debian_copyright
/usr/share/package-licenses/SDL2_mixer/external_flac-1.3.2_COPYING.FDL
/usr/share/package-licenses/SDL2_mixer/external_flac-1.3.2_COPYING.GPL
/usr/share/package-licenses/SDL2_mixer/external_flac-1.3.2_COPYING.LGPL
/usr/share/package-licenses/SDL2_mixer/external_flac-1.3.2_COPYING.Xiph
/usr/share/package-licenses/SDL2_mixer/external_flac-1.3.2_doc_html_license.html
/usr/share/package-licenses/SDL2_mixer/external_libogg-1.3.2_COPYING
/usr/share/package-licenses/SDL2_mixer/external_libvorbis-1.3.5_COPYING
/usr/share/package-licenses/SDL2_mixer/external_libvorbisidec-1.2.1_COPYING
/usr/share/package-licenses/SDL2_mixer/external_mpg123-1.25.6_COPYING
/usr/share/package-licenses/SDL2_mixer/external_opus-1.0.3_COPYING
/usr/share/package-licenses/SDL2_mixer/external_opusfile-0.10_COPYING
/usr/share/package-licenses/SDL2_mixer/timidity_COPYING
