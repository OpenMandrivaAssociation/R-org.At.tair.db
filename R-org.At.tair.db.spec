%bcond_with bootstrap
%global packname  org.At.tair.db
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          2.9.0
Release:          1
Summary:          Genome wide annotation for Arabidopsis
Group:            Sciences/Mathematics
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/data/annotation/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/annotation/src/contrib/org.At.tair.db_2.9.0.tar.gz
BuildArch:        noarch
Requires:         R-core R-methods R-AnnotationDbi
%if %{without bootstrap}
Requires:         R-hgu95av2.db R-RUnit
%endif
Requires:         R-annotate
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-methods
BuildRequires:    R-methods R-AnnotationDbi R-annotate
%if %{without bootstrap}
BuildRequires:    R-hgu95av2.db R-RUnit
%endif

%description
Genome wide annotation for Arabidopsis, primarily based on mapping using
TAIR identifiers.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{without bootstrap}
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/help

