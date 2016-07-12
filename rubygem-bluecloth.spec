Name     : rubygem-bluecloth
Version  : 2.2.0
Release  : 9
URL      : https://rubygems.org/downloads/bluecloth-2.2.0.gem
Source0  : https://rubygems.org/downloads/bluecloth-2.2.0.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: rubygem-bluecloth-bin
Requires: rubygem-bluecloth-lib
BuildRequires : ruby
BuildRequires : rubygem-devise
BuildRequires : rubygem-diff-lcs
BuildRequires : rubygem-hoe
BuildRequires : rubygem-hoe-mercurial
BuildRequires : rubygem-rake
BuildRequires : rubygem-rake-compiler
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rspec
BuildRequires : rubygem-rspec-core
BuildRequires : rubygem-rspec-expectations
BuildRequires : rubygem-rspec-mocks
BuildRequires : rubygem-rspec-support
BuildRequires : rubygem-test-unit
BuildRequires : rubygem-tidy-ext

%description
= bluecloth 2
* http://deveiate.org/projects/BlueCloth
== Description
BlueCloth is a Ruby implementation of John Gruber's
Markdown[http://daringfireball.net/projects/markdown/], a text-to-HTML
conversion tool for web writers. To quote from the project page: Markdown
allows you to write using an easy-to-read, easy-to-write plain text format,
then convert it to structurally valid XHTML (or HTML).

%package bin
Summary: bin components for the rubygem-bluecloth package.
Group: Binaries

%description bin
bin components for the rubygem-bluecloth package.


%package lib
Summary: lib components for the rubygem-bluecloth package.
Group: Libraries

%description lib
lib components for the rubygem-bluecloth package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n bluecloth-2.2.0
gem spec %{SOURCE0} -l --ruby > rubygem-bluecloth.gemspec

%build
gem build rubygem-bluecloth.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
bluecloth-2.2.0.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/bluecloth-2.2.0
rspec -I.:lib spec/ || :
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/bluecloth-2.2.0.gem
/usr/lib64/ruby/gems/2.3.0/extensions/x86_64-linux/2.3.0/bluecloth-2.2.0/gem.build_complete
/usr/lib64/ruby/gems/2.3.0/extensions/x86_64-linux/2.3.0/bluecloth-2.2.0/gem_make.out
/usr/lib64/ruby/gems/2.3.0/extensions/x86_64-linux/2.3.0/bluecloth-2.2.0/mkmf.log
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/.gemtest
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/.rspec
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/History.rdoc
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/LICENSE.discount
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/Manifest.txt
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/README.rdoc
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/bin/bluecloth
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/bluecloth.1.pod
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/ext/.RUBYARCHDIR.time
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/ext/Csio.c
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/ext/Csio.o
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/ext/Makefile
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/ext/VERSION
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/ext/amalloc.h
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/ext/bluecloth.c
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/ext/bluecloth.h
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/ext/bluecloth.o
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/ext/config.h
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/ext/css.c
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/ext/css.o
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/ext/cstring.h
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/ext/docheader.c
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/ext/docheader.o
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/ext/emmatch.c
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/ext/emmatch.o
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/ext/extconf.h
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/ext/extconf.rb
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/ext/generate.c
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/ext/generate.o
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/ext/html5.c
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/ext/html5.o
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/ext/markdown.c
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/ext/markdown.h
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/ext/markdown.o
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/ext/mkdio.c
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/ext/mkdio.h
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/ext/mkdio.o
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/ext/resource.c
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/ext/resource.o
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/ext/setup.c
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/ext/setup.o
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/ext/tags.c
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/ext/tags.h
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/ext/tags.o
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/ext/version.c
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/ext/version.o
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/ext/xml.c
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/ext/xml.o
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/ext/xmlpage.c
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/ext/xmlpage.o
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/lib/bluecloth.rb
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/man/man1/bluecloth.1
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/spec/bluecloth/101_changes_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/spec/bluecloth/TEMPLATE
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/spec/bluecloth/autolinks_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/spec/bluecloth/blockquotes_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/spec/bluecloth/code_spans_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/spec/bluecloth/emphasis_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/spec/bluecloth/entities_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/spec/bluecloth/hrules_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/spec/bluecloth/images_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/spec/bluecloth/inline_html_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/spec/bluecloth/links_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/spec/bluecloth/lists_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/spec/bluecloth/paragraphs_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/spec/bluecloth/titles_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/spec/bluecloth_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/spec/bugfix_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/spec/contributions_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/spec/data/antsugar.txt
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/spec/data/markdowntest/*
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/spec/data/ml-announce.txt
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/spec/data/re-overflow.txt
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/spec/data/re-overflow2.txt
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/spec/discount_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/spec/lib/constants.rb
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/spec/lib/helpers.rb
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/spec/lib/matchers.rb
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/spec/markdowntest_spec.rb
/usr/lib64/ruby/gems/2.3.0/specifications/bluecloth-2.2.0.gemspec

%files bin
%defattr(-,root,root,-)
/usr/bin/bluecloth

%files lib
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/extensions/x86_64-linux/2.3.0/bluecloth-2.2.0/bluecloth_ext.so
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/ext/bluecloth_ext.so
/usr/lib64/ruby/gems/2.3.0/gems/bluecloth-2.2.0/lib/bluecloth_ext.so
