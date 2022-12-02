%global octpkg level-set
%define Werror_cflags	%{nil}

Summary:	Calculating the time-evolution of the level-set equation with Octave
Name:		octave-%{octpkg}
Version:	0.3.1
Release:	1
# published package v0.3.0 is too old so build a new one from git
#  git clone https://git.code.sf.net/p/octave/level-set octave-level-set
#  cd octave-level-set
#  git checkout dbf46228a7582eef4fe5470fd00bc5b421dd33a5
#  sh ./build.sh
#  mv level-set-0.3.1.tar.gz ..
#  cd ..
Source0:	https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
# https://savannah.gnu.org/bugs/index.php?58842
Patch0:		octave5.patch
# https://savannah.gnu.org/bugs/index.php?59668
Patch1:		bist-unload-parallel.patch
# https://savannah.gnu.org/bugs/index.php?61475
Patch2:		honor-cppflags.patch
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/%{octpkg}/

BuildRequires:	octave-devel >= 4.0.0
BuildRequires:	octave-parallel

Requires:	octave(api) = %{octave_api}
Requires:	octave-parallel

Requires(post): octave
Requires(postun): octave

%description
Routines for calculating the time-evolution of the level-set equation and
extracting geometric information from the level-set function.

%files
%license COPYING
%doc NEWS
%dir %{octpkglibdir}
%{octpkglibdir}/*
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}

# remove backup files
find . -name \*~ -delete

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

