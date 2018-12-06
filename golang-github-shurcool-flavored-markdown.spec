# Run tests in check section
%bcond_without check

%global goipath         github.com/shurcooL/github_flavored_markdown
%global commit          2122de53247006a637e59cf1c99d0770312d4be3

%global common_description %{expand:
github_flavored_markdown provides a GitHub Flavored Markdown renderer 
with fenced code block highlighting, clickable heading anchor links.

The functionality should be equivalent to the GitHub Markdown API endpoint 
specified at 
https://developer.github.com/v3/markdown/#render-a-markdown-document-in-raw-mode
, except the rendering is performed locally.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.4%{?dist}
Summary:        GitHub Flavored Markdown renderer
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(github.com/microcosm-cc/bluemonday)
BuildRequires: golang(gopkg.in/russross/blackfriday.v1)
BuildRequires: golang(github.com/shurcooL/highlight_diff)
BuildRequires: golang(github.com/shurcooL/highlight_go)
BuildRequires: golang(github.com/shurcooL/octicon)
BuildRequires: golang(github.com/shurcooL/sanitized_anchor_name)
BuildRequires: golang(github.com/sourcegraph/annotate)
BuildRequires: golang(github.com/sourcegraph/syntaxhighlight)
BuildRequires: golang(golang.org/x/net/html)
BuildRequires: golang(golang.org/x/net/html/atom)

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup

# Replace blackfriday import path to avoid conflict with v2
sed -i 's|"github.com/russross/blackfriday|"gopkg.in/russross/blackfriday.v1|' $(find . -name '*.go')


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%doc README.md


%changelog
* Fri Oct 26 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20181026git2122de5
- Rename octiconssvg to octicon

* Fri Oct 26 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.3.20181026git2122de5
- Bump to commit 2122de53247006a637e59cf1c99d0770312d4be3
- Replace blackfriday import path

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git28433ea
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 24 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180418git28433ea
- First package for Fedora

